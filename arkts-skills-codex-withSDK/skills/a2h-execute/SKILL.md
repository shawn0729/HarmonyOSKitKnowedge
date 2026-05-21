---
name: a2h-execute
description: 第三步：三阶段执行引擎。Stage 1 UI Pipeline（a2h-activity-converter agent 逐页转换）→ Stage 2 Feature Base（水平基础设施）→ Stage 3 Feature Slices（垂直切片 4 步流）。支持部分执行、FAILED 重试、编译闭环。即使用户只说"执行"或"开始"，也应触发。
---

# a2h-execute

## 1. 定位

Pipeline 层第三步，**三阶段执行引擎**。读取 a2h-plan 生成的双计划（ui-plan.md + feature-plan.md），按三阶段顺序执行迁移。

```
a2h-spec → a2h-plan → a2h-execute（本 skill）
                          │
                          ├─ Stage 1: UI Pipeline
                          │   └─ a2h-activity-converter agent × N 页面
                          │
                          ├─ Stage 2: Feature Base
                          │   └─ a2h-migration-worker × Base 任务
                          │
                          └─ Stage 3: Feature Slices
                              └─ a2h-migration-worker × Slice × 4 步
```

**核心原则**：a2h-execute 是**编排层**，本 skill 自身**禁止**调用 Edit / Write 工具去改 `.ets`、ViewModel、Repository、Base 层文件。所有实际工作必须通过 Codex subagent 派发：Stage 1 派发 `@a2h-activity-converter`，Stage 2 / Stage 3 派发 `@a2h-migration-worker`。

### Codex 派发语义（本文件所有"派发"段落均按此语义执行）

本 skill 的执行主体是 Codex 主会话（父 agent）。当流程要求"派发 Agent X 去做 T"时，父 agent 在本轮输出中应显式触发 subagent，形如：

```
@<agent-name>
<结构化 prompt——含 activity_name / output_file / allowed_write_paths 等所有参数>
```

- 触发后**必须等待** subagent 返回，再继续后续步骤；禁止父 agent 边等边自己动手。
- 并行页面 → 在同一轮里并列多个 `@a2h-activity-converter` 派发块，每块一个页面。
- 如果 Codex 版本不支持 `@` 触发，退化方案是用自然语言显式请求："请以 subagent `a2h-activity-converter` 身份处理以下任务：…"；仍然**禁止**父 agent 直接写 `.ets`。

### 新增硬约束（违反即视为本轮失败）

- Stage 1 只有在真实派发 `.codex/agents/a2h-activity-converter.toml` 之后，页面才允许进入 executed / converted 生命周期。
- 父 agent 不得用 Edit / Write 本地直改页面文件代替 Stage 1 subagent 产出。**唯一例外**：subagent 误删或写坏目标文件后的应急恢复——恢复到可读状态后**必须立即重新派发**该页 agent 完成真正转换，不得以恢复结果顶替。
- Stage 2 Base 任务、Stage 3 Slice 各步骤（ViewModel / Repository / 数据接入）同样**必须**派发 `@a2h-migration-worker`，父 agent 不得"顺手写一下"。
- 所有编译门禁都以**主工作区**结果为准；subagent 在自己上下文里宣称"已编译通过"不能直接作为 batch 完成依据。父 agent 必须在主工作区通过 `$hmos_fix_build_errors` 重新编译。

---

## 2. 输入

自动读取 `spec/baseline/plans/` 下已审批的双计划文件：

| 文件 | 用途 | 消费阶段 |
|------|------|---------|
| `spec/baseline/plans/ui-plan.md` | UI 转换计划：按批次分组的页面列表 | Stage 1 |
| `spec/baseline/plans/feature-plan.md` | 功能执行计划：Base 层 + Feature Slices | Stage 2, Stage 3 |

启动时检查：
- `spec/baseline/plans/` 目录是否存在
- `ui-plan.md` 和 `feature-plan.md` 是否存在
- 如果不存在或为空 → 提示用户先执行 `a2h-plan`

辅助文件（执行过程中读取）：

| 文件 | 用途 |
|------|------|
| `spec/baseline/ui-manifest.md` | 页面状态追踪（pending/converted/verified） |
| `spec/baseline/feature-base.md` | Base 层公共能力定义 |
| `spec/baseline/features/F-xxx.md` | 各功能详细 Spec |
| `spec/baseline/ui/page_NNNN.md` | 各页面详细 UI Spec |
| `spec/placeholder-registry.md` | 占位符注册表 |
| `spec/migration-report.md` | 执行过程记录、agent ownership、编译门禁结果 |

可复用执行提示词模板见：`references/new-project-prompt-templates.md`

---

## 3. Stage 1: UI Pipeline

Stage 1 读取 `ui-plan.md`，按批次调用 `a2h-activity-converter` agent 将 Android 页面转换为 ArkTS。

### 3a. 执行流程

