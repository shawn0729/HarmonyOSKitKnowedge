# 鸿蒙文档加工为工程能力 Skill 的设计

## 目标

输入已经是 Markdown 文档，例如：

- `output.md`：鸿蒙开发者文档中的最佳实践。
- `tabs.md`：鸿蒙开发者文档中的 FAQ。

后续目标不是把这些 Markdown 继续整理成资料库、索引或文档摘录，而是把它们加工成可以指导模型进行鸿蒙代码生成的工程能力。

也就是说，Skill 不应只是回答“文档里说了什么”，而应让模型在生成、修改、诊断鸿蒙代码时自动执行更专业的工程判断。

## 核心原则

### 文档不是最终形态

最佳实践和 FAQ 文档只是原料。真正要沉淀的是：

- 代码生成前的设计判断。
- 代码生成中的结构选择。
- 代码生成后的质量检查。
- 问题排查时的诊断路径。
- 可迁移到用户项目的代码模式。

### Skill 不是资料库

不要把完整文档按章节塞入 `references/`，再让模型临时查找。这样会让 Skill 退化成资料检索。

更好的做法是把文档内容转化为：

- 工程流程。
- 反模式检测。
- 修复策略。
- 代码生成规则。
- 质量门禁。

### 最佳实践和 FAQ 应加工成不同类型的能力

最佳实践应先区分规范型和功能型：规范型沉淀约束和质量规则，功能型沉淀任务链路和 API 组合。

FAQ 更适合加工成诊断型、修复型、场景解法型能力。

一句话概括：

```text
最佳实践类 Skill：把文档加工成规范型能力或功能型能力，分别沉淀工程约束、任务链路、API 组合和可迁移代码模板。

FAQ 类 Skill：把文档加工成模型解决具体鸿蒙问题时使用的诊断流程、修复模式和可迁移代码模板。
```

## 最佳实践 Skill 设计

### 一句话定位

最佳实践类文档不只有“规范建议”，也可能是“端到端功能实践”。设计 Skill 时应先判断它属于规范型最佳实践，还是功能型最佳实践。

```text
规范型最佳实践：沉淀工程约束、反模式检测、质量门禁。
功能型最佳实践：沉淀任务链路、API 组合、能力路由、可迁移代码模板。
```

不要把最佳实践文档都做成“生成前/中/后工作方式”。很多最佳实践本质上是在教模型完成一个功能。

### 类型判断

#### 规范型最佳实践

适合以下文档：

- 状态管理最佳实践。
- 性能优化最佳实践。
- 组件拆分最佳实践。
- 架构治理或工程规范。
- 可维护性、可测试性、刷新控制等质量类主题。

这类 Skill 主要回答：

```text
这段代码怎样写才更符合工程质量？
应该避免哪些反模式？
生成后要检查哪些质量问题？
```

#### 功能型最佳实践

适合以下文档：

- 图片获取与保存实践。
- 文件选择与上传实践。
- 登录授权接入实践。
- 分享、支付、定位、地图、推送等端到端能力接入实践。
- 跨多个 Kit/API 才能完成的功能开发实践。

这类 Skill 主要回答：

```text
这个功能应该按什么链路实现？
涉及哪些 Kit 和 API？
不同场景如何选型？
代码模板如何迁移到用户项目？
```

### 规范型最佳实践的组织方式

以 `output.md` 中 ArkUI 状态管理最佳实践为例，它适合加工为：

```text
arkui-state-engineering/
  SKILL.md
  capabilities/
    state-necessity.md
    decorator-selection.md
    state-sharing-scope.md
    state-refresh-control.md
  examples/
    redundant-state-before-after.md
    batch-state-update-before-after.md
    appstorage-splitting-pattern.md
    watch-precision-refresh-before-after.md
```

`SKILL.md` 负责触发和路由：

```markdown
## 能力路由

- 判断状态变量是否必要、只读变量是否误用状态装饰器：
  读取 `capabilities/state-necessity.md`

- 选择 `@State`、`@Prop`、`@Link`、`@ObjectLink`、`@Provide/@Consume`、`LocalStorage`、`AppStorage`：
  读取 `capabilities/decorator-selection.md`

- 判断状态共享范围、避免层层传参或过度共享：
  读取 `capabilities/state-sharing-scope.md`

- 控制刷新范围、使用 `@Watch` 或订阅机制减少无关刷新：
  读取 `capabilities/state-refresh-control.md`
```

