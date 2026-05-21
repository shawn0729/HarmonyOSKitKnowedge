---
name: arkts-knowledge-verifier
description: ArkTS 知识验证与查找入口。当你对任何 ArkTS/HarmonyOS 知识点不确定时（包括但不限于：API 版本兼容性、组件属性是否存在、装饰器语法规则、权限字符串、ArkTS 与 TypeScript 的差异、配置字段含义、导入路径是否正确），务必触发此 skill。它会指引你到正确的 reference 文件查找确切信息，避免生成错误代码。即使用户只是问"这个 API 对不对"或"ArkTS 能用 any 吗"，也应触发。
---

# ArkTS Knowledge Verifier — 知识验证与查找入口

## HarmonyOS Kit 知识使用规则

本 skill 的工程实践、迁移步骤和 ownership 以当前 skill 原内容为准。涉及具体 HarmonyOS Kit API、错误码、导入路径、权限、版本兼容、FAQ、最佳实践时，必须读取 `references/harmonyos-sdk/` 下对应 Kit 资料。

先按本 skill 的分层查找策略确定不确定性类别，再按任务场景读取对应 Kit 的 `routing.md` / `guides.md`。API、导入、权限、错误码、版本兼容以 Kit references 和 sources 为准。排障、适配或行为异常必须读取对应 Kit 的 `best-practices-and-faq.md`。当本 skill 原规则与 Kit 资料冲突时，保留工程分层和 ownership，用 Kit 知识修正具体 API 调用。不确定时继续使用本 skill 做交叉验证。

## HarmonyOS Kit 路由索引

当问题涉及具体 HarmonyOS Kit API、错误码、权限、导入路径或版本兼容，但当前上下文不确定应该读取哪个 skill 时，先读取 `references/harmonyos-sdk/kit-routing-index.md`。

该索引只负责指路，不替代目标 skill。确认目标后，必须读取目标 skill 的 `SKILL.md` 和对应 `references/harmonyos-sdk/<kit>/` 资料。

### 本 skill 已融合的 Kit

Kit 任务场景覆盖见 `references/harmonyos-sdk/kit-task-scenarios.md`。

- ArkUI：用于界面实现、组件行为、状态语义和版本兼容不确定性验证；入口路径 `references/harmonyos-sdk/arkui/routing.md`。
- ArkTS：用于语言语法、数据转换、类型约束和迁移写法不确定性验证；入口路径 `references/harmonyos-sdk/arkts/routing.md`。
- Network Kit：用于网络能力、通信行为、权限边界和异常处理不确定性验证；入口路径 `references/harmonyos-sdk/network-kit/routing.md`。

## 何时使用此 Skill

当你对以下任何一类知识点不确定时，使用此 skill 的分层查找策略来验证：

| 不确定性类别 | 典型场景 | 首选查找位置 |
|---|---|---|
| **组件属性** | 不确定某组件是否有某个属性/方法 | `arkts-component-builder/references/common-components.md` |
| **装饰器语法** | 不确定装饰器的初始化规则或组合方式 | `arkts-state-manager/references/state-decorators.md` |
| **权限字符串** | 不确定权限的完整名称 | `arkts-project-scaffolder/SKILL.md` 权限速查表 |
| **配置字段** | 不确定配置文件的字段名/格式 | `arkts-project-scaffolder/references/config-reference.md` |
| **导入路径** | 不确定 @kit.* 的正确模块名 | 本 skill 的 @ohos→@kit 映射表（见下文） |
| **版本兼容** | 不确定某 API 在目标版本是否可用 | 本 skill references/ |
| **语言限制** | 不确定 ArkTS 相对 TypeScript 的限制 | 本 skill `references/arkts-vs-typescript.md` |
| **网络 API** | 不确定 HTTP 请求的参数/用法 | `arkts-data-layer/references/network-service.md` |
| **动画 API** | 不确定动画函数的参数 | `arkts-animation-builder/references/explicit-animation.md` |
| **导航 API** | 不确定 NavPathStack 的方法/参数 | `arkts-navigation-builder/references/nav-patterns.md` |

完整索引见 `references/verification-index.md`。

---

## 分层查找策略

遇到不确定的知识点时，按以下层次查找：

### Layer 1：查本地 reference 文件（总是可用）

1. 在上方"何时使用此 Skill"表中找到对应类别
2. 读取"首选查找位置"指向的 reference 文件
3. 如果该文件能回答你的问题，直接使用

这一步不需要任何外部工具，任何环境都可以执行。

