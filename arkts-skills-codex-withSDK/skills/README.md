# Android→ArkTS 迁移 Skill 体系（Codex 适配版）

双层架构：5 个 Pipeline Skills（用户接口）+ 33 个 Domain Skills（默认内部实现）+ 2 个工具 Skills + 10 个 WFHc 风格 Skills（已迁至 `.agents/skills_type/`）+ 3 个 Agent（TOML 格式，`.codex/agents/`）。

默认 Skills 位于 `.agents/skills/`（Codex 标准路径），WFHc 风格 Skills 位于 `.agents/skills_type/`，Agents 位于 `.codex/agents/`（TOML 格式）。

用户只需 5 句话完成从 Android 源码到可编译 ArkTS 项目的全流程。

---

## 架构总览

```
┌──────────────────────────────────────────────────────────┐
│ Pipeline Layer（用户接口，5 个 Skill）                      │
│                                                          │
│  a2h-spec → a2h-plan → a2h-execute → a2h-verify         │
│                                         → a2h-retrospect │
│                                                          │
│  用户只需 5 句话：                                         │
│  "分析项目" → "生成计划" → "执行" → "验证" → "回顾"        │
└────────────────────────┬─────────────────────────────────┘
                         │ 智能路由 + runtime 覆盖
┌────────────────────────▼─────────────────────────────────┐
│ Domain Layer（默认内部实现，33 个 Skill + 3 个 Agent）      │
│                                                          │
│  Spec 类:     spec-evolver                               │
│  Graph 类:    android-ui-graph-builder,                   │
│               android-ui-graph-query                     │
│  Hub 类:      project-scaffolder, pattern-library,       │
│               knowledge-verifier                         │
│  Spoke 类:    component-builder, state-manager,          │
│               navigation-builder, data-layer,            │
│               animation-builder, library-migration,      │
│               system-capabilities, media-playback,       │
│               download-manager, ui-alignment             │
│  Identity:    arkts-app-identity                         │
│  Resource:    android2hmos_resources_convert              │
│  Build:       hmos_fix_build_errors                      │
│  Issue:       fix-issue                                  │
│  Codebase 类: codebase-config, codebase-debug,           │
│               codebase-explainer, codebase-locator,      │
│               codebase-modifier                          │
│  Analysis:    android-screenshot-analyzer                │
│  Migration:   android-view-to-arkui                      │
│  I18n:        arkts-i18n                                 │
│  Webview:     arkts-webview-manager                      │
│  Agent:       a2h-activity-converter,                     │
│               a2h-migration-worker,                      │
│               a2h-android-analyzer                       │
│                                                          │
│  [新增 domain skill 自动可用，无需改 Pipeline]              │
└──────────────────────────────────────────────────────────┘

工具类（Pipeline 外，独立使用）: drawio, skill-checker
```

## HarmonyOS Kit Knowledge Integration

`arkts-skills-codex/skills` uses two forms of HarmonyOS Kit integration:

1. **Fused Kit Knowledge** — Kit skills that overlap existing migration or generation skills are fused into those host skills under `references/harmonyos-sdk/<kit>/`. The host skill remains the trigger entry, and the Kit references provide official API, error-code, version, FAQ, and best-practice knowledge.

2. **Independent Kit Skills** — Kit skills without a natural host are migrated as peer skills under `arkts-skills-codex/skills`. They are first-class skill entries and are triggered directly for their Kit-specific scenarios.

Fused Kit skills are not copied as peer directories, to avoid ambiguous triggering. Independent Kit skills are not fallback material; they are direct skill entries.

### Independent Kit Skills

| Skill | Use When |
|---|---|
| `ads-kit-development` | Ads Kit, monetization, banner/native/rewarded/interstitial/splash ads |
| `basic-services-kit-development` | Common events, account, USB, process/thread communication |
| `crypto-architecture-kit-development` | Encryption, decryption, key generation, certificate, signature |
| `form-kit-development` | Service widgets, FormExtensionAbility, card refresh and interaction |
| `share-kit-development` | System share, share panel, Knock Share, Air Transfer |

### Fused Kit Knowledge

