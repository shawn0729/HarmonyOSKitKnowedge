---
name: a2h-plan
description: 第二步：双计划生成（UI 转换计划 + 功能执行计划）。读取 spec/baseline/ 下的 ui-manifest.md 和 feature-index.md，生成 ui-plan.md（按优先级分批的页面转换计划）和 feature-plan.md（Phase 0 Base 层 + 拓扑排序的 Feature Slices）。即使用户只说"生成计划"或"怎么做"，也应触发。
---

# a2h-plan

## 1. 定位

Pipeline 层第二步，读取已审批的 Spec 生成**双执行计划**。

本 skill 将 Spec 中的分析结果转化为两份独立但互补的 plan：**UI 转换计划**（ui-plan.md）和**功能执行计划**（feature-plan.md）。核心增值：UI 计划按优先级和 confidence 分批调度页面转换，功能计划按拓扑排序组织 Base 层水平任务 + Feature Slice 垂直切片，每个步骤标注 `suggested_skills`，让下游 a2h-execute 知道该调用哪个 Domain Skill。

```
a2h-spec（Spec 审批通过）
  │
  ▼
a2h-plan（读 Spec → 生成双计划）
  │
  ├─ ui-plan.md（UI 转换计划：按优先级分批 + 并行标注 + Agent 估算）
  └─ feature-plan.md（功能执行计划：Base 层 + Feature Slices 拓扑排序）
      │
      ▼
  a2h-execute（按双计划分阶段执行）
```

---

## 2. 输入

自动读取以下文件：

| 文件 | 用途 |
|------|------|
| `spec/baseline/ui-manifest.md` | UI 页面清单、优先级、confidence、共享组件、转换批次 |
| `spec/baseline/feature-index.md` | 功能总索引、依赖图、优先级、V1/V2 分配 |
| `spec/baseline/feature-base.md` | Base 层公共能力定义（Models, DB, Network, Events 等） |
| `spec/baseline/features/F-xxx.md` | 各功能的详细 Spec（每个功能一个文件） |
| `spec/baseline/ui/page_NNNN.md` | 各页面的详细 UI Spec（每个页面一个文件） |

如果 `spec/baseline/` 不存在或关键文件缺失，提示用户先执行 `a2h-spec`。

检查规则：
- `ui-manifest.md` + `feature-index.md` 都存在 → 可以生成双计划
- 只有 `ui-manifest.md` → 只能生成 ui-plan.md，提示功能 Spec 缺失
- 只有 `feature-index.md` → 只能生成 feature-plan.md，提示 UI Spec 缺失
- 都不存在 → 阻断，提示执行 `a2h-spec`

---

## 3. 双计划生成

### 3a. UI 转换计划（ui-plan.md）

UI 计划负责调度所有页面的 UI 转换工作，按优先级和 confidence 分批执行。

**生成步骤**：

**Step 1: 读取页面清单**

从 `spec/baseline/ui-manifest.md` 的页面清单表格中提取：
- 每个页面的 Android 源、ArkTS 目标文件、优先级（P0/P1/P2）、confidence（high/medium/low）、当前状态

**Step 2: 按优先级和 confidence 分批**

分批规则：
1. 同一优先级内，confidence: high 的页面排在前面，low 的排在后面或标记需人工补充
2. P0 → P1 → P2 顺序编排批次
3. 每批控制在 3-6 个页面，避免单批过大
4. 有依赖关系的页面必须在同一批次或依赖方在前一批次

具体排序算法：
```
1. 提取所有 P0 + confidence: high 的页面 → 形成 Batch 1
2. 提取所有 P0 + confidence: medium 的页面 → 追加到 Batch 1 或形成 Batch 2
3. 提取所有 P0 + confidence: low 的页面 → 标记 ⚠️ 需人工补充数据
4. P1 页面按相同规则排入后续 Batch
5. P2 页面排入最后的 Batch
```

**Step 3: 标注可并行的页面组**

在每批内，分析页面之间的依赖关系：
- 共享同一 Fragment 容器的页面 → 可以并行（各自独立的 NavDestination）
- 有数据依赖的页面 → 标注依赖方向，不可并行
- 完全独立的页面 → 标注"可并行"