capability 文件写工程规则和判断依据，不堆完整原文。

例如 `capabilities/decorator-selection.md` 可以写：

```text
覆盖范围：组件内状态、父子状态同步、跨层级共享、页面级/应用级共享。
核心判断：共享范围、绑定方向、数据复杂度、生命周期。
示例路由：复杂对象双向同步读取 Link 示例；嵌套对象属性监听读取 ObjectLink 示例。
常见错误：默认使用 @State；用 AppStorage 解决局部状态；用 @Prop 传复杂大对象导致拷贝成本。
```

### 功能型最佳实践的组织方式

以“图片获取与保存实践”为例，它不适合做成规范门禁型 Skill，而适合做成端到端功能接入 Skill：

```text
image-get-save-development/
  SKILL.md
  capabilities/
    image-get-flow.md
    image-read-flow.md
    image-save-flow.md
  examples/
    pick-image-from-album-template.md
    take-photo-template.md
    read-image-info-template.md
    save-pixelmap-to-file-template.md
    save-image-to-gallery-pattern.md
```

`SKILL.md` 负责触发和路由：

```markdown
## 能力路由

- 相册选择、页面内嵌相册选择、拍照获取图片：
  读取 `capabilities/image-get-flow.md`

- 读取图片宽高、像素信息、EXIF 信息、创建 `ImageSource`：
  读取 `capabilities/image-read-flow.md`

- 保存 `PixelMap` 到文件目录、保存图片到系统相册、图片编码：
  读取 `capabilities/image-save-flow.md`
```

capability 文件写任务链路、API 选型和 example 路由。

例如 `capabilities/image-save-flow.md` 可以写：

```text
覆盖范围：把 PixelMap 保存到应用文件目录或系统相册。
保存到文件目录链路：PixelMap -> ImagePacker -> PackingOption -> fileIo.openSync -> packToFile。
保存到系统相册链路：PixelMap -> 先编码到应用文件目录 -> Media Library Kit 入库 -> 授权与失败处理。
示例路由：保存文件读取 save-pixelmap-to-file-template；保存相册读取 save-image-to-gallery-pattern。
常见错误：把写入应用目录当成保存到系统相册；保存相册时不处理授权；编码后不关闭文件描述符。
```

### 最佳实践条目的沉淀形态

最佳实践条目不应按章节原样保存，而应根据用途沉淀成不同资产。

```text
规范型条目 -> rule：工程约束。
反例/正例 -> before-after：错误形态和修正形态。
性能建议 -> quality-gate：生成后检查项。
API 选型 -> decision-pattern：选择依据和代码形态。
功能步骤 -> flow：任务链路。
示例代码 -> template：可迁移代码模板。
```

### 何时拆成独立 Skill

默认优先按 Kit 大领域或工程能力域组织。

只有满足以下条件时，才把某篇最佳实践拆成独立 Skill：

- 它描述的是一个完整、常见、可复用的端到端功能。
- 触发词稳定，用户会直接提出类似任务。
- 涉及多个能力步骤或多个 Kit/API 组合。
- examples 中有多份可迁移代码模板。
- 放在大领域 Skill 下会让入口路由过长或能力边界不清。

“图片获取与保存实践”满足这些条件，因为它跨越图片获取、图片读取、图片编码、文件保存、媒体库保存和授权处理，适合独立成：

```text
image-get-save-development
```

## FAQ Skill 设计

### 一句话定位

FAQ 类文档不适合“一条 FAQ 一个 Skill”，而应按 Kit 或组件能力域组织成 Skill，再把每条 FAQ 加工成该 Skill 内的 pattern、template、diagnosis 或 example。

FAQ Skill 的重点不是复述 FAQ，也不是建立资料库，而是沉淀“遇到某类鸿蒙问题时可以复用的解法模式”。

### 粒度原则

不要按单条 FAQ 建 Skill。

不推荐：

```text
arkui-tabs-custom-tab-skill
arkui-tabs-align-skill
arkui-tabs-switch-skill
arkui-button-click-faq-skill
arkui-list-scroll-faq-skill
```

更推荐：

```text
arkui-component-problem-solving
arkui-tabs-problem-solving
arkui-list-scroll-problem-solving
arkui-navigation-routing-problem-solving
```

判断标准：

- 一个 Skill 覆盖一个稳定工程能力域。
- 一条 FAQ 只作为该能力域下的一个经验样例。
- 只有当某个组件或问题域足够复杂、触发词稳定、工程流程独立时，才拆成独立 Skill。
- 如果某个组件只有少量 FAQ，优先放进更大的组件问题解决 Skill。