| Kit | Host Skills |
|---|---|
| ArkUI | `arkts-component-builder`, `arkts-state-manager`, `arkts-navigation-builder`, `arkts-animation-builder`, `arkts-ui-alignment`, `arkts-knowledge-verifier` |
| ArkTS | `arkts-knowledge-verifier`, `arkts-data-layer` |
| ArkData | `arkts-data-layer`, `arkts-state-manager` |
| Network Kit | `arkts-data-layer`, `arkts-download-manager`, `arkts-knowledge-verifier` |
| Ability Kit | `arkts-project-scaffolder`, `arkts-system-capabilities`, `arkts-navigation-builder` |
| Core File Kit | `arkts-system-capabilities`, `arkts-download-manager`, `android2hmos_resources_convert` |
| Media Kit | `arkts-media-playback`, `arkts-system-capabilities` |
| Image Kit | `arkts-system-capabilities`, `arkts-ui-alignment`, `android2hmos_resources_convert` |
| ArkWeb | `arkts-webview-manager`, `arkts-system-capabilities` |
| Performance Analysis Kit | `hmos-env-doctor`, `arkts-codebase-debug`, `hmos_fix_build_errors` |

---

## Pipeline Skills（用户接口，5 个）

| Skill | 触发 | 说明 | 产出物 |
|-------|------|------|--------|
| `a2h-spec` | "分析项目" / "开始迁移" / "功能缺失" | 三阶段 Spec 生成（数据准备 + UI 清单 + 功能 Spec） | `spec/baseline/ui-manifest.md` + `feature-index.md` + `features/` |
| `a2h-plan` | "生成计划" | 按 Spec 智能拆分执行计划 | `spec/baseline/plans/plan.md` |
| `a2h-execute` | "执行" | Agent 驱动执行 + runtime skill 覆盖 | ArkTS 代码 + `spec/migration-report.md` |
| `a2h-verify` | "验证" / "测试" | 编译 + 静态分析 + 页面状态审计 + UI 对齐 | `spec/verify-report.md` |
| `a2h-retrospect` | "回顾" / "优化" | 沉淀经验，优化 domain skill | `docs/retrospect-report-YYYY-MM-DD.md` |

### 五步流水线

```
用户: "分析这个 Android 项目"  → a2h-spec     → Spec + UI 图谱     → 人工审批
用户: "生成计划"              → a2h-plan     → 1-N 个 plan.md     → 人工审批
用户: "执行"                 → a2h-execute  → ArkTS 代码          → 编译通过
用户: "验证"                 → a2h-verify   → verify-report.md   → P0 页面 verified
用户: "回顾"                 → a2h-retrospect → retrospect-report → 人工审批
```

### 新项目从头开始的推荐顺序

如果是一个新的 Android→ArkTS 迁移项目，建议严格按下面顺序执行：

1. `@a2h-spec` 分析 `{ANDROID_SRC}`
2. `@a2h-plan` 生成计划
3. 人工审批 `ui-plan.md` / `feature-plan.md`
4. `@a2h-execute` 从 Batch 1 开始，强制使用 `.codex/agents`
5. `@a2h-verify` 做主工作区验证
6. `@a2h-retrospect` 沉淀经验并优化 skill / agent

推荐原因：
- `a2h-spec` 先把三源数据、页面清单和功能基线做全，避免后续页面转换缺上下文
- `a2h-plan` 把 UI 批次和 Feature Slice 拆开，便于审批和分阶段执行
- `a2h-execute` 必须在 Stage 1 强制使用 `a2h-activity-converter`，不要用主执行器本地直改页面兜底
- 每个 Batch 完成后必须在主工作区编译，编译失败优先回灌给对应 page agent 修复
- `a2h-verify` 负责确认页面状态、编译结果和占位符登记
- `a2h-retrospect` 负责把本轮踩坑固化回 skill / agent，避免下个项目重复犯错

推荐执行 prompt：

```text
1. @a2h-spec 分析 `{ANDROID_SRC}`
2. @a2h-plan 生成计划
3. 我审批 ui-plan / feature-plan
4. @a2h-execute 从 Batch 1 开始，强制使用 .codex/agents
5. @a2h-verify 做主工作区验证
6. @a2h-retrospect 沉淀经验并优化 skill / agent
```

---

## Domain Skills（默认内部实现，33 个）

### WFHc 风格 Skills（已迁出到 `.agents/skills_type/`）

这组 skills 属于 `style-set: wfhc-standard`，当前已经迁到 `.agents/skills_type/`，不属于默认自动发现集合。只有你后续显式接入或重新迁回 `.agents/skills/`，Codex 才会把它们当作可直接触发的 skills。

只有在以下条件之一满足时，才建议把它们重新作为强规则注入：

- plan 或任务上下文显式设置 `style_set: wfhc-standard`
- 用户明确要求“按 WFHc 风格/规范执行”
- 目标仓已经存在 `lib_common`、`lib_network`、`BaseViewModel`、`RouterUtils` 等 WFHc 约定