```
读取 ui-plan.md
  │
  ▼
Batch 1:
  ├─ Page A → spawn a2h-activity-converter
  ├─ Page B → spawn a2h-activity-converter  [可并行]
  ├─ Page C → spawn a2h-activity-converter  [可并行]
  ├─ 等待本批所有 Agent 完成
  ├─ hmos_fix_build_errors 编译验证
  └─ 更新 ui-manifest.md: status pending → converted
  │
  ▼
Batch 2:
  ├─ Page D → spawn a2h-activity-converter
  ├─ ...
  ├─ hmos_fix_build_errors 编译验证
  └─ 更新 ui-manifest.md: status pending → converted
  │
  ▼
... 直到所有 Batch 完成
```

### 3a-hard. Stage 1 强约束

- 每个页面必须建立 `page_id -> agent_id -> output_file -> allowed_write_paths` 的 ownership 映射，并记录到 `spec/migration-report.md`
- 没有真实 `spawn_agent(agent_type=a2h-activity-converter)` 的页面，不得标记为已执行
- Stage 1 主执行器不得直接修改目标页面 `.ets` 代替 agent 产出
- page agent 一旦越权修改 `allowed_write_paths` 之外的文件，直接判定该次转换 FAIL，需要缩小权限后重跑
- page agent 如果只输出分析、未真正写入目标文件，也不得视为完成

### 3a-pre. 数据完整性预检查（Stage 1 每页派发前）

对当前 Batch 中每个待转换页面 page_NNNN，在派发 converter agent 前检查三源数据完整性：

| meta.json 状态 | view.xml 状态 | 处理 |
|---------------|-------------|------|
| ✓ 含 layout_sources | ✓ 存在 | 运行 `synthesize_meta_json.py --mode enrich` 补充缺失字段，然后派发 |
| ✓ 含 layout_sources | ✗ 缺失 | 调用 `synthesize_view_xml.py` 补充 view.xml → `synthesize_meta_json.py --mode enrich` → 派发 |
| ✗ 缺失或无 layout_sources | — | `synthesize_meta_json.py --mode scaffold` → Phase A 按需 → `synthesize_view_xml.py` → enrich → 派发 |

补充合成 view.xml 的调用方式：
```bash
python3 .agents/skills/android-ui-graph-builder/scripts/synthesize_view_xml.py \
  $ANDROID_SRC \
  --layouts "{meta.json.layout_sources 逗号拼接}" \
  --output spec/baseline/ui-snapshots/page_NNNN_XxxActivity/view.xml \
  --package {package}
```

补充/修正 meta.json 确定性字段的调用方式：
```bash
python3 .agents/skills/android-ui-graph-builder/scripts/synthesize_meta_json.py \
  $ANDROID_SRC \
  --activity {fully_qualified_class_name} \
  --page-id {page_id} \
  --output spec/baseline/ui-snapshots/page_NNNN_XxxActivity/meta.json \
  --mode enrich \
  --existing spec/baseline/ui-snapshots/page_NNNN_XxxActivity/meta.json \
  --view-xml spec/baseline/ui-snapshots/page_NNNN_XxxActivity/view.xml \
  --package {package}
```

注意：预检查在 Batch 级别批量执行。同一 Batch 内多个页面缺 view.xml 时，可并行调用脚本合成。enrich 模式确保所有 meta.json 字段完整（`menu_sources`、`fragment_tags`、`recycler_item_layouts` 等），避免 LLM 遗漏导致的字段缺失。

### 3b. Agent 派发方式（Stage 1 专用）

Stage 1 **必须**派发 `@a2h-activity-converter`（**不是** `@a2h-migration-worker`，也不是父 agent 自己写）。

每个页面作为一次独立的 subagent 派发，父 agent 按下面的模板输出派发块（直接触发 Codex subagent 机制）：

```
@a2h-activity-converter

任务：将 {activity_name} 从 Android 迁移到 ArkTS。

必填参数:
- activity_name: {activity_name}
- ui_info: {ui_snapshots_path}
- harmony_project_dir: {harmony_project_dir}
- references_dir: {references_dir}
- android_source_dir: {android_source_dir}
- output_file: {target_ets_path}
- allowed_write_paths: [{target_ets_path}]
- preserve_contract_from_existing_file: true
- compile_in_parent_workspace: true

额外上下文:
- 页面 Spec: spec/baseline/ui/page_{page_id}.md
- 公共组件库路径: entry/src/main/ets/components/common/（如 Stage 2 已完成，请引用这些组件作为样式锚点）
- 现有路由/状态契约：如目标页已存在，必须兼容现有 exported component 名、参数、flow.route 协议
- 缺失 string/resource 时：先报告缺口，不得顺手改 string.json / 共享组件 / 其他页面
- 完成后返回结构化转换报告（touched files + preserved contracts + unresolved resource gaps + assumptions）。
```

**派发规则**：
- 每个页面一个独立派发块（即使同一 Batch 并行也是并列多个块，不要合并）
- 父 agent 派发后必须**等待 subagent 返回**再继续；不要边等边自己 Edit `.ets`
- 若本轮 Codex 未真正进入 subagent（例如用户未授权 agent 模式），父 agent 应**停下**并提示用户："当前轮未真正派发 `a2h-activity-converter`，按 AGENTS.md 硬约束，本 skill 不代写页面文件。请确认允许 subagent 派发后重试。"

**关键参数说明**：

