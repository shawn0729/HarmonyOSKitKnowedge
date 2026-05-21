---
name: arkts-spec-evolver
description: 增量 Spec 演进管理。当用户需要补全功能、修复 Bug、性能优化、审计 spec 与代码差距、或任何 "spec 先行" 的变更时触发。即使用户只说"这个功能缺失"或"这个有 bug"或"检查下还缺什么"，也应触发。
---

# arkts-spec-evolver

## 定位

Post-V1 增量 spec 演进管理 skill。在 `a2h-spec` 完成初始 baseline（ui-manifest + feature-index/base/features）生成后接管，负责后续所有变更的 spec 管理与执行编排。

**核心原则**：强制 "spec 先行" 纪律——**任何代码变更必须先有 spec，spec 是唯一变更驱动源**。

### 适用场景

- **功能补全**：baseline 遗漏的功能需要补录并实现
- **Bug 修复**：开发/测试中发现的问题需要先记录为 spec 再修复
- **优化迭代**：V1 交付后的性能优化、UI 对齐、V2 增强
- **差距审计**：定期检查 spec 与代码的差距，发现遗漏

### 在整体工作流中的位置

```
a2h-spec（Phase A/B/C）→ a2h-plan → a2h-execute（3 Stage 引擎）→ a2h-verify → a2h-retrospect
    │
    ▼
交付 V1 → baseline 固化（ui-manifest + feature-index + features/ 移入 baseline/）
    │
    ▼
后续迭代（spec-evolver 接管）
    ├─ 用户/测试发现问题 → create + execute
    ├─ 定期审计 → audit → 批量 create → 逐个 execute
    └─ V2 规划 → 多个 create → 逐个 execute
```

---

## 七种工作模式

| 模式 | 触发 | 说明 |
|------|------|------|
| `create` | "XX功能缺失，生成spec" | 创建增量 spec，不执行 |
| `plan` | "为 F-xxx 生成实现计划" | 为已有增量 spec 生成实现计划 |
| `execute` | "执行 spec/features/...-F031-...md" | 按计划执行代码变更 |
| `create+plan+execute+verify` | "XX功能缺失，生成spec并实现" | 全流程（含两道门禁，见下方） |
| `verify` | "验证 F-xxx 的实现" | 按验收标准验证已完成的变更 |
| `audit` | "检查spec还缺什么" | 审计 baseline 与代码差距，批量生成增量 spec |
| `status` | "查看所有增量spec状态" | 列出所有增量 spec 的状态 |

### 全流程执行逻辑

<HARD-GATE>
全流程模式自动推进各阶段，但必须在以下两个节点暂停等待用户确认：

```
create（生成 spec）
    │
    ▼
★ Gate 1: 输出 spec 摘要，等待用户确认
    │ 用户确认
    ▼
plan（生成实现计划）
    │
    ▼
★ Gate 2: 输出 plan 摘要，等待用户确认
    │ 用户确认
    ▼
execute（执行代码变更）
    │
    ▼
verify（验证）
```

用户在任一门禁处可以：
- 确认 → 自动进入下一阶段
- 要求修改 → 修改后重新等待确认
- 终止 → 停止流程，保留已生成的 spec/plan

绝对禁止在用户确认前进入下一阶段。
</HARD-GATE>

---

## 完整工作流程（对齐 Pipeline 五步流水线）

```
                Pipeline 流程对照
                ━━━━━━━━━━━━━━━━━━
用户输入        Pipeline             spec-evolver
变更需求        ↓                    ↓
    │           a2h-spec        →    Step 1-5: create 增量 spec
    │           ↓                    ↓
    │           a2h-plan        →    Step 6-7: plan 实现计划
    │           ↓                    ↓
    │           a2h-execute     →    Step 8-9: execute 代码变更
    │           ↓                    ↓
    │           a2h-verify      →    Step 10-11: verify 验证
    ▼           ↓                    ↓
完成            a2h-retrospect       done
```

### Create 阶段（Step 1-5）