如果以上条件都不满足，这组 skill 应保持为 advisory mode：只输出风格差异和可选迁移方向，不要虚构企业私有 lib 或强行重构项目结构。

| Skill | 类型 | 用途 |
|-------|------|------|
| `arkts-style-orchestrator` | 编排器 | 根据场景挑选并注入 WFHc 风格 skills |
| `arkts-project-structure` | 叶子 skill | `products/features/components` 三层模块架构 |
| `arkts-state-v2` | 叶子 skill | v2 状态管理装饰器与全局状态模式 |
| `arkts-viewmodel-pattern` | 叶子 skill | `BaseViewModel` / `@ObservedV2` / 单例生命周期 |
| `arkts-ui-component` | 叶子 skill | UI 组件分层、`@Builder` 导出、`NavDestination` 页面壳层 |
| `arkts-network-request` | 叶子 skill | `lib_network` / `RequestUtil` 请求规范 |
| `arkts-navigation-routing` | 叶子 skill | `RouterUtils`、路由常量分层、类型化路由参数 |
| `arkts-lib-usage-guide` | 叶子 skill | `lib_common` / `lib_widget` / `lib_payment` 等企业 lib 使用边界 |
| `arkts-config-engineering` | 叶子 skill | `build-profile`、签名、`GlobalUtils`、工程化约定 |
| `arkts-scan-capabilities` | 叶子 skill | 扫描/OCR/图片处理/文档持久化领域规范 |

### Spec 类

| Skill | 用途 | 阶段 |
|-------|------|------|
| `arkts-spec-evolver` | 增量 spec 演进（功能补全/Bug 修复/优化/审计） | Phase 8+ |

### Graph 类

| Skill | 用途 | 阶段 |
|-------|------|------|
| `android-ui-graph-builder` | Python 确定性解析 Android XML 布局，构建 UI 知识图谱 (4 JSON) | Phase 1 |
| `android-ui-graph-query` | 查询 UI 图谱，获取迁移上下文（组件树/属性/导航关系） | Phase 6c |

### Hub 类（编排入口）

| Skill | 用途 | 阶段 |
|-------|------|------|
| `arkts-project-scaffolder` | 项目骨架搭建（目录/配置/EntryAbility/GlobalState/AppRouter） | Phase 2 |
| `arkts-pattern-library` | 完整业务功能编排（搜索/列表详情/登录/设置） | Phase 6c |
| `arkts-knowledge-verifier` | ArkTS 知识验证兜底（API 兼容性/装饰器语法/导入路径） | 全阶段 |

### Spoke 类（领域专家）

| Skill | 用途 | 阶段 |
|-------|------|------|
| `arkts-component-builder` | 声明式 UI 组件生成（Column/Row/List/Grid/ForEach） | Phase 6c |
| `arkts-state-manager` | 状态管理（@State/@Prop/@Link/AppStorage/Preferences） | Phase 6b |
| `arkts-navigation-builder` | 页面导航（Navigation/NavPathStack/Tabs/路由映射） | Phase 6a |
| `arkts-data-layer` | 数据层（Model/DAO/HTTP/IDataSource/Preferences） | Phase 4-5 |
| `arkts-animation-builder` | 动画效果（animateTo/transition/手势动画/弹簧动画） | Phase 6c |
| `arkts-library-migration` | 三方库替代方案查找与决策 | Phase 3 |
| `arkts-system-capabilities` | 系统 API（权限/文件/媒体查询/后台任务/沙箱路径） | Phase 4 |
| `arkts-media-playback` | AVPlayer 音视频播放（fd://协议/后台播放/AVSession） | Phase 6c |
| `arkts-download-manager` | 大文件下载（request.agent/进度追踪/队列管理） | Phase 6c |
| `arkts-ui-alignment` | Android UI 视觉还原（Material Design 映射/SymbolGlyph） | Phase 6c |
| `arkts-truncation-fix` | 多设备 UI 截断 / 安全区遮挡 / 折叠屏 / 响应式断点修复 | Phase 6c / Phase 7 |

### Resource / Build / Issue 类

| Skill | 用途 | 阶段 |
|-------|------|------|
| `android2hmos_resources_convert` | Android 资源转换（strings/colors/drawables → HarmonyOS） | Phase 2 |
| `hmos_fix_build_errors` | 自动编译修复循环（最多 20 轮，全阶段可用） | 全阶段 |
| `hmos-env-doctor` | HarmonyOS 开发环境诊断与修复（DevEco/工具链/签名/权限/真机运行） | Phase 0 / 全阶段 |
| `fix-issue` | GitHub Issue 驱动修复工作流 | 全阶段 |