| 参数 | 含义 | 来源 |
|------|------|------|
| `activity_name` | 目标 Android Activity 类名 | ui-plan.md 的 Android 来源列 |
| `ui_info` | UIAutomator 快照目录路径（含 view.xml + meta.json） | 项目中的 ui-snapshots 目录 |
| `harmony_project_dir` | HarmonyOS 工程根目录 | 当前项目路径 |
| `references_dir` | 领域知识和映射参考文件目录 | .agents/skills/android-ui-graph-query/references/ |
| `android_source_dir` | Android 源码根目录 | 用户提供的 $ANDROID_SRC |
| `output_file` | 本页唯一允许落盘的目标文件 | ui-manifest / plan 推导 |
| `allowed_write_paths` | 本次 agent 允许写入的白名单 | 默认仅 `output_file` |
| `preserve_contract_from_existing_file` | 保留已有页面对外契约 | 默认 true |
| `compile_in_parent_workspace` | 提醒 agent 不要自行把编译当成完成依据 | 默认 true |

**三源数据**：converter agent 消费三种数据源：
1. `view.xml` — UIAutomator dump 的视图层次
2. `meta.json` — 页面元数据（可交互元素、导航路径等）
3. 源码 layout XML — Android 原始布局文件（通过 `android_source_dir` + Activity 源码中的 `setContentView` 定位）

**派发 Prompt 必带约束**：
- 明确声明“只允许修改 `output_file`”
- 明确声明“不要修改 string.json、公共组件、其他页面，除非额外授权”
- 明确声明“不要编译；编译由主执行器在主工作区统一执行”
- 明确声明“如果现有文件被误删/误写，必须先恢复可读状态，再继续输出”

### 3c. 批内并行与顺序约束

- `ui-plan.md` 中标注"可并行"的页面 → 同时派发多个 Agent
- 有依赖关系的页面 → 按依赖顺序串行
- 每批内的所有 Agent 必须全部完成后，才执行该批的编译检查

### 3d. 编译检查点（per-batch, parent workspace only）

每个 Batch 完成后：

1. 主执行器在**主工作区**调用编译命令或 `hmos_fix_build_errors` 执行批次级检查
2. 子 agent 自己的编译结论只作参考，不能直接更新页面状态
3. 若错误集中在本 Batch 页面文件：
   - 按 `output_file` ownership 将错误回灌给对应 page agent
   - 每页最多 3 轮“编译失败 -> agent 修复 -> 重编译”
   - 主执行器只负责错误归因与重派发，不直接代写页面逻辑
4. 若错误落在共享文件（如 `EntryAbility.ets`、`main_pages.json`、公共组件、资源文件）：
   - 显式创建新的 ownership task
   - 使用 `a2h-migration-worker` 或用户批准的 shared-file 修复流程处理
   - 禁止把共享文件 hotfix 混入某个 page agent 的单页 ownership
5. 编译通过后，才更新 `spec/baseline/ui-manifest.md`，将本批页面 status 从 `pending` 改为 `converted`
6. 3 轮 page repair 或 20 轮共享修复仍失败 → 记录失败原因，标记失败页面，继续下一批（除非用户指定 blocking）

### 3d-post. 入口页面注册

Stage 1 第一个 Batch 编译通过后，检查并更新入口页面配置：

1. 读取 `entry/src/main/resources/base/profile/main_pages.json`
2. 检查 `"src"` 数组是否包含已转换的主页面（如 `"pages/MainPage"`）
3. 如果只有默认的 `"pages/Index"`：
   - 将 Launcher Activity 对应的 ArkTS 页面加入 `"src"` 数组首位
   - 保留 `"pages/Index"` 在数组中（不删除，避免其他引用断裂）
4. 确保所有已转换的页面都在 `"src"` 数组中注册（Navigation 路由页面也需要）
5. **同步修改 EntryAbility.ets 的 `loadContent` 调用**：
   - 读取 `entry/src/main/ets/entryability/EntryAbility.ets`
   - 将 `windowStage.loadContent('pages/Index', ...)` 改为 `windowStage.loadContent('pages/{MainPage}', ...)`（其中 `{MainPage}` 为 Launcher Activity 对应的 ArkTS 页面名）
   - 这一步必须与 main_pages.json 首项保持一致，否则运行时仍会加载默认 Hello World 页面

### 3e. Stage 1 完成标志

所有 Batch 执行完毕，输出 Stage 1 统计：

```
Stage 1 完成:
- 总页面: X
- 成功转换: Y (status: converted)
- 失败: Z (需人工介入)
- 编译状态: PASS / PARTIAL
```

---

## 4. Stage 2: Feature Base（水平基础设施）

Stage 2 读取 `feature-plan.md` 的 Phase 0 Base 层任务，按顺序执行公共基础设施建设。

### 4a. 执行流程

```
读取 feature-plan.md → 提取 Phase 0 Base 层任务列表
  │
  ▼
Base-1: Models → spawn a2h-migration-worker
  ▼
Base-2: Database → spawn a2h-migration-worker
  ▼
Base-3: Network → spawn a2h-migration-worker
  ▼
Base-4: Events → spawn a2h-migration-worker
  ▼
Base-5: Preferences → spawn a2h-migration-worker
  ▼
Base-6: 公共组件库 → spawn a2h-migration-worker
  ▼
Base-7: 编译验证 → hmos_fix_build_errors
```