判断依赖关系的数据来源：
- `ui-manifest.md` 的共享组件表 → 共享组件多的页面有弱依赖
- `feature-index.md` 的功能依赖图 → 功能强依赖的页面有数据依赖
- 页面级 spec `ui/page_NNNN.md` 的导航关系 → 跳转目标页面有导航依赖

**Step 4: 估算 Agent 数量**

每个页面估算所需 agent 数量：
- 简单页面（≤ 3 组件，confidence: high）→ 1 agent
- 中等页面（4-8 组件）→ 1 agent
- 复杂页面（> 8 组件或含复杂列表/自定义控件）→ 1-2 agents
- 每批的总 agent 数 = 该批所有页面 agent 数之和（可并行的页面可同时调度）

**Step 5: 编译检查点注入**

每个 Batch 完成后自动注入一个编译检查点：
- 调用 `hmos_fix_build_errors` 全量编译验证
- 确保该批所有页面编译通过后再进入下一批

---

### 3b. 功能执行计划（feature-plan.md）

功能计划负责编排从 Base 层公共能力到各功能垂直切片的完整执行计划。

**生成步骤**：

**Step 1: 读取依赖图**

从 `spec/baseline/feature-index.md` 提取：
- 所有功能 ID（F-xxx）及其优先级和 V1/V2 分配
- 功能之间的依赖关系（依赖图）
- 每个功能涉及的页面和数据层组件

从 `spec/baseline/feature-base.md` 提取：
- Base 层包含的公共能力列表（Models, DB, Network, Events, Preferences, 公共组件库）

**Step 2: 拓扑排序**

对功能依赖图执行拓扑排序，确定 Feature Slices 的执行顺序：
1. 无依赖的功能 → 可以最先执行（或并行执行）
2. 有前置依赖的功能 → 排在依赖项之后
3. 检测循环依赖 → 如存在，报告错误并建议解耦方案

**Step 3: 生成 Phase 0 Base 层任务列表**

Base 层任务是水平执行的基础设施任务，在所有 Feature Slices 之前完成：

| 任务 | 内容 | suggested_skills |
|------|------|-----------------|
| Base-1: Models | 所有 entity / DTO 定义 | `arkts-data-layer` |
| Base-2: Database | Schema + DAO + 迁移脚本 | `arkts-data-layer` |
| Base-3: Network | HttpClient + interceptors + API 接口定义 | `arkts-data-layer` |
| Base-4: Events | EventHub 常量定义 + pub/sub wrapper 封装 | `arkts-state-manager` |
| Base-5: Preferences | SharedPreferences → Preferences 迁移 | `arkts-data-layer` |
| Base-6: 公共组件库 | Toolbar, TabBar, Card, ListItem 等复用组件 | `arkts-component-builder`, `arkts-pattern-library` |
| Base-7: 编译验证 | Base 层全量编译 | `hmos_fix_build_errors` |

Base 层任务的输入来源：
- `feature-base.md` 中定义的公共能力清单
- `feature-index.md` 中被多个功能引用的共享组件/服务

**Step 4: 生成 Feature Slice 任务列表**

按拓扑排序的顺序，为每个 V1 功能生成一个 Slice。每个 Slice 包含 4 个步骤：

```
Slice N: [功能名]
  │
  ├─ Step 3a: UI 补充
  ├─ Step 3b: ViewModel + 状态管理
  ├─ Step 3c: 数据层接入
  └─ Step 3d: 切片级验证
```

各步骤详细定义见 Section 5b。

**Step 5: 标注可并行的 Slices**

根据拓扑排序结果，标注哪些 Slice 可以并行执行：
- 无依赖关系的 Slices → 可并行
- 有依赖关系的 Slices → 依赖方在前，被依赖方在后
- 并行组用 `parallel_group: N` 标注

**Step 6: 编译检查点注入**

除 Step 3d 的切片级验证外，以下位置注入额外检查点：
- 每 3 个 Slice 完成后 → 全量编译验证
- 所有 Slice 完成后 → 最终全量编译收尾