### Layer 2：查官方文档（条件性）

如果你的工具环境中有网络搜索/获取能力（如 WebSearch、WebFetch、MCP 文档服务、或任何可访问 URL 的工具），可以查阅华为开发者文档：

- API 参考首页：`https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/`
- 版本 Release Notes：`https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/`
- 搜索特定 API：WebSearch `"HarmonyOS [API名称] site:developer.huawei.com"`

如果没有网络工具，**跳过此步**，直接进入 Layer 3。不要假装查阅了文档。

### Layer 3：标注不确定性（兜底）

当 Layer 1 和 Layer 2 都无法确认时：

1. 用 `[待验证]` 标记不确定的信息
2. 给出你的最佳猜测 + 推理依据（例如"根据 API 12 的模式推断..."）
3. 建议用户通过以下方式确认：
   - 在 DevEco Studio 中查看自动补全和文档提示
   - 查阅华为开发者官方文档
   - 编译验证

**示例**：
```
Text 组件支持 .fontColor() 设置字体颜色（参见 common-components.md）。
注意：Text 没有 .color() 属性 — 这是 CSS/Web 的写法，ArkTS 中用 .fontColor()。

[待验证] Text 的 .letterSpacing() 属性在 API 12 中是否可用，
建议在 DevEco Studio 中确认自动补全。
```

---

## ArkTS vs TypeScript 关键差异速查

LLM 最大的幻觉来源是把 TypeScript 经验直接套用到 ArkTS。以下是最关键的差异：

| 特性 | TypeScript | ArkTS | 常见错误 |
|---|---|---|---|
| 组件声明 | `class` | `struct`（不能继承、不能 new） | 写成 `class MyComp` |
| UI 语法 | JSX `<Comp prop={v}/>` | 链式调用 `Comp().prop(v)` | 写 JSX 标签语法 |
| build() | 无限制 | 只能放 UI 描述 | 在 build() 里声明变量、console.log |
| `any` 类型 | 允许 | **禁止** | 用 `any` 声明类型 |
| 对象解构 | `const {a,b} = obj` | 受限 | 在组件中解构 |
| DOM API | 可用 | **不存在** | 用 `document.getElementById` |
| npm 包 | 可用 | **不可用** | 试图 import npm 包 |
| 模块导入 | `from 'pkg'` | `from '@kit.*'` | 用 `@ohos.*`（已废弃） |
| 对象字面量类型 | `(data: {a: number}) => {}` | **禁止**（用 class 替代） | 回调参数用对象字面量类型 |
| `as` 断言 | `x as Type` | **禁止**（用 instanceof） | 类型窄化用 as |
| 回调参数类型 | 匿名接口 | **必须用 class** | 系统回调用对象字面量 |

**详细差异 + 代码示例**：见 `references/arkts-vs-typescript.md`

---

## 常见幻觉警示

LLM 生成 ArkTS 代码时最常犯的 9 类错误，遇到时请特别警惕：

### 1. 虚构组件属性
❌ `Text('hello').color('#333')` — Text 没有 `.color()`，应该用 `.fontColor()`
❌ `Image($r('app.media.img')).src('url')` — Image 的图片源在构造参数中传入，不是 `.src()`

### 2. 在 build() 中写逻辑语句
❌ `build() { let x = 1; ... }` — build() 中不能声明变量
❌ `build() { console.log('render'); ... }` — build() 中不能 console.log

### 3. 用 class 代替 struct
❌ `@Component class MyComp { ... }` — 必须用 `struct`

### 4. 使用废弃的 @ohos.router
❌ `import router from '@ohos.router'` — API 12+ 已废弃，用 Navigation + NavPathStack

### 5. @Prop 不初始化
❌ `@Prop title: string` — API 12+ 必须初始化：`@Prop title: string = ''`

### 6. 使用 any/unknown 类型
❌ `let data: any = ...` — ArkTS 禁止 any/unknown

### 7. 虚构权限字符串
❌ `"ohos.permission.NETWORK"` — 正确的是 `"ohos.permission.INTERNET"`
权限字符串必须精确匹配，查阅 project-scaffolder 的权限速查表

### 8. 使用 @ohos.* 导入
❌ `import { http } from '@ohos.net.http'` — 用 `import { http } from '@kit.NetworkKit'`
查阅下方的 @ohos→@kit 映射表

### 9. 混用 JSX 和 ArkTS 语法
❌ `<Text fontSize={16}>Hello</Text>` — ArkTS 不是 JSX
✓ `Text('Hello').fontSize(16)`