### Codebase 类（代码库问答，5 个）

面向已有 ArkTS/HarmonyOS 代码库的智能问答 Skill，覆盖定位、解释、调试、修改建议、配置查询五大场景。

| Skill | 用途 | 典型触发问题 |
|-------|------|-------------|
| `arkts-codebase-locator` | 功能定位 — 快速找到功能入口和核心文件 | "xx 功能在哪实现？""导出逻辑在哪？" |
| `arkts-codebase-explainer` | 功能解释 — 分析执行流程、交互逻辑、技术细节 | "点击下载后发生了什么？""数据是怎么流转的？" |
| `arkts-codebase-debug` | 缺陷诊断 — 定位问题入口和可疑点，提供修复建议 | "列表不刷新""页面白屏""网络请求失败" |
| `arkts-codebase-modifier` | 修改建议 — 基于代码仓事实的功能修改方案（不直接改代码） | "怎么加个下拉刷新？""如何扩展搜索功能？" |
| `arkts-codebase-config` | 配置问答 — 定位配置项的定义、读取位置、默认值及覆盖路径 | "权限在哪配的？""这个 Flag 在哪控制？" |

### Analysis 类

| Skill | 用途 | 阶段 |
|-------|------|------|
| `android-screenshot-analyzer` | App 页面截图分析与命名，识别页面功能/布局/风格，输出结构化文档 | Phase 1（辅助） |
| `app-relationship-tree` | 多源聚合生成 `app-relationship-tree.json`（页面/导航/组件关系树），融合 ui-graph-builder + spec + ArkTS 源码 | Phase 1 / Phase 7 |

### Verification 类

| Skill | 用途 | 阶段 |
|-------|------|------|
| `arkts-visual-verify` | 按页面粒度自动截图对比验证（adb + hdc + 多模态对比），单页闭环修复，a2h-verify CHECK-7 增强执行器 | Phase 7 |

### Migration 类

| Skill | 用途 | 阶段 |
|-------|------|------|
| `android-view-to-arkui` | Android View/XML UI 到 ArkUI 的受控批次迁移（特性批次流程） | Phase 6c（替代方案） |

### I18n 类

| Skill | 用途 | 阶段 |
|-------|------|------|
| `arkts-i18n` | 国际化支持（多语言/动态切换/资源配置/硬编码扫描） | 全阶段 |

### Webview 类

| Skill | 用途 | 阶段 |
|-------|------|------|
| `arkts-webview-manager` | WebView 开发（WebviewController API/CSS·JS 注入/多 WebView 分屏/页面模式/字体控制/页内搜索/标签页/页面翻译/TTS 朗读） | 全阶段 |

### 工具类（Pipeline 外）

| Skill | 用途 | 阶段 |
|-------|------|------|
| `drawio` | 生成 .drawio 流程图/架构图/时序图，可导出 PNG/SVG/PDF | 独立使用 |
| `skill-checker` | 检查新增/修改的 Skill/Agent/Command/Rule 是否符合项目规范与 Skill Hub 管理规范 | 独立使用 |

---

## Agent（3 个）

| Agent | 用途 | 编排的 Skill | 阶段 |
|-------|------|-------------|------|
| `a2h-android-analyzer` | Android 项目分析，生成 spec.md + design.md 参考文档 | (无 skill 依赖) | Phase 0（可选前置） |
| `a2h-migration-worker` | 通用迁移工作 agent，执行任何迁移 task | 32 个 domain skills | Phase 1-7 |
| `a2h-activity-converter` | 单个 Activity UI 页面迁移到 ArkTS | graph-query + resources-convert + fix-build-errors | Phase 6c |

位置：`.codex/agents/`（TOML 格式）

---

## Skill 绑定机制

```
Plan 生成时: 每个 task 标注 suggested_skills: [...]
  │
  ▼ Execute 执行时:
  ├─ 主路径: 读 suggested_skills，加载对应 domain skill
  ├─ 覆盖路径: agent 检查 runtime 上下文
  │   ├─ UI 迁移 → 委托 a2h-activity-converter agent
  │   ├─ 编译失败 → hmos_fix_build_errors
  │   ├─ API 不确定 → knowledge-verifier
  │   ├─ 资源缺失 → android2hmos_resources_convert
  │   └─ 国际化 → arkts-i18n
  └─ 发现机制: description 匹配 + tags 过滤
```

---

## 报告链路

```
a2h-execute   → spec/migration-report.md
                      ↓ 被读取
a2h-verify    → spec/verify-report.md
                      ↓ 被读取
a2h-retrospect → docs/retrospect-report-YYYY-MM-DD.md
```