### 4b. Agent 派发方式（Stage 2/3 通用）

Stage 2 和 Stage 3 的所有任务**必须**派发 `@a2h-migration-worker`。父 agent 按下面模板输出派发块：

```
@a2h-migration-worker

任务: {task_name}
描述: {task_description}
详细信息: {task_details}

使用 Skill: {suggested_skills}   （形如 $arkts-data-layer、$arkts-state-manager）
输入来源: {task_input_source}
output_paths: {task_output_path_list}
allowed_write_paths: {task_output_path_list}

Android 源码路径: {android_source_dir}
HarmonyOS 项目路径: {harmony_project_dir}

验收标准:
{task_acceptance_criteria}

占位符登记:
如果本任务生成任何占位符代码（TODO 注释、console.info('TODO:...')、空回调等），
必须把每个占位符同步写入 spec/placeholder-registry.md。不登记视为任务未完成。
```

**派发规则**：
- 同一 Base 任务只派发一个 worker；worker 返回后父 agent 在主工作区编译，不接受 worker 自报"编译通过"
- Stage 3 Slice 的 4 步（3a UI 补充 / 3b ViewModel / 3c 数据层 / 3d 验证）**每一步**都派发一次新的 worker
- 跨共享文件的修改（EntryAbility / main_pages.json / 公共组件）**必须单开**一次派发，不能塞进单页 / 单 slice 的 ownership 里

Stage 2/3 也必须遵守 ownership：
- prompt 必须显式给出 `output_path` 或 `allowed_write_paths`
- task agent 不得越权修改未声明文件
- 共享文件修复必须单独建 task，不能顺带“顺手改一圈”

### 4c. Base 层任务详情

| 任务 | 内容 | suggested_skills |
|------|------|-----------------|
| Base-1: Models | 所有 entity / DTO 定义 | `arkts-data-layer` |
| Base-2: Database | Schema + DAO + 迁移脚本 | `arkts-data-layer` |
| Base-3: Network | HttpClient + interceptors + API 接口 | `arkts-data-layer` |
| Base-4: Events | EventHub 常量 + pub/sub wrapper | `arkts-state-manager` |
| Base-5: Preferences | SharedPreferences → Preferences | `arkts-data-layer` |
| Base-6: 公共组件库 | Toolbar, TabBar, Card, ListItem 等 | `arkts-component-builder`, `arkts-pattern-library` |
| Base-7: 编译验证 | Base 层全量编译 | `hmos_fix_build_errors` |

**Base-6 公共组件库** 是后续 Stage 3 UI 工作的样式锚点：
- 定义统一的 Design Tokens（颜色、字号、间距、圆角等）
- 构建原子组件（Button, Badge, Divider）和复合组件（Toolbar, TabBar, Card, ListItem）
- Stage 3 的 UI 补充步骤必须引用这些组件，确保全局样式一致

### 4d. 编译检查点（per-phase）

Base 层所有任务完成后（Base-7）：

1. 调用 `hmos_fix_build_errors`（最多 20 轮自动修复）
2. 编译通过 → Stage 2 完成，进入 Stage 3
3. 编译失败 → 阻断，必须修复后才能继续（Base 层是所有 Slice 的前置依赖）

### 4e. Stage 2 完成标志

```
Stage 2 完成:
- Base 任务总数: 7
- 成功: X
- 失败: Y
- 公共组件库: Z 个组件
- 编译状态: PASS / FAIL（FAIL 则阻断）
```

---

## 5. Stage 3: Feature Slices（垂直切片）

Stage 3 读取 `feature-plan.md` 的 Slice 任务，按拓扑排序逐功能执行。每个 Slice 内部有 4 个步骤。

### 5a. 执行流程

```
读取 feature-plan.md → 提取 Slice 列表（已拓扑排序）
  │
  ▼
Slice 1 (parallel_group: 1):     Slice 2 (parallel_group: 1):
  ├─ Step 3a: UI 补充              ├─ Step 3a: UI 补充
  ├─ Step 3b: ViewModel            ├─ Step 3b: ViewModel
  ├─ Step 3c: 数据层接入            ├─ Step 3c: 数据层接入
  └─ Step 3d: 切片级验证            └─ Step 3d: 切片级验证
  │                                  │
  └──────────┬───────────────────────┘
             ▼
Slice 3 (parallel_group: 2, depends_on: [Slice 1]):
  ├─ Step 3a: UI 补充
  ├─ Step 3b: ViewModel
  ├─ Step 3c: 数据层接入
  └─ Step 3d: 切片级验证
  │
  ▼
... 直到所有 Slice 完成
```

**并行规则**：
- 同一 `parallel_group` 的 Slices 可以并行执行（各自独立走完 4 步）
- 有 `depends_on` 约束的 Slice 必须等依赖的 Slice 完成后才开始
- 每个 Slice 内部的 4 步严格串行

### 5b. Step 3a: UI 补充