---

## 已验证 sys.symbol 名称清单

LLM 经常虚构不存在的 SymbolGlyph 名称。以下清单来自实际编译验证：

**已验证可用（22 个）**：
```
house, list_bullet, envelope, square_grid_2x2, line_3_horizontal,
play_fill, pause_fill, arrow_down, checkmark, plus, trash,
magnifyingglass, chevron_right, chevron_left, lock, clock, gearshape,
arrow_left, arrow_right, forward_fill, backward_fill, speaker_wave_2_fill
```

**已验证不存在 + 替代方案**：
| 猜测名称 | 替代方案 |
|---------|---------|
| `tray_arrow_down` | `envelope` |
| `dot_3_horizontal` / `ellipsis` | `line_3_horizontal` |
| `chart_bar` | `square_grid_2x2` |

> 不确定的名称请标注 `[待验证]`，建议在 DevEco Studio 中编译确认。

---

## API 命名纠错表

| 错误名称 | 正确名称 | 来自 |
|---------|---------|------|
| `promptAction.ShowActionMenuSuccessResponse` | `promptAction.ActionMenuSuccessResponse` | @kit.ArkUI |

---

## API 版本概览

| HarmonyOS 版本 | API 级别 | 发布时间 | 关键变化 |
|---|---|---|---|
| 5.0.0 | **API 12** | 2024.11 | 首个 NEXT 稳定版，@kit.* 推荐，router 废弃 |
| 5.0.1 | **API 13** | 2025.01 | 增量优化 |
| 5.0.2 | **API 14** | 2025.02 | Reader Kit, GPU 渲染 |
| 5.0.3 | **API 15** | 2025.03 | 2in1 设备 API, C API 扩展 |
| 5.0.5 | **API 17** | 2025.03 | ArkUI/Ability/ArkData 变更 |
| 5.1.0 | **API 18** | 2025.06 | 媒体和 Web 能力增强 |
| 6.0.0 | **API 20** | 2025.06 | 大版本更新 |
| 6.0.1 | **API 21** | 2025.11 | 当前最新稳定版 |
| 6.x | **API 23** | 2026.02 | 最新 Dev Beta |

---

## 版本检测方法

生成代码前，先确认用户的目标 API 版本：

```
读取项目的 build-profile.json5 → app.products[].compatibleSdkVersion
括号内的数字（或直接的数字）就是 API 级别。

示例：
  compileSdkVersion: 12              → API 12
  compileSdkVersion: "5.0.0(12)"     → API 12
  compatibleSdkVersion: 22           → API 22
```

如果无法确定版本，**默认按 API 12 生成代码**（最低兼容基线）。

---

## @ohos → @kit 模块映射表

API 12+ 推荐使用 `@kit.*` 导入。完整映射见 `references/api12-baseline.md`，以下是最常用的：

| 旧 (@ohos.*) | 新 (@kit.*) |
|---|---|
| `@ohos.window` | `@kit.ArkUI` |
| `@ohos.router` | `@kit.ArkUI`（但 router 本身已废弃，用 Navigation） |
| `@ohos.curves` | `@kit.ArkUI` |
| `@ohos.net.http` | `@kit.NetworkKit` |
| `@ohos.net.connection` | `@kit.NetworkKit` |
| `@ohos.data.preferences` | `@kit.ArkData` |
| `@ohos.data.relationalStore` | `@kit.ArkData` |
| `@ohos.app.ability.UIAbility` | `@kit.AbilityKit` |
| `@ohos.app.ability.common` | `@kit.AbilityKit` |
| `@ohos.multimedia.image` | `@kit.ImageKit` |
| `@ohos.file.fs` | `@kit.CoreFileKit` |
| `@ohos.hilog` | `@kit.PerformanceAnalysisKit` |
| `@ohos.notification` | `@kit.NotificationKit` |

---

## 废弃 API 替代方案（概要）

核心替代模式（详细代码见 `references/migration-patterns.md`）：

| 废弃 | 替代 | 说明 |
|---|---|---|
| `router.pushUrl()` | `navPathStack.pushPathByName()` | API 12+ |
| `router.back()` | `navPathStack.pop()` | API 12+ |
| `@ohos.data.preferences` | `import { preferences } from '@kit.ArkData'` | 仅导入路径变化 |
| `@Prop title: string` | `@Prop title: string = ''` | API 12+ 必须初始化 |
| `Child({ link: $var })` | `Child({ link: this.var })` | API 12+ 推荐 |