---

## 目录结构

```
.agents/skills/
├── README.md                          ← 本文件
│
├── a2h-spec/                          ← Pipeline（用户接口）
├── a2h-plan/
├── a2h-execute/
├── a2h-verify/
├── a2h-retrospect/
│
├── arkts-spec-evolver/
│   └── SKILL.md + templates/
│
├── android-ui-graph-builder/          ← Domain - Graph 类
│   └── SKILL.md + references/ + scripts/
├── android-ui-graph-query/
│   └── SKILL.md + references/ + scripts/
│
├── arkts-project-scaffolder/          ← Domain - Hub 类
├── arkts-pattern-library/
├── arkts-knowledge-verifier/
│
├── arkts-component-builder/           ← Domain - Spoke 类
├── arkts-state-manager/
├── arkts-navigation-builder/
├── arkts-data-layer/
├── arkts-animation-builder/
├── arkts-library-migration/
├── arkts-system-capabilities/
├── arkts-media-playback/
├── arkts-download-manager/
├── arkts-ui-alignment/
│
├── android2hmos_resources_convert/    ← Domain - Resource / Build / Issue
│   └── SKILL.md + references/ + tools/
├── hmos_fix_build_errors/
├── fix-issue/
│
├── arkts-codebase-locator/            ← Domain - Codebase 类
│   └── SKILL.md + references/
├── arkts-codebase-explainer/
├── arkts-codebase-debug/
│   └── SKILL.md + references/
├── arkts-codebase-modifier/
│   └── SKILL.md + references/
├── arkts-codebase-config/
│   └── SKILL.md + references/
│
├── android-screenshot-analyzer/       ← Domain - Analysis 类
│   └── SKILL.md + evals/ + references/
├── android-view-to-arkui/             ← Domain - Migration 类
│   └── SKILL.md + agents/ + references/ + scripts/
├── arkts-i18n/                        ← Domain - I18n 类
│   └── SKILL.md + evals/ + references/
├── arkts-webview-manager/             ← Domain - Webview 类
│   └── SKILL.md + references/
│
└── drawio/                            ← 工具类（Pipeline 外）
```

---

## Skill 分类速查

### 按迁移阶段

| 阶段 | Domain Skill |
|------|-------------|
| Phase 1 分析 | a2h-spec (Phase A/B/C), android-ui-graph-builder, android-screenshot-analyzer（辅助） |
| Phase 2 骨架 | project-scaffolder, android2hmos_resources_convert |
| Phase 3 三方库 | library-migration |
| Phase 4 适配层 | system-capabilities, data-layer |
| Phase 5 数据层 | data-layer |
| Phase 6a 导航 | navigation-builder |
| Phase 6b 状态 | state-manager |
| Phase 6c 组件 | component-builder, pattern-library, animation-builder, media-playback, download-manager, ui-alignment, arkts-webview-manager, android-view-to-arkui（替代方案） |
| Phase 7 验证 | knowledge-verifier, hmos_fix_build_errors |
| Phase 8+ 迭代 | spec-evolver |
| 全阶段 | knowledge-verifier, hmos_fix_build_errors, fix-issue, arkts-i18n, arkts-webview-manager |
| 代码库问答 | codebase-locator, codebase-explainer, codebase-debug, codebase-modifier, codebase-config |

### 按使用场景

| 场景 | Skill |
|------|-------|
| 迁移流水线（核心） | 5 Pipeline + spec-evolver + scaffolder + data-layer + navigation-builder + state-manager + component-builder + activity-converter (agent) + fix-build-errors |
| UI 还原 | ui-graph-builder/query + screenshot-analyzer + view-to-arkui + ui-alignment + activity-converter (agent) |
| 代码库理解 | codebase-locator + codebase-explainer + codebase-config |
| 问题排查 | codebase-debug + knowledge-verifier + fix-issue |
| 功能增强 | codebase-modifier + pattern-library + animation-builder |
| WebView | arkts-webview-manager |
| 国际化 | arkts-i18n |
| 工具 | drawio |

---

## 设计原则

| 原则 | 说明 |
|------|------|
| 关注点分离 | Pipeline 管"什么时候做"，Domain 管"怎么做" |
| 薄 Pipeline | Pipeline Skill 只做路由和编排，不实现业务逻辑 |
| 自动发现 | 新增 Domain Skill 只要有正确的 description，Pipeline 自动发现 |
| 只升级不降级 | Execute 的 runtime 覆盖只会切到更精确的 Skill |
| 三级渐进加载 | description(~100词) → SKILL.md(<500行) → references/(按需) |