---

## 4. suggested_skills 标注规则

根据 task 内容自动标注应使用的 Domain Skill：

| Task 内容 | suggested_skills |
|-----------|-----------------|
| UI 页面转换 | `a2h-activity-converter` (agent) |
| 项目结构 / 模块配置 | `arkts-project-scaffolder` |
| 第三方库替换 | `arkts-library-migration` |
| 数据库 / DAO / Model | `arkts-data-layer` |
| 网络请求 / HTTP | `arkts-data-layer` |
| 文件操作 / 权限 | `arkts-system-capabilities` |
| 导航框架 / 路由 | `arkts-navigation-builder` |
| 状态管理 / 数据绑定 | `arkts-state-manager` |
| 页面组件 / 列表 | `arkts-component-builder` |
| 音频播放 / AVPlayer | `arkts-media-playback` |
| 大文件下载 | `arkts-download-manager` |
| 动画 / 转场 | `arkts-animation-builder` |
| 编译修复 | `hmos_fix_build_errors` |
| API 验证 | `arkts-knowledge-verifier` |
| App 身份配置 | `arkts-app-identity` |
| 资源转换 | `android2hmos_resources_convert` |
| 公共组件库 | `arkts-component-builder`, `arkts-pattern-library` |

### Feature Slice 步骤的默认 suggested_skills

| Step | suggested_skills |
|------|-----------------|
| Step 3a: UI 补充 | `a2h-activity-converter` |
| Step 3b: ViewModel + 状态管理 | `arkts-state-manager` |
| Step 3c: 数据层接入 | `arkts-data-layer` |
| Step 3d: 切片级验证 | `hmos_fix_build_errors` |

一个 task 可以标注多个 skill（按执行顺序排列）。当功能涉及特殊领域时，在默认基础上追加对应 skill（例如媒体播放功能的 Step 3c 追加 `arkts-media-playback`）。

### 风格 Skills 追加

读取 spec 文档中的 `style_set` 字段（缺失时视为 `none`）：

- `style_set = none` → 不追加任何风格 skills，suggested_skills 保持原样
- `style_set != none`（例如 `wfhc-standard`）→ 根据 task 内容，从对应风格集中选取相关 skills 追加到 suggested_skills：

| Task 内容 | 追加的风格 Skill |
|-----------|-----------------|
| UI 页面 / 组件 | 对应 style-set 中 domain=ui 的风格 skill |
| 状态管理 / ViewModel | 对应 style-set 中 domain=state 的风格 skill |
| 导航 / 路由 | 对应 style-set 中 domain=navigation 的风格 skill |
| 网络请求 | 对应 style-set 中 domain=data 的风格 skill |
| 项目结构 / 配置 | 对应 style-set 中 domain=engineering 的风格 skill |
| 特殊领域（扫描等） | 对应 style-set 中 domain=system 的风格 skill |

选取依据：扫描 skills 目录中 frontmatter `style-set` 值匹配的条目，根据 `domain` 字段与 task 领域匹配。一个 task 可追加多个风格 skill。

风格 skills 追加在 domain skills 之后，确保风格规则叠加（而非覆盖）基线。

---

## 5. Plan 格式

### 5a. UI 转换计划格式（ui-plan.md）