### 按 Kit 大领域组织

当 FAQ 数量多、覆盖组件多时，优先按 Kit 大领域建立入口 Skill。

```text
arkui-development/
  SKILL.md
  capabilities/
    component-problem-solving.md
    tabs-problem-solving.md
    list-scroll-problem-solving.md
    navigation-routing-problem-solving.md
    layout-composition.md
  examples/
    tabs/
      custom-tabs-template.md
      switch-sync-diagnosis.md
      alignment-pattern.md
    list/
      lazy-foreach-pattern.md
      scroll-position-diagnosis.md
    navigation/
      navpathstack-pattern.md
      route-state-diagnosis.md
```

这里的层次关系是：

```text
SKILL.md：大领域入口和路由表。
capabilities/*.md：某个能力域的设计原则和处理模式。
examples/*：具体 FAQ 沉淀出的代码模板、诊断样例、架构模式。
```

### 如何保证大领域 Skill 被正确加载

按 Kit 大领域建 Skill 时，`description` 要覆盖常见触发词、API、组件、问题类型和代码生成场景。

示例：

```yaml
---
name: arkui-development
description: Use when 生成、修改、审查或排查 HarmonyOS ArkUI/ArkTS UI 代码，包括组件、装饰器、状态管理、Tabs、List、Scroll、Navigation、布局、交互、渲染性能、组件通信或常见 ArkUI FAQ 问题。
---
```

要点：

- `description` 负责让大领域 Skill 被加载。
- `SKILL.md` 负责把任务路由到具体能力域。
- `capabilities` 负责表达某类问题的工程模式。
- `examples` 负责承载单条 FAQ 提炼出的样例。

### SKILL.md 内部路由

大领域 `SKILL.md` 不要堆所有 FAQ 内容，只维护路由表。

示例：

```markdown
## FAQ 能力路由

- 状态管理、装饰器、组件通信、刷新控制：
  读取 `capabilities/state-engineering.md`

- Tabs、TabContent、TabsController、自定义页签、隐藏默认 tab bar、页签切换、选中态同步：
  读取 `capabilities/tabs-problem-solving.md`

- List、ListItem、LazyForEach、列表滚动、列表刷新、滚动性能：
  读取 `capabilities/list-scroll-problem-solving.md`

- Navigation、NavPathStack、页面跳转、路由栈、路由状态共享：
  读取 `capabilities/navigation-routing.md`

- Row、Column、Flex、Stack、Grid、布局适配：
  读取 `capabilities/layout-composition.md`
```

FAQ 的高频关键词必须出现在入口 `description` 或 `SKILL.md` 路由表里。不要只写在 example 文件中，因为 example 文件不会自动触发。

### FAQ 条目的沉淀形态

单条 FAQ 应转成能力域下的子资产，而不是单独 Skill。

常见形态：

```text
FAQ 条目 -> template：可迁移代码模板。
FAQ 条目 -> diagnosis：问题诊断清单。
FAQ 条目 -> pattern：API 组合模式或架构模式。
FAQ 条目 -> before-after：存在明确错误写法和修正写法时使用。
```

以 `tabs.md` 为例，它可以沉淀为：

```text
capabilities/tabs-problem-solving.md
examples/tabs/custom-tabs-template.md
examples/tabs/switch-sync-diagnosis.md
examples/tabs/alignment-pattern.md
```

其中：

- `custom-tabs-template.md`：沉淀自定义页签、`TabsController`、`.barHeight(0)`、`onContentWillChange` 的代码模板。
- `switch-sync-diagnosis.md`：沉淀“点击后内容不切换、滑动后选中态不同步”的排查规则。
- `alignment-pattern.md`：沉淀左对齐、横向滚动、外部 tab bar 布局模式。

### 何时拆成独立 Skill

默认先按 Kit 大领域或组件问题解决大类组织。

只有满足以下条件时，才拆成独立 Skill：

- 某个能力域 FAQ 数量多。
- 触发词稳定且明确。
- 处理逻辑足够独立。
- 该能力会频繁参与代码生成或问题排查。
- 放在大领域 Skill 下会导致入口路由过长或上下文过重。

例如：

```text
arkui-tabs-problem-solving
```

只有在 Tabs 相关 FAQ 覆盖 `TabsController`、`TabContent` 生命周期、自定义 tab bar、嵌套 Tabs、滚动同步、懒加载、动效、状态同步、性能问题等多个方向时，才值得独立成 Skill。