---

## 各版本 Breaking Changes 概要

- **API 12**（基线）：@Prop 必须初始化、@Link 不需 $ 前缀、router 废弃、@kit.* 推荐、keyframeAnimateTo 新增
- **API 13~15**：增量优化，无 Breaking Changes
- **API 17**：部分组件属性调整、RelationalStore 接口微调
- **API 18~20**：媒体/Web 增强，权限模型微调
- **API 21**：稳定性优化

**详细变化清单**：见 `references/api13-21-changes.md`

---

## canIUse() 特性检测

运行时检查设备是否支持某个系统能力：

```typescript
if (canIUse('SystemCapability.Multimedia.Camera.Core')) {
  // 有相机能力
}

// 常用系统能力
'SystemCapability.Communication.NetStack'          // 网络
'SystemCapability.Multimedia.Camera.Core'           // 相机
'SystemCapability.Location.Location.Core'           // 定位
'SystemCapability.ArkUI.ArkUI.Full'                // 完整 ArkUI
```

---

## 生成检查清单

- [ ] 确认了用户的目标 API 版本（读 build-profile.json5）
- [ ] 对不确定的知识点执行了分层查找
- [ ] 导入使用 `@kit.*` 而非 `@ohos.*`
- [ ] 导航使用 `Navigation` 而非 `@ohos.router`
- [ ] `@Prop` 变量有默认初始值
- [ ] 没有使用 `any` / `unknown` 类型
- [ ] 组件属性名称已验证（如 `.fontColor()` 而非 `.color()`）
- [ ] 权限字符串经过查证
- [ ] 不确定的信息已标注 `[待验证]`

---

## Skill 路由指南

当你被触发但用户的需求超出本 skill 范围时，使用以下决策树判断应该读取哪个 skill 的内容：

### 决策树

```
用户请求的核心是什么？
│
├─ 问知识点/验证语法 → 在本 skill 内回答（分层查找策略）
│
├─ 要 UI 组件/页面布局 → 读取 arkts-component-builder/SKILL.md
│
├─ 要完整业务功能（列表详情页、搜索、登录等）
│   └─ 读取 arkts-pattern-library/SKILL.md（它有编排协议引导后续步骤）
│
├─ 要从零搭建项目
│   └─ 读取 arkts-project-scaffolder/SKILL.md（它有 6 步编排指南）
│
├─ 要动画效果 → 读取 arkts-animation-builder/SKILL.md
│
├─ 要页面导航/路由 → 读取 arkts-navigation-builder/SKILL.md
│
├─ 要状态管理/数据通信 → 读取 arkts-state-manager/SKILL.md
│
├─ 要数据请求/持久化 → 读取 arkts-data-layer/SKILL.md
│
├─ 要三方库替代方案 → 读取 arkts-library-migration/SKILL.md
│
├─ 要媒体播放/AVPlayer/后台播放 → 读取 arkts-media-playback/SKILL.md
│
├─ 要文件下载/下载管理 → 读取 arkts-download-manager/SKILL.md
│
├─ 要 Android UI 对齐/Material 迁移 → 读取 arkts-ui-alignment/SKILL.md
│
└─ 要系统能力（媒体/权限/文件/后台任务） → 读取 arkts-system-capabilities/SKILL.md
```

### 综合回答

即使被触发的是 knowledge-verifier，你也可以读取其他 skill 的 reference 文件来给出综合回答。例如用户问"下拉刷新列表怎么做"，可以同时读取 pattern-library 的模式模板和 data-layer 的 BasicDataSource 实现来组织完整回答。

> 完整的请求分类矩阵、场景路由表和输出合并协议见 `references/skill-routing-guide.md`

---

## References

- `references/api12-baseline.md` — API 12 基线：完整的导入映射 + 状态装饰器规则 + 导航方案
- `references/api13-21-changes.md` — API 13~21 每个版本的增量变化清单
- `references/migration-patterns.md` — @ohos→@kit 迁移代码对照、router→Navigation 迁移步骤
- `references/arkts-vs-typescript.md` — ArkTS 与 TypeScript 的所有关键差异 + 代码示例
- `references/verification-index.md` — 全 skill 体系知识查找索引
- `references/skill-routing-guide.md` — Skill 路由与编排指南（请求分类矩阵 + 场景路由表 + 输出合并协议）
- `references/real-migration-pitfalls.md` — 22 条实战踩坑百科（AVPlayer/下载/UI/语言/导航/数据库/网络）