```markdown
# UI Conversion Plan

## Context
- Source: spec/baseline/ui-manifest.md
- Style: <style_set 值，none 或具体风格名>
- Total pages: <总页面数>
- Batches: <批次数>
- Estimated total agents: <预计 agent 总数>

## Batch 1: P0 Core Pages (confidence: high)
| 序号 | 页面 | Android 来源 | confidence | 可并行 | 预计 agent |
|------|------|-------------|-----------|--------|-----------|
| 0001 | MainPage | MainActivity | high | - | 1 |
| 0002 | HomePage | HomeFragment | high | 与 0003 并行 | 1 |
| 0003 | QueuePage | QueueFragment | high | 与 0002 并行 | 1 |

编译检查点: Batch 1 完成后

## Batch 2: P0 Player + Subscription (confidence: high/medium)
| 序号 | 页面 | Android 来源 | confidence | 可并行 | 预计 agent |
|------|------|-------------|-----------|--------|-----------|
| 0004 | PlayerPage | PlayerActivity | high | - | 2 |
| 0005 | SubscriptionPage | SubscriptionFragment | medium | 与 0006 并行 | 1 |
| 0006 | SearchPage | SearchFragment | medium | 与 0005 并行 | 1 |

编译检查点: Batch 2 完成后

## Batch 3: P1 Secondary (confidence: mixed)
...

## Batch N: P2 Low Priority
| 序号 | 页面 | Android 来源 | confidence | 可并行 | 预计 agent |
|------|------|-------------|-----------|--------|-----------|
| 00XX | AboutPage | AboutActivity | low ⚠️ | - | 1 |

⚠️ confidence: low 页面需人工补充 UIAutomator dump 数据

编译检查点: Batch N 完成后（最终全量编译）

## Summary
- P0 pages: X (Batch 1-2)
- P1 pages: Y (Batch 3-4)
- P2 pages: Z (Batch 5+)
- ⚠️ Low confidence: W pages (需人工补充数据)
```

### 5b. 功能执行计划格式（feature-plan.md）