否则应放进：

```text
arkui-component-problem-solving
```

## 推荐的 Skill 内容形态

### 最佳实践 Skill

```text
arkui-state-engineering/
  SKILL.md
  examples/
    redundant-state-before-after.md
    batch-state-update-before-after.md
    decorator-selection-decision-pattern.md
    provide-consume-architecture-pattern.md
    appstorage-splitting-pattern.md
    watch-precision-refresh-before-after.md
    centralized-state-update-template.md
```

主体内容应包含：

- 触发条件。
- 必须执行的工程 pass。
- 状态设计规则。
- 装饰器选择规则。
- 反模式检测。
- 代码生成后质量门禁。

`examples/` 中保留加工后的代码样例、架构模式和决策模式。它们不是原文资料库，而是帮助模型理解和迁移工程模式的样例。

### FAQ Skill

```text
arkui-development/
  SKILL.md
  capabilities/
    component-problem-solving.md
    tabs-problem-solving.md
    list-scroll-problem-solving.md
    navigation-routing.md
  examples/
    tabs/
      custom-tabs-template.md
      switch-sync-diagnosis.md
      alignment-pattern.md
    list/
      lazy-foreach-pattern.md
      scroll-position-diagnosis.md
```

主体内容应包含：

- Kit 大领域触发描述。
- FAQ 能力域路由表。
- 组件/API/问题关键词到 capability 的映射。
- capability 到 examples 的按需加载规则。

FAQ 示例代码应被转化为“可迁移代码模式、诊断样例或 API 组合模式”，而不是作为文档摘录保存。

### examples 的类型

并不是所有样例都要做成 `before / after`。不同来源内容应加工成不同类型的 example。

#### Before / After 型

适合原文中存在明确反例和正例的最佳实践内容。

用于：

- 冗余 `@State`。
- 多次修改同一个状态变量。
- AppStorage 大对象拆分。
- 直接依赖状态导致刷新过多。

文件结构示例：

```markdown
# Redundant State Variable

## Trigger
变量被状态装饰器修饰，但只读、不变或不参与 UI。

## Before
问题代码。

## Problem
为什么有问题。

## After
修正代码。

## Apply
迁移规则。
```

#### Template 型

适合 FAQ 或组件组合模式，没有必要强行构造反例。

例如 Tabs 自定义页签：

```markdown
# Custom Tabs Template

## Trigger
用户需要自定义 Tabs 页签、隐藏默认页签栏、控制页签对齐或滚动。

## Required Parts
- `TabsController`
- `@State selectedIndex`
- 自定义 tab builder
- `controller.changeIndex(index)`
- `Tabs({ controller })`
- `.barHeight(0)`
- `.onContentWillChange(...)`

## Template
可迁移代码模板。

## Apply
替换 tab 数据源、资源名、内容组件和样式。
```

#### Decision Pattern 型

适合装饰器选择、状态共享范围选择。

```markdown
# Decorator Selection Pattern

## Trigger
需要在组件间共享状态。

## Decision
- 父传子只读：`@State` + `@Prop`
- 父子实时双向：`@State` + `@Link`
- 深层对象属性监听：`@Observed` + `@ObjectLink`
- 同一组件树深层共享：`@Provide` + `@Consume`
- 页面级共享：`LocalStorage`
- 应用级共享：`AppStorage`

## Code Shapes
每种选择对应的代码形态。
```

#### Diagnostic 型

适合 FAQ 排错或用户贴出已有代码时的问题定位。

例如 Tabs 点击不切换：

```markdown
# Tabs Switch Diagnosis

## Trigger
用户说 Tabs 点击不切换、选中态不同步、内容区没变化。

## Check Order
1. `TabsController` 是否创建。
2. `Tabs` 是否绑定同一个 controller。
3. 自定义 tab 点击是否调用 `changeIndex(index)`。
4. `selectedIndex` 是否同步。
5. `onContentWillChange` 是否返回 `true`。

## Fix Patterns
常见修复代码形态。
```

### FAQ Skill 如何路由到 examples

`SKILL.md` 不应一次性要求模型读取所有 FAQ examples，而应先路由到能力域，再由能力域选择具体 example。

路由规则的核心是两级映射：

```text
Kit 入口 -> capability
capability -> example
```

Kit 入口示例：