**Step 1: 读取上下文**
- 读 `spec/spec-index.md`（baseline + 已有增量）
- 读 baseline 中受影响的层（按需）
- 读已有增量（避免重复创建）

**Step 2: 分类 + 编号**
- 自动判断 `type`: feature / bugfix / optimization
- 从 spec-index.md "当前状态摘要" 读取下一编号，分配: F-xxx / BF-xxx / OPT-xxx
- 分析 `affects`: 哪些 baseline 层/section

**Step 3: 生成增量 spec**
- 按模板（`templates/increment-spec-template.md`）写入对应目录
  - feature → `spec/features/YYYY-MM-DD-Fxxx-description.md`
  - bugfix → `spec/bugfixes/YYYY-MM-DD-BFxxx-description.md`
  - optimization → `spec/optimizations/YYYY-MM-DD-OPTxxx-description.md`
- **status: pending**
- bugfix 类型额外包含 "复现步骤" 和 "根因分析" 两节

**Step 4: 更新 spec-index.md**
- 在对应类型表（Features / Bugfixes / Optimizations）中新增一行
- 更新 "当前状态摘要" 中的计数和下一编号

**Step 5: 用户确认 spec（★ Gate 1）**
- 输出: "增量 spec 已生成，请审阅。"
- 等待用户确认后才进入 Plan 阶段
- 如果是全流程模式（create+plan+execute+verify），用户确认后自动进入 Plan 阶段

<HARD-GATE>
无论何种模式，Step 5 必须等待用户明确确认。绝对禁止自动跳过此步骤。
</HARD-GATE>

### Plan 阶段（Step 6-7）

**Step 6: 生成实现计划**
- 分析增量 spec 的 `affects` 和 "实现指引"
- 生成 plan 文件: `spec/<type>/plans/YYYY-MM-DD-<id>-plan.md`
- plan 内容包含:
  - 影响的文件清单（创建/修改/测试）
  - 按依赖顺序拆解的 task 列表
  - 每个 task 的具体步骤
  - 调用哪些下游 skill
- 简单 bugfix 可生成简化 plan（单 task，见"简化流程"）
- 更新增量 spec 的 "实现计划" 区域，记录 plan 文件路径和 task 数量

**Step 7: 用户确认 plan（★ Gate 2）**
- 输出: "实现计划已生成，请审阅。"
- 等待用户确认后才进入 Execute 阶段

<HARD-GATE>
无论何种模式，Step 7 必须等待用户明确确认。绝对禁止自动跳过此步骤。
</HARD-GATE>

### Execute 阶段（Step 8-9）

<HARD-GATE>
Execute 前置检查：
1. 读取增量 spec 文件的 status 字段
2. status 必须为 planned
3. status 为 pending → 拒绝执行，提示 "spec 尚未确认，请先审阅并确认"
4. spec 文件不存在 → 拒绝执行，提示 "请先通过 create 模式生成 spec"
不存在已审批 spec 的情况下，绝对禁止生成任何实现代码。
</HARD-GATE>

**Step 8: 执行代码变更**
- spec status: **planned → in_progress**
- 按 plan 的 task 列表逐个执行:
  - 每个 task 调用对应下游 skill（见"Skill 调度顺序"）
  - feature → component-builder / data-layer / ...
  - bugfix → knowledge-verifier 诊断 → 对应 skill
  - optimization → ui-alignment / component-builder
- 每个 task 完成后标记 plan 中的 checkbox

**Step 9: 回填执行记录**
- 在增量 spec 的 "执行记录" 中填充:
  - 执行时间
  - 触发 skill
  - 修改文件列表
  - commit hash
- plan 文件中所有 task 标记完成

### Verify 阶段（Step 10-11）

**Step 10: 验证**
- spec status: **in_progress → verifying**
- 编译验证: hmos_fix_build_errors 自动编译修复（最多 20 轮，替代手动 hvigor build）
- 验收验证: 按增量 spec 的 "验收标准" 逐项检查
- 回归验证: 确认未破坏已有功能（grep 静态检查）
- 验证结果记录到增量 spec 的 "验证记录" 区域