检查 Stage 1 是否已转换该功能涉及的页面：

```
读取 ui-manifest.md 中目标页面的 status
  │
  ├─ status = converted → 跳过转换，直接使用已有 .ets 文件
  │
  ├─ status = pending 或页面不在 ui-plan.md 中 →
  │   ├─ 检查 ui-snapshots 数据是否存在
  │   │   ├─ 存在 → 直接调 a2h-activity-converter 转换
  │   │   └─ 不存在 → 触发 Phase A 按需模式（见 Section 6）
  │   ├─ 转换完成后更新 ui-manifest.md: status → converted
  │   └─ hmos_fix_build_errors 编译验证
  │
  └─ status = verified → 已验证，直接跳过
```

UI 补充时**必须引用 Stage 2 Base-6 公共组件库**的 Design Tokens 和共享组件，确保样式一致性。

Agent 派发（**注意 Step 3a 的路由特殊性**）：

- 如果页面状态是 `pending` 且 `ui-snapshots` 齐全 → 父 agent 直接派发 `@a2h-activity-converter`（和 Stage 1 同一模板），**不要**派发 `@a2h-migration-worker`
- 如果页面状态是 `pending` 且缺 `ui-snapshots` → 先触发 Phase A 按需模式补数据（见 Section 6），再派发 `@a2h-activity-converter`
- 如果页面状态已是 `converted` / `verified` → **不派发任何 agent**，父 agent 只输出一条 "SKIP: 页面已在 Stage 1 完成" 的说明即可

如果确实存在"UI 补充但又不属于 converter 职责"的过渡性工作（例如只是把 Design Tokens 套用回已转换的页面），可派发 `@a2h-migration-worker`：

```
@a2h-migration-worker

任务: Feature Slice [{slice_name}] Step 3a UI 补充 — Design Tokens 对齐
目标页面: {page_list}
页面 Spec: {page_spec_paths}
已有 .ets 文件: {existing_ets_files}

使用 Skill: $arkts-ui-alignment
公共组件库路径: entry/src/main/ets/components/common/
allowed_write_paths: {existing_ets_files}

验收: 页面引用公共组件库 Design Tokens，不新增 hardcode 样式，编译仍通过。
```

### 5c. Step 3b: ViewModel + 状态管理

为该功能切片生成 ViewModel，管理状态和事件绑定：

```
@a2h-migration-worker

任务: Feature Slice [{slice_name}] Step 3b — ViewModel + 状态管理
功能 Spec: {feature_spec_path}
UI Spec: {ui_spec_paths}
已有 UI 文件: {existing_ets_files}

使用 Skill: $arkts-state-manager
output_paths: [entry/src/main/ets/viewmodels/{SliceName}ViewModel.ets]
allowed_write_paths: [entry/src/main/ets/viewmodels/{SliceName}ViewModel.ets, {existing_ets_files}]

子任务:
1. 读取功能 Spec 的业务逻辑描述 + UI Spec 的状态接口
2. 创建 ViewModel class
3. 定义 @State / @Prop / @Link 状态变量
4. 实现 UI 事件处理方法
5. 将 UI 组件事件绑定到 ViewModel 方法

验收: ViewModel 编译通过（父 agent 在主工作区验证），UI 事件绑定完整。
```

### 5d. Step 3c: 数据层接入

为该功能切片创建 Repository/Service，连接数据源：

```
@a2h-migration-worker

任务: Feature Slice [{slice_name}] Step 3c — 数据层接入
功能 Spec: {feature_spec_path}
已有 Base 层: entry/src/main/ets/network/, entry/src/main/ets/database/, entry/src/main/ets/models/
已有 ViewModel: {viewmodel_path}

使用 Skill: $arkts-data-layer
output_paths: [entry/src/main/ets/repositories/{SliceName}Repository.ets]
allowed_write_paths: [entry/src/main/ets/repositories/{SliceName}Repository.ets, {viewmodel_path}]

子任务:
1. 按需创建 Repository / Service（复用 Base 层已有的公共能力）
2. 接入网络层（API 调用）或本地存储（DB / Preferences）
3. ViewModel 调用 Repository 获取数据
4. 完成完整数据流: UI ← ViewModel ← Repository ← API/DB
5. 处理数据转换和缓存策略

验收: 数据流完整闭环，父 agent 在主工作区编译通过。
```

**特殊领域追加 Skill**：当功能涉及特殊领域时，在 `arkts-data-layer` 基础上追加对应 Skill：
- 媒体播放功能 → 追加 `arkts-media-playback`
- 文件下载功能 → 追加 `arkts-download-manager`
- 系统权限功能 → 追加 `arkts-system-capabilities`

### 5e. Step 3d: 切片级验证

该 Slice 的所有步骤完成后，执行编译验证和状态更新：

```
1. 调用 hmos_fix_build_errors（最多 20 轮自动修复）
2. 基本功能检查:
   - 导航跳转：相关页面的 router.pushUrl / Navigation 是否正确
   - 数据加载：ViewModel 的 aboutToAppear 是否调用 Repository
   - 状态更新：@State 变量变化是否正确触发 UI 刷新
3. 更新 ui-manifest.md 对应页面 status: converted → verified
4. 通过 → 进入下一个 Slice
   失败 → 修复后重新验证（最多 3 轮），仍失败则标记 FAILED
```