```markdown
## FAQ 能力路由

- Tabs、TabContent、TabsController、自定义页签、隐藏默认 tab bar、页签切换、选中态同步：
  读取 `capabilities/tabs-problem-solving.md`

- List、ListItem、LazyForEach、列表滚动、列表刷新、滚动性能：
  读取 `capabilities/list-scroll-problem-solving.md`

- Navigation、NavPathStack、页面跳转、路由栈、路由状态共享：
  读取 `capabilities/navigation-routing.md`

- Row、Column、Flex、Stack、Grid、布局适配：
  读取 `capabilities/layout-composition.md`
```

能力域示例：

```markdown
## Tabs FAQ 示例路由

- 自定义 tab bar、隐藏默认页签栏、完整自定义 Tabs 实现：
  读取 `examples/tabs/custom-tabs-template.md`

- 点击后内容不切换、滑动后选中态不同步、`TabsController` 不生效：
  读取 `examples/tabs/switch-sync-diagnosis.md`

- 左对齐、横向滚动、自定义 tab bar 布局：
  读取 `examples/tabs/alignment-pattern.md`
```

这样既能保证 Kit 大领域 Skill 被正确加载，又不会把所有 FAQ 样例一次性塞进上下文。

## 原始代码的处理方式

### 代码样例应保留，但要加工

代码样例对代码生成非常重要，应该保留。但保留方式不是完整照搬官方长代码，而是转成帮助模型理解和迁移的工程样例。

处理原则：

```text
保留关键结构，不保留完整文档代码。
保留 before/after，不保留无关 UI 细节。
保留可迁移模板，不保留一次性业务样例。
```

原始代码通常可以分为三类。

#### 反例代码 -> 反模式检测器

例如冗余 `@State` 反例应转成检测规则：

```text
如果变量被 @State 修饰，但：
- 不参与 build 中的 UI 表达式
- 或只读不写
- 或变化不驱动 UI
则判定为冗余状态变量，改成普通成员变量。
```

#### 正例代码 -> 代码生成模板

例如临时变量替代多次状态写入：

```text
当一次事件中需要多次拼接或计算状态时：
- 先用局部变量完成计算
- 最后只赋值一次状态变量
```

#### 完整业务示例 -> 结构模式

例如 AppStorage 拆分 `userData` 和 `collectedIds` 的例子，重点不是业务代码本身，而是结构模式：

```text
不要把低相关字段塞进同一个 AppStorage 对象。
如果 userData.username 和 collectedIds 驱动不同 UI 区域，应拆成不同 key。
```

## 从 Markdown 到 Skill 的加工流程

### 1. 识别文档类型

先判断输入 Markdown 是：

- 最佳实践。
- FAQ。
- API 指南。
- 错误码说明。
- 示例教程。

不同类型文档对应不同 Skill 形态。

### 2. 抽取工程意图

不要只抽取标题和段落，而要抽取：

- 这个段落想防止什么错误。
- 这个反例暴露了什么工程问题。
- 这个正例体现了什么生成规则。
- 这个 FAQ 解决了什么具体故障。
- 这个代码块可以迁移成什么模式。

### 3. 转换为能力单元

每个能力单元包含：

```text
能力名称
触发场景
适用边界
核心规则
示例路由
常见错误
```

### 4. 组织为 Skill 结构

把能力单元组织成可路由的 Skill 结构：

```text
SKILL.md：入口触发和能力路由。
capabilities/*.md：能力域说明、选型规则、约束、example 路由。
examples/*.md：代码模板、before-after、diagnosis、pattern。
```

### 5. 验证 Skill 是否真的改变模型行为

用典型 prompt 测试：

```text
1. 生成一个复杂状态页面，看是否会先设计状态归属。
2. 生成一个自定义 Tabs 页面，看是否会正确使用 TabsController。
3. 给一段错误 Tabs 代码，看是否能按诊断路径定位问题。
4. 给一段滥用 @State 的代码，看是否能指出并修复。
```

如果模型只是复述文档，说明 Skill 仍然偏资料库。

如果模型能主动设计、诊断、修复、自检，说明已经转化成工程能力。

## 结论

最佳实践文档应转化为工程规范、设计判断和质量门禁。

FAQ 文档应转化为问题诊断、修复流程和可迁移代码模式。

两者最终都应服务于鸿蒙代码生成：

```text
最佳实践 Skill 让模型写得更像工程师。
FAQ Skill 让模型解决具体问题更像熟悉鸿蒙组件的人。
```