**Step 11: 完成或回退**
- 验证通过:
  - spec status: **verifying → done**
  - 更新 spec-index.md 状态为 done
  - 更新摘要计数
- 验证失败:
  - 执行回退处理（见"回退处理"）
  - spec status: **verifying → failed → pending**（回归失败时）

---

## 简化流程（适用于简单 bugfix）

```
复杂度判断:
  影响 ≤2 个文件 + 单一 section → 简化流程
  影响 >2 个文件 或 多层 → 完整流程
```

<HARD-GATE>
简化流程仅简化 plan 的存储形式（嵌入 spec 而非独立文件），
两道门禁同样不可跳过。
</HARD-GATE>

简化流程步骤：
```
create → ★ Gate 1（用户确认 spec）→
plan（嵌入 spec 的"实现计划"区域）→ ★ Gate 2（用户确认 plan）→
execute → verify
```

状态流转完整保留：pending → planned → in_progress → verifying → done

简化的是 plan 文件形式（嵌入 spec 而非独立文件），不是流程步骤。

---

## 回退处理

验证失败时，按失败类型分别处理:

### 编译失败
- `hmos_fix_build_errors` 自动修复（最多 20 轮）
- 20 轮后仍失败 → `knowledge-verifier` 介入诊断
- 修复后重新 verify
- **不回退代码**（修复前进策略）

### 验收失败
- 分析失败原因
- 若实现方案有误 → 调整 plan，重新 execute 失败的 task
- 若 spec 本身有误 → 更新增量 spec，重新 plan + execute

### 回归失败（破坏已有功能）
- 记录回退路径: `git revert <commit>`
- spec status: **verifying → failed → pending**（回退到待确认状态）
- 在增量 spec 中追加 "回退记录" 和原因分析
- 重新 plan（需考虑兼容性约束）

---

## audit 模式

audit 模式用于审计 baseline spec 与实际代码的差距。**仅检测结构性地标**，不做语义级功能检测，避免过多误报。

### 检测范围

| 检测对象 | 扫描方式 |
|---------|---------|
| @Entry Page | `grep "@Entry" pages/*.ets` |
| @Component | `ls components/*.ets` 与 ui-manifest.md 页面清单对比 |
| DAO 类 | `ls database/*Dao.ets` 与 feature-base.md 数据模型对比 |
| 数据表 | `grep "CREATE TABLE" database/*.ets` 与 feature-base.md 数据模型对比 |

**不检测**：工具函数、内部重构、UI 微调等非结构性变更。

### audit 流程

```
1. 读 baseline feature-index.md（功能清单）+ ui-manifest.md（页面清单）+ feature-base.md（数据模型）
2. 扫描 ArkTS 代码中的结构性地标:
   - @Entry Page（pages/*.ets）
   - @Component（components/*.ets）
   - DAO 类（database/*Dao.ets）
   - 数据表（grep CREATE TABLE）
3. 对比:
   - spec 有但代码无 → feature 增量（待实现）
   - 代码有但 spec 无（限结构性地标）→ feature 增量（补录）
   - spec 有 + 代码有但行为不一致 → bugfix 增量
4. 批量生成增量 spec
5. 更新 spec-index.md
6. 输出审计报告
```

#### audit 模式增强: 覆盖率驱动的 GAP 检测 [新增]

当 `spec/baseline/plans/coverage-matrix.md` 存在时，audit 模式额外执行：

1. 读取 coverage-matrix.md 的 Gaps 表和 Full Matrix
2. 对每个 GAP（未被任何 task 覆盖的 Feature ID）:
   - 读取 feature-index.md 中该功能的描述和子功能列表
   - 检查代码中是否有非计划内的实现（grep 关键词）
   - 如果代码中无实现 → 生成 increment spec (type: feature, status: pending)
   - 如果代码中有部分实现 → 生成 increment spec (type: optimization, status: pending)
3. 对每个 COVERED 但实际未实现的项（结合 CHECK-7 结果）:
   - 生成 increment spec (type: bugfix, status: pending)
4. 输出: 一组 increment spec 文件（spec/features/ 或 spec/optimizations/ 或 spec/bugfixes/）