### 5f. Stage 3 完成标志

```
Stage 3 完成:
- Slice 总数: N
- 成功: X (所有 4 步通过)
- 失败: Y
- 已验证页面: Z (status: verified)
- 编译状态: PASS / PARTIAL
```

---

## 6. Phase A 按需触发机制

当 Stage 3 Step 3a（UI 补充）发现目标页面的 ui-snapshots 数据缺失时，自动触发 a2h-spec 的 Phase A 按需模式。

### 6a. 触发条件

同时满足以下两个条件时触发：
1. `ui-manifest.md` 中目标页面的 status 不是 `converted` 或 `verified`
2. `ui-snapshots/page_NNNN/` 目录不存在或数据不完整（缺少 view.xml 或 meta.json）

### 6b. 执行流程

```
Step 3a 检查到数据缺失
  │
  ▼
调用 a2h-spec Phase A 按需模式:
  ├─ 对该单个页面执行源码分析（从 Activity 源码定位 layout XML）
  ├─ 生成最小数据集（至少包含源码 layout XML 解析结果）
  ├─ 增量更新 ui-manifest.md（新增页面条目 + confidence 标记）
  ├─ 增量生成 spec/baseline/ui/page_NNNN.md
  │
  ▼
数据准备完成 → 继续调用 a2h-activity-converter 转换该页面
  │
  ▼
继续 Slice 执行，无需中断整个 Pipeline
```

### 6c. 降级处理

如果按需模式无法为该页面生成足够数据（例如该页面是动态生成的、没有静态 layout XML）：
- 标记该页面 confidence: low
- 生成最小 UI 骨架（基于 Activity/Fragment 类名推断）
- 在 placeholder-registry.md 注册需要人工补充的占位项
- 不阻断 Slice 执行（后续步骤可以先用骨架 UI）

---

## 7. Skill 绑定机制

### 7a. 主路径：plan 的 suggested_skills

默认使用 `feature-plan.md` 中 task 标注的 `suggested_skills`。这是 a2h-plan 阶段已经根据 task 内容分配好的。

```
Task:
  suggested_skills: [arkts-data-layer]
  → agent 使用 arkts-data-layer skill
```

### 7b. 覆盖路径：runtime 上下文检查

在 agent 启动前，a2h-execute 检查当前上下文，可能覆盖 plan 的建议：

| 检查条件 | 覆盖规则 | 原因 |
|---------|---------|------|
| Stage 1 页面转换 | 使用 `a2h-activity-converter` agent | converter agent 专门为页面级 UI 转换设计 |
| Stage 3 Step 3a 页面未转换且有 Android 源码 | 先触发 Phase A 按需数据准备，再调 converter | 必须有数据才能转换 |
| 上一个编译检查点 FAILED | 暂停执行，报告错误列表 | 阻断性检查点不继续后续 task |
| task 使用了不确定的 API | 追加 `arkts-knowledge-verifier` | 防止使用错误/废弃的 API |
| task 涉及特殊领域（媒体/下载/权限） | 追加对应 Domain Skill | 默认 skill 无法覆盖特殊领域 |
| task 跨多个领域 | 组合多个 skill 按顺序执行 | 单个 skill 无法覆盖所有需求 |
| plan 中 style_set != none | 追加对应风格集的全部 style skills | 风格 skills 提供团队规范约束，agent 自动遵循 |

**风格 Skills 注入**

读取 plan Context 中的 `Style` 字段（即 `style_set` 值）：

- `style_set = none` 或字段缺失 → 不注入任何风格 skills，agent 仅使用 domain/codebase/tool skills
- `style_set != none`（例如 `wfhc-standard`）→ 执行以下逻辑：
  1. 扫描 skills 目录中 frontmatter `style-set` 值匹配的所有 SKILL.md
  2. 如果找到匹配的风格 skills → 追加到 agent 的 skills 列表
  3. 如果 style_set 值在 skills 目录中找不到对应 skills → 发出 WARN 日志，回退到 `none`（不阻断执行）

风格 skills 对 `a2h-activity-converter`（Stage 1）和 `a2h-migration-worker`（Stage 2/3）均生效。注入时追加在 suggested_skills 之后。

### 7c. 覆盖原则

**只升级不降级**：
- 可以从单 skill 升级为多 skill 组合
- 可以追加验证类 skill（knowledge-verifier）
- 不能移除 plan 中已建议的 skill（除非 skill 不存在需降级）

覆盖发生时记录原因到迁移报告的覆盖记录表。

### 7d. Skill 不存在降级

如果 plan 建议的 skill 不存在（用户可能未安装）：
1. 将 task 描述与所有可用 skill 的 `description` 字段做语义匹配
2. 优先选择带 `tags: [migration]` 的 skill
3. 如果无匹配 → agent 仅基于 prompt 中的上下文执行（无 skill 增强）

---

## 8. 编译闭环