```markdown
# Feature Execution Plan

## Context
- Source: spec/baseline/feature-index.md, spec/baseline/feature-base.md
- Style: <style_set 值，none 或具体风格名>
- Total features (V1): <V1 功能总数>
- Total slices: <Slice 总数>
- Base tasks: <Base 层任务数>
- Estimated phases: Phase 0 (Base) + <N> Slices

## Dependency Graph
<来自 feature-index.md 的功能依赖关系简要可视化>

## Phase 0: Base 层（水平执行）

所有 Feature Slices 共用的基础设施，必须先完成。

- [ ] Base-1: Models — 所有 entity / DTO 定义
  - suggested_skills: [arkts-data-layer]
  - input: feature-base.md Models 段
  - output: entry/src/main/ets/models/*.ets
  - details:
    - 从 Android 源码的 entity/model 类提取字段和关系
    - 按 ArkTS 最佳实践定义 class/interface
    - 包含序列化/反序列化方法

- [ ] Base-2: Database — Schema + DAO
  - suggested_skills: [arkts-data-layer]
  - input: feature-base.md Database 段
  - output: entry/src/main/ets/database/*.ets
  - details:
    - 迁移 Room/SQLite → RDB（关系型数据库）
    - 定义表结构 + DAO 接口
    - 包含数据迁移脚本（如需）

- [ ] Base-3: Network — HttpClient + interceptors
  - suggested_skills: [arkts-data-layer]
  - input: feature-base.md Network 段
  - output: entry/src/main/ets/network/*.ets
  - details:
    - 迁移 Retrofit/OkHttp → @ohos/net.http 或三方 HTTP 库
    - 实现请求拦截器（Token 注入、日志等）
    - 定义 API 接口常量

- [ ] Base-4: Events — EventHub 常量 + pub/sub wrapper
  - suggested_skills: [arkts-state-manager]
  - input: feature-base.md Events 段
  - output: entry/src/main/ets/events/*.ets
  - details:
    - 迁移 EventBus/LiveData → Emitter 或 EventHub
    - 定义事件常量枚举
    - 封装 pub/sub 工具类

- [ ] Base-5: Preferences — SharedPreferences 迁移
  - suggested_skills: [arkts-data-layer]
  - input: feature-base.md Preferences 段
  - output: entry/src/main/ets/preferences/*.ets
  - details:
    - 迁移 SharedPreferences → @ohos.data.preferences
    - 封装异步读写工具类
    - 定义 Key 常量

- [ ] Base-6: 公共组件库
  - suggested_skills: [arkts-component-builder, arkts-pattern-library]
  - input: ui-manifest.md 共享组件表 + feature-base.md 公共组件段
  - output: entry/src/main/ets/components/common/*.ets
  - details:
    - Toolbar / TabBar / NavBar
    - Card / ListItem / Badge
    - Loading / Empty / Error 状态组件
    - 其他被多个页面引用的共享组件

- [ ] Base-7: 编译验证 — Base 层全量编译
  - suggested_skills: [hmos_fix_build_errors]
  - blocking: true
  - details:
    - 调用 hmos_fix_build_errors 全量编译
    - 验证所有 Base 层产出编译通过
    - 检查 spec/placeholder-registry.md 中可回填的占位符

---

## Slice 1: [功能名] (priority: P0, parallel_group: 1)
depends_on: [Base]

- [ ] Step 3a: UI 补充 — [功能涉及的页面列表]
  - suggested_skills: [a2h-activity-converter]
  - input: ui-manifest.md 对应页面条目
  - details:
    - 检查目标页面在 ui-plan.md 中的 status
    - 如果 status = converted → 跳过，直接使用已转换产出
    - 如果 status = pending → 触发按需数据准备 + 页面转换
    - 如果 status = skipped → 标记为本 Slice 需要的最小 UI 骨架
  - output: 对应页面的 ArkTS 组件文件
  - acceptance:
    - 页面编译通过
    - 所有用户可见文本使用 $r() 引用

- [ ] Step 3b: ViewModel + 状态管理 — [功能名]ViewModel
  - suggested_skills: [arkts-state-manager]
  - input: features/F-xxx.md 状态定义段
  - details:
    - 创建 ViewModel class
    - 定义 @State / @Prop / @Link 状态变量
    - 实现 UI 事件处理方法
    - 绑定 UI 组件事件到 ViewModel 方法
  - output: entry/src/main/ets/viewmodels/[功能名]ViewModel.ets
  - acceptance:
    - ViewModel 编译通过
    - UI 事件绑定完整

- [ ] Step 3c: 数据层接入 — [功能名] Repository/Service
  - suggested_skills: [arkts-data-layer]
  - input: features/F-xxx.md 数据层接口段
  - details:
    - 创建 Repository / Service（如需，复用 Base 层已有的）
    - 连接到 Network 层（API 调用）或 Local Storage（DB/Preferences）
    - 完成数据流: UI ← ViewModel ← Repository ← API/DB
    - 处理数据转换和缓存策略
  - output: entry/src/main/ets/repositories/[功能名]Repository.ets（如需）
  - acceptance:
    - 数据流完整闭环
    - 编译通过

- [ ] Step 3d: 切片级验证 — [功能名]
  - suggested_skills: [hmos_fix_build_errors]
  - blocking: true
  - details:
    - 调用 hmos_fix_build_errors 编译验证
    - 基本功能检查（数据能否加载、UI 能否渲染）
    - 更新 ui-manifest.md 对应页面 status: converted → verified
  - acceptance:
    - 编译通过（BUILD SUCCESSFUL）
    - 所有涉及页面 status 更新为 verified

## Slice 2: [功能名] (priority: P0, parallel_group: 1)
depends_on: [Base]
<与 Slice 1 相同的 4 步结构，parallel_group 相同表示可与 Slice 1 并行>

## Slice 3: [功能名] (priority: P0, parallel_group: 2)
depends_on: [Slice 1]
<有依赖关系，必须在 Slice 1 之后执行>

...

## Slice N: [功能名] (priority: P1)
depends_on: [Slice X, Slice Y]
<最后的 Slice>

---

## Final Verification
- [ ] 全量编译检查
  - suggested_skills: [hmos_fix_build_errors]
  - blocking: true
  - details: 所有 Slice 完成后的最终全量编译

## Summary
- Phase 0 (Base): 7 tasks
- Feature Slices: N slices (M parallel groups)
- Total steps: 7 + N * 4 + 1
- Parallelizable: X slices can run in parallel
```

---

## 6. 存储

所有 plan 存储在 `spec/baseline/plans/` 目录下：

```
spec/baseline/plans/
├── ui-plan.md
├── feature-plan.md
└── coverage-matrix.md
```

固定两个 plan 文件 + 一个覆盖率校验文件。不再按数量拆分多个 plan 文件。