这样 audit 模式不仅能检测"代码中有但 spec 中没有"的情况（当前能力），还能检测"spec 中有但代码中没有"的情况（新增能力）。

**前置条件**: 如果 coverage-matrix.md 不存在，跳过此增强部分，仅执行原有的结构扫描。

---

## 增量 spec 文件格式

增量 spec 文件使用模板 `templates/increment-spec-template.md` 生成。

### frontmatter 字段

```yaml
---
id: F-xxx                           # 唯一编号
type: feature                       # feature | bugfix | optimization
title: 播放速度控制                   # 简短标题
priority: P0                        # P0/P1/P2
status: pending                     # pending | planned | in_progress | verifying | done | failed | deprecated
created: YYYY-MM-DD                 # 创建日期
source: issue #45                   # 来源（issue/用户反馈/测试发现/审计发现）
affects:                            # 影响哪些 baseline 文件
  - feature-index: F001
  - feature-base: database
  - ui: page_0001
# deprecated_by:                    # 被哪个增量替代（废弃时填写）
# deprecated_reason:                # 废弃原因（废弃时填写）
---
```

### 正文区域

- **背景** — 为什么需要这个变更
- **复现步骤** — bugfix 类型专用
- **根因分析** — bugfix 类型专用
- **变更描述** — 对 feature-index/feature-base/features/ui 的影响
- **实现指引** — 具体实现方案、注意事项、参考踩坑
- **验收标准** — 可检查的验收条件列表
- **实现计划** — plan 阶段自动生成
- **执行记录** — execute 阶段自动填充
- **验证记录** — verify 阶段自动填充
- **回退记录** — 仅在验证失败回退时填充

---

## 命名约定

| 类型 | 前缀 | 编号规则 | 示例 |
|------|------|---------|------|
| 功能补全/新功能 | F | 延续 baseline feature-index.md 的 F-xxx 编号 | `YYYY-MM-DD-Fxxx-description.md` |
| Bug 修复 | BF | 独立编号 | `YYYY-MM-DD-BFxxx-description.md` |
| 优化 | OPT | 独立编号 | `YYYY-MM-DD-OPTxxx-description.md` |

Plan 文件命名与增量 spec 对应:
- `spec/features/plans/YYYY-MM-DD-Fxxx-plan.md`
- `spec/bugfixes/plans/YYYY-MM-DD-BFxxx-plan.md`
- `spec/optimizations/plans/YYYY-MM-DD-OPTxxx-plan.md`

---

## 状态生命周期

增量 spec 的 `status` 字段支持 7 种状态:

| 状态 | 含义 | 对应阶段 |
|------|------|---------|
| `pending` | 已创建 spec，待确认 | create 完成 |
| `planned` | 实现计划已生成，待确认 | plan 完成 |
| `in_progress` | 正在执行代码变更 | execute 中 |
| `verifying` | 代码变更完成，验证中 | verify 中 |
| `done` | 验证通过，全部完成 | verify 通过 |
| `failed` | 验证失败，需回退/重做 | verify 失败 |
| `deprecated` | 已废弃，不再有效 | 任意阶段可标记 |

### 状态流转图

```
pending → planned → in_progress → verifying → done
                                      │
                                      └→ failed → pending（回退重做）
任意状态 → deprecated（废弃）
```

### 废弃处理

废弃时在 frontmatter 中增加 `deprecated_by` 和/或 `deprecated_reason`:

```yaml
status: deprecated
deprecated_reason: "被 BF-005 替代，提供了更好的修复方案"
deprecated_by: BF-005
```

---

## 有效状态合成

baseline 不可变 + 增量独立存在，意味着 "当前状态" 需要合成。

### 合成规则

增量 spec 对 baseline 是**严格追加**语义:

| 操作 | 语义 | 示例 |
|------|------|------|
| 新增行 | 在 baseline 表中追加新行 | D4 新增 F-xxx |
| 修正行 | 标注 baseline 中某行的修正值 | SS6 中 F-005 从 V2 改为 V1 |
| 删除行 | 标注 baseline 中某行已废弃 | F-014 标记 `deprecated` |