<HARD-GATE>
三阶段每个检查点均 MUST 调用 hmos_fix_build_errors 编译验证。
编译检查失败处理规则因阶段不同而异（见下文）。
</HARD-GATE>

补充门禁：
- 编译动作必须发生在父执行器的主工作区
- Stage 1 默认先走“ownership 定位 -> 回灌原 page agent 修复”，再考虑共享修复
- 不允许用主执行器静默本地改页来替代 agent 修复

### 8a. 编译检查点分布

| 阶段 | 检查点粒度 | 失败处理 |
|------|-----------|---------|
| Stage 1 | 每 Batch 完成后 | 记录失败页面，继续下一 Batch |
| Stage 2 | Base 层全部完成后（Base-7） | **阻断**——Base 层是后续全部 Slice 的依赖 |
| Stage 3 | 每 Slice 完成后（Step 3d） | 最多 3 轮修复重试，失败标记 FAILED，继续下一 Slice |

### 8b. 编译修复流程

```
调用 hmos_fix_build_errors
  │
  ├─ 最多 20 轮自动修复循环
  │
  ├─ [可选] 本轮修复 >= 5 个错误时:
  │   ├─ 调用 a2h-retrospect --incremental
  │   ├─ 分析本轮错误模式
  │   ├─ 新模式写入 skill references
  │   └─ 后续 task 立即受益
  │
  ├─ 编译通过后检查占位符回填:
  │   ├─ 读取 spec/placeholder-registry.md
  │   ├─ 对每个 status=pending 的条目:
  │   │   ├─ 目标已实现 → 回填真实代码，status → resolved
  │   │   └─ 目标未实现 → 保持 pending
  │   └─ 回填后如有代码变更 → 重新编译验证
  │
  ├─ 编译通过 + 回填完成 → SUCCESS
  │
  └─ 20 轮仍失败 → 升级处理:
      ├─ 调用 arkts-knowledge-verifier 诊断
      │   ├─ 诊断后修复 → 编译通过 → SUCCESS
      │   └─ 仍然无法修复 → 标记 FAILED
      │
      └─ FAILED 处理按阶段规则（Section 8a）
```

### 8c. 增量学习（可选）

编译检查点完成后，如果本轮 `hmos_fix_build_errors` 修复了 >= 5 个错误：
- 调用 `a2h-retrospect --incremental`
- 分析本轮错误模式并沉淀到 skill references
- 后续 task 的 agent 读取更新后的 references，避免重复犯同样的编译错误

少于 5 个错误不触发（避免噪音）。

---

## 9. 迁移报告

所有 Stage 执行完毕后生成 `spec/migration-report.md`：

```markdown
# 迁移报告

- 执行时间: YYYY-MM-DD
- 三阶段执行: Stage 1 → Stage 2 → Stage 3

## 总览

| 阶段 | 任务数 | 成功 | 失败 | 编译状态 |
|------|--------|------|------|---------|
| Stage 1: UI Pipeline | X pages | a | a' | PASS/PARTIAL |
| Stage 2: Feature Base | 7 tasks | b | b' | PASS/FAIL |
| Stage 3: Feature Slices | N slices × 4 steps | c | c' | PASS/PARTIAL |
| **总计** | **M** | **S** | **F** | |

## Stage 1 详情: UI Pipeline

| Batch | 页面数 | 成功 | 失败 | 编译修复轮数 |
|-------|--------|------|------|------------|
| Batch 1 | 3 | 3 | 0 | 2 |
| Batch 2 | 4 | 3 | 1 | 5 |

### 页面转换清单
| 页面 | Android 来源 | 状态 | 输出文件 | Agent ID | ownership | 修复轮数 |
|------|-------------|------|---------|----------|-----------|---------|
| MainPage | MainActivity | converted | pages/MainPage.ets | 019d... | [pages/MainPage.ets] | 1 |
| HomePage | HomeFragment | converted | pages/HomePage.ets | 019d... | [pages/HomePage.ets] | 2 |

## Stage 2 详情: Feature Base

| 任务 | Skill | 状态 | 产出文件数 |
|------|-------|------|-----------|
| Base-1: Models | arkts-data-layer | SUCCESS | 5 |
| Base-2: Database | arkts-data-layer | SUCCESS | 3 |
| Base-6: 公共组件库 | component-builder | SUCCESS | 8 |

## Stage 3 详情: Feature Slices

| Slice | 功能 | Step 3a | Step 3b | Step 3c | Step 3d | 状态 |
|-------|------|---------|---------|---------|---------|------|
| Slice 1 | 播放功能 | SKIP(已转换) | SUCCESS | SUCCESS | VERIFIED | PASS |
| Slice 2 | 订阅功能 | SUCCESS | SUCCESS | SUCCESS | VERIFIED | PASS |
| Slice 3 | 搜索功能 | SUCCESS | SUCCESS | FAILED | - | FAIL |

## Skill 使用统计

| Skill | 调用次数 | 被覆盖次数 |
|-------|---------|-----------|
| a2h-activity-converter | 12 | 0 |
| arkts-data-layer | 8 | 0 |
| arkts-state-manager | 6 | 0 |
| hmos_fix_build_errors | 15 | 0 |
| arkts-knowledge-verifier | 2 | 0 (追加) |

## 覆盖记录

| Task | 阶段 | 原建议 | 实际使用 | 覆盖原因 |
|------|------|--------|---------|---------|
| Slice 3 Step 3c | Stage 3 | data-layer | data-layer + media-playback | 功能涉及音频播放 |
| Batch 1 HomePage | Stage 1 | activity-converter | activity-converter + repair loop | 主工作区编译失败回灌给原 page agent |

## 产出文件清单

| 文件路径 | 来源阶段 | 状态 |
|---------|---------|------|
| entry/src/main/ets/pages/MainPage.ets | Stage 1 | NEW |
| entry/src/main/ets/models/Episode.ets | Stage 2 | NEW |
| entry/src/main/ets/viewmodels/PlaybackViewModel.ets | Stage 3 | NEW |

## FAILED 列表

| 阶段 | Task | 失败原因 | 建议处理 |
|------|------|---------|---------|
| Stage 3 | Slice 3 Step 3c | API 不存在 | 手动排查 API 兼容性 |

## 页面状态汇总

| 状态 | 数量 |
|------|------|
| verified | X |
| converted | Y |
| pending | Z |
| FAILED | W |

## 最终编译

- 状态: SUCCESS | FAILED
- 剩余错误: (如果 FAILED)
```