---

## 7. 覆盖率校验（Plan 生成后自动执行）

Plan 生成完毕后，必须执行覆盖率校验，确保所有 V1 功能都被 plan 覆盖。

校验算法：
1. 从 `feature-index.md` 提取所有功能 ID（F-xxx）及其优先级和 V1/V2 分配
2. 从 `feature-plan.md` 所有 Slice 的功能 ID 收集已覆盖集合
3. 从 `ui-plan.md` 所有 Batch 的页面收集已覆盖的 UI 页面集合
4. 交叉比对 `ui-manifest.md` 的页面清单，确认无遗漏
5. 计算覆盖率

校验规则：
- P0 (V1) 功能覆盖率 = 100%：不满足则阻断 plan 输出，自动补充缺失的 Slice
- P1 (V1) 功能覆盖率 >= 80%：不满足则警告，列出缺失项
- P2 / V2 / Skip：允许 GAP，仅记录
- UI 页面覆盖率：ui-plan.md 中的页面集合必须 >= ui-manifest.md 中所有非 skipped 页面

输出文件：`spec/baseline/plans/coverage-matrix.md`

```markdown
# Coverage Matrix

## Summary
- Feature 覆盖率:
  - P0 (V1): X/Y (Z%) — 必须 100%
  - P1 (V1): X/Y (Z%) — 建议 >= 80%
  - P2 / V2 / Skip: X 个 GAP（允许）
- UI 页面覆盖率: X/Y (Z%)

## Feature Gaps
| F-ID | 功能名 | 优先级 | 版本 | 状态 |
|------|--------|--------|------|------|
| F-xxx | ... | P1 | V1 | MISSING |

## UI Page Gaps
| 序号 | 页面 | 优先级 | 状态 |
|------|------|--------|------|
| 00XX | XxxPage | P1 | MISSING |

## Deferred
| F-ID | 功能名 | 优先级 | 版本 | 原因 |
|------|--------|--------|------|------|
| F-xxx | ... | P2 | V2 | 延期到 V2 |

## Full Feature Matrix
| F-ID | 功能名 | 优先级 | 版本 | 覆盖 Slice | 状态 |
|------|--------|--------|------|-----------|------|
| F-xxx | ... | P0 | V1 | Slice 1 | COVERED |

## Full UI Page Matrix
| 序号 | 页面 | 优先级 | confidence | 覆盖 Batch | 状态 |
|------|------|--------|-----------|-----------|------|
| 0001 | MainPage | P0 | high | Batch 1 | COVERED |
```

---

## 8. 门控

双计划生成后需要**人工审批**：

```
## 双计划生成完成

### UI 转换计划 (ui-plan.md)
- 总页面: X 个
- 批次: Y 个 Batch
- 预计 agent: Z 个
- ⚠️ Low confidence 页面: W 个

### 功能执行计划 (feature-plan.md)
- Base 层任务: 7 个
- Feature Slices: N 个
- 可并行组: M 组
- 总步骤: K 步

### 覆盖率
- P0 (V1) 功能: 100% ✓
- P1 (V1) 功能: XX%
- UI 页面: XX%

请审阅 spec/baseline/plans/，确认后执行 a2h-execute。

可调整项:
- 调整 Batch 分组或页面排序
- 调整 Slice 执行顺序或并行组
- 修改 suggested_skills
- 增删 Slice 或 Base 任务
- 移动页面到不同 Batch
```

用户可以：
- 直接确认 → 进入 a2h-execute
- 修改后确认 → 进入 a2h-execute
- 要求重新生成 → a2h-plan 重新执行

---

## 9. 触发 Prompt 示例

```
生成执行计划
```

```
怎么做这个迁移
```

```
为 spec 生成 plan
```

```
拆分迁移任务
```

```
Spec 我看过了没问题，下一步怎么做
```

```
生成 UI 计划和功能计划
```

自然语言触发时，a2h-plan 会先检查 `spec/baseline/` 是否存在且已审批。如果 Spec 不存在，提示用户先执行 `a2h-spec`。