### 多个增量影响同一 section 时

按时间顺序（创建日期）依次叠加。后创建的增量覆盖先创建的（同一字段时）。

### 读取 "当前状态" 的标准流程（5 步）

```
1. 读 spec-index.md
2. 读 baseline 对应 section
3. 扫描增量表中 status=done 且 affects 包含该 section 的增量
4. 按创建日期排序，依次叠加
5. 得到有效状态
```

---

## Skill 调度顺序

post-V1 增量执行不走完整 3 Stage 流程（UI Pipeline → Feature Base → Feature Slices），而是按影响层精简调度:

```
增量 spec affects 分析
    │
    ├─ 仅影响 feature-index 元数据 → 不改代码，仅更新 spec
    │
    ├─ 影响 feature-base (数据模型) → arkts-data-layer 优先
    │   └─ 若同时影响 ui pages → 再调 arkts-component-builder
    │
    ├─ 影响 ui-manifest / ui pages → arkts-navigation-builder
    │   └─ 若同时影响 ui pages → 再调 arkts-component-builder
    │
    ├─ 仅影响 ui page specs → arkts-component-builder / arkts-ui-alignment
    │
    └─ 影响多层 → 按依赖顺序:
        arkts-data-layer → arkts-navigation-builder → arkts-state-manager → arkts-component-builder
```

### spec-evolver 与下游 skill 的关系

spec-evolver 是**编排层**，不替代任何现有 skill:

```
spec-evolver (编排)
    ├─ feature → 按影响层选择:
    │   ├─ affects feature-base → arkts-data-layer
    │   ├─ affects ui pages → arkts-navigation-builder
    │   ├─ affects ui pages → arkts-component-builder / arkts-ui-alignment
    │   ├─ affects WebView → arkts-webview-manager
    │   └─ affects 多层 → 按依赖顺序依次调用
    ├─ bugfix →
    │   ├─ 先 arkts-knowledge-verifier 诊断
    │   └─ 再调用对应 skill 修复
    └─ optimization →
        ├─ 性能 → arkts-component-builder
        ├─ UI 对齐 → arkts-ui-alignment
        └─ 动画 → arkts-animation-builder
```

---

## 触发 Prompt 示例

| 场景 | Prompt | 模式 |
|------|--------|------|
| 全流程 | `播放速度控制功能缺失，生成 spec 并实现` | create+plan+execute+verify |
| 只生成 spec | `播放速度控制功能缺失，只生成 spec` | create |
| 为已有 spec 生成计划 | `为 F-xxx 生成实现计划` | plan |
| 执行已有计划 | `执行 spec/features/...-F031-...md` | execute |
| 验证已完成的变更 | `验证 F-xxx 的实现` | verify |
| 修复 bug 全流程 | `AVPlayer seek 到末尾会崩溃，修复` | create+plan+execute+verify |
| 优化全流程 | `列表滚动卡顿，优化` | create+plan+execute+verify |
| 审计 | `检查下 spec 和代码的差距` | audit |
| 查看状态 | `查看所有增量 spec 的状态` | status |

---

## a2h-spec vs spec-evolver

| 职责 | a2h-spec | spec-evolver |
|------|----------|-------------|
| 何时用 | 初始迁移（0→1），Phase A/B/C 三阶段 | V1 交付后，持续迭代（1→N） |
| 输入 | Android 源码 + ref + ui-snapshots | 用户描述的变更需求 |
| 输出 | baseline（ui-manifest + feature-index/base/features） | 增量 spec 文件 |
| 修改 baseline | 生成 baseline | 不修改 baseline（只读） |
| 驱动代码 | 不驱动（只产 spec） | 驱动（spec → plan → code → verify 闭环） |
| 目录 | `spec/baseline/` | `spec/features/` `spec/bugfixes/` `spec/optimizations/` |
| 调用频次 | 项目初始一次 | 持续迭代多次 |
| 路由关系 | baseline 已存在时自动委托 spec-evolver | 被 a2h-spec 透传调用 |

### baseline 冻结约束