---

## 10. 触发 Prompt 示例

### 完整执行

```
执行迁移
```

```
开始执行
```

```
按 plan 开始做
```

```
Plan 我看过了没问题，开始执行
```

```
做吧
```

### 严格 agent 模式

```
@a2h-execute 从 Batch 1 开始，强制使用 .codex/agents。
Stage 1 只允许 a2h-activity-converter；
每页只允许改自己的 output_file；
Batch 完成后必须在主工作区编译；
编译失败先回灌给对应 page agent 修，不要主执行器本地直改兜底。
```

完整可复制模板见：`references/new-project-prompt-templates.md`

### 部分执行

支持指定执行范围：

```
只执行 Stage 1
```

```
只执行 Stage 2 和 Stage 3
```

```
从 Stage 2 开始（Stage 1 已完成）
```

```
只执行 Slice 3
```

```
只执行 Stage 1 的 Batch 2
```

### 重试与继续

```
重试 FAILED 的 slice
```

```
继续执行（从上次中断的地方继续）
```

```
重试 Stage 1 中失败的页面
```

### 自然语言

```
开始
```

```
继续
```

自然语言触发时，a2h-execute 会列出待执行的 Stage 和任务数量，确认后开始执行。

### 部分执行的实现

当用户指定部分执行时：

| 用户指令 | 行为 |
|---------|------|
| "只执行 Stage 1" | 只读 ui-plan.md，只执行页面转换批次 |
| "只执行 Stage 2" | 只读 feature-plan.md 的 Phase 0 Base 层 |
| "只执行 Stage 3" | 只读 feature-plan.md 的 Slice 列表（前提：Stage 2 已完成） |
| "从 Stage 2 开始" | 跳过 Stage 1，从 Base 层开始执行 |
| "重试 FAILED 的 slice" | 扫描迁移报告中的 FAILED slice，重新执行其 4 步 |
| "只执行 Slice N" | 只执行指定 Slice 的 4 步（前提：其依赖已完成） |

---

## 11. 执行状态追踪

a2h-execute 在执行过程中维护以下状态：

### 11a. Task 完成标记

每个 task/step 完成后，在 `feature-plan.md` 中将 `- [ ]` 更新为 `- [x]`：

```markdown
- [x] Base-1: Models — 所有 entity / DTO 定义 ✓
- [x] Base-2: Database — Schema + DAO ✓
- [ ] Base-3: Network — HttpClient + interceptors  ← 正在执行
```

### 11b. 页面状态生命周期

`ui-manifest.md` 中每个页面的 status 字段追踪整个转换生命周期：

```
pending → converted → verified
                        ↑
                        │ (Stage 3 Step 3d 验证通过)
                        │
pending → converted ────┘
            ↑
            │ (Stage 1 batch 转换完成 / Stage 3 Step 3a 补充转换)
```

| 状态 | 含义 | 更新时机 |
|------|------|---------|
| `pending` | 初始状态，等待转换 | Spec 生成时设置 |
| `converted` | UI 转换完成，编译通过 | Stage 1 batch 编译通过后 / Stage 3 Step 3a 完成后 |
| `verified` | 功能验证通过（含 ViewModel + 数据层） | Stage 3 Step 3d 验证通过后 |

### 11c. 中断恢复

如果执行过程中断（用户取消、session 结束等），下次执行时：
1. 读取 `feature-plan.md` 中的 `[x]` / `[ ]` 标记，确定已完成和未完成的 task
2. 读取 `ui-manifest.md` 中的页面 status，确定已转换的页面
3. 先检查 `git status` 和 ownership 记录，确认是否存在 agent 误删、半写入或越权修改
4. 如果存在损坏页面：先执行应急恢复并重派发原页面 agent，不得直接跳过
5. 从第一个未完成的 task 继续执行
6. 提示用户当前进度和待执行任务数量