一旦 baseline 固化，**a2h-spec 不得在同一项目上重新运行**生成新的 baseline（否则 F-xxx 编号冲突）。a2h-spec 检测到 `spec/baseline/` 已存在时，自动委托 spec-evolver 处理。如需纳入新的 Android 功能，使用 spec-evolver create 模式生成增量 spec。

---

## Spec 目录结构

```
spec/
├── spec-config.yaml              ← 层定义 + ref 扫描规则（不变）
├── spec-index.md                 ← 主索引（baseline + 增量串联视图）
├── baseline/                     ← 初始生成的 spec（只读基准）
│   ├── ui-manifest.md            ← 页面清单 + 全局约定
│   ├── ui/                       ← 分页 UI spec
│   │   └── page_NNNN.md
│   ├── ui-snapshots/             ← 三源数据
│   ├── feature-index.md          ← 功能清单 + 依赖图
│   ├── feature-base.md           ← 共享基础设施
│   ├── features/                 ← 按功能分 spec
│   │   └── F00x.md
│   └── plans/
│       ├── ui-plan.md
│       ├── feature-plan.md
│       └── coverage-matrix.md
├── ref/                          ← 只读输入源（不变）
│   ├── *_design.md
│   ├── *_spec.md
│   └── ui/
├── features/                     ← 功能补全 / 新功能
│   ├── YYYY-MM-DD-Fxxx-description.md
│   └── plans/                    ← 对应的实现计划
│       └── YYYY-MM-DD-Fxxx-plan.md
├── bugfixes/                     ← Bug 修复
│   ├── YYYY-MM-DD-BFxxx-description.md
│   └── plans/
│       └── YYYY-MM-DD-BFxxx-plan.md
└── optimizations/                ← 性能优化 / UI 对齐 / 重构
    ├── YYYY-MM-DD-OPTxxx-description.md
    └── plans/
        └── YYYY-MM-DD-OPTxxx-plan.md
```

**设计原则**: spec 目录完全自包含——每一层 spec（baseline 或增量）都有对应的 plan，spec → plan → code 的完整链路在一个目录树中可追溯。

---

## spec-index.md 作为统一入口

所有 skill 读 spec 时的入口是 `spec/spec-index.md`:

```
任何 skill 需要了解"当前功能全貌"时:
  1. 读 spec-index.md
  2. 看 baseline 摘要
  3. 看增量变更中 status=done 的项
  4. 按需深入读具体文件
```

### spec-index.md 升级格式

```markdown
# Project Migration Spec

## 元数据
- 源项目: <project> (Android)
- 生成时间: YYYY-MM-DD
- a2h-spec 版本: v4
- ref 来源: ai-generated

## Baseline

| 层 | 文件 | 摘要 |
|----|------|------|
| UI | baseline/ui-manifest.md | X 页面, P0*a P1*b P2*c |
| 功能 | baseline/feature-index.md | X 功能, 依赖图 |
| 基础 | baseline/feature-base.md | Models, DB, Network, Events |

## 增量变更

### Features

| ID | 标题 | 优先级 | 状态 | 影响层 | 文件 |
|----|------|--------|------|--------|------|

### Bugfixes

| ID | 标题 | 状态 | 影响层 | 文件 |
|----|------|------|--------|------|

### Optimizations

| ID | 标题 | 状态 | 影响层 | 文件 |
|----|------|------|--------|------|

## 当前状态摘要

- Baseline: ui-manifest(X页面) + feature-index(X功能) + feature-base + features(X个)
- 增量: Features x0 | Bugfixes x0 | Optimizations x0
- 下一编号: F-xxx / BF-xxx / OPT-xxx（从 spec-index.md 读取）

## 交叉引用

<!-- baseline 交叉引用 -->
<!-- 增量交叉引用追加 -->
```

---

## References

- 增量 spec 模板: `templates/increment-spec-template.md`
- a2h-spec skill: `arkts-skills/skills/a2h-spec/SKILL.md`
- 迁移 Spec baseline: `spec/baseline/`（固化后）
- 统一索引入口: `spec/spec-index.md`
