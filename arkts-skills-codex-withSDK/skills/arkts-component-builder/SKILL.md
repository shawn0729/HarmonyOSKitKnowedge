---
name: arkts-component-builder
description: 生成 ArkTS/HarmonyOS 声明式 UI 组件代码。当用户需要创建页面、编写组件、设计布局、使用 Column/Row/Stack/Grid/List/Flex 布局容器、创建自定义组件、使用 @Builder/@Styles/@Extend 装饰器、编写 ForEach/LazyForEach 列表、处理响应式断点适配、实现卡片/列表/表单/弹窗等常见 UI 元素、或生成任何 .ets UI 代码时，务必触发此 skill。即使用户只是说"帮我写个页面"或"做个界面"，也应触发。如果用户需要的是完整业务功能（如搜索、登录、列表详情页），应优先触发 arkts-pattern-library。
---

# ArkTS Component Builder — UI 组件生成器

## HarmonyOS Kit 知识使用规则

本 skill 的工程实践、迁移步骤和 ownership 以当前 skill 原内容为准。涉及具体 HarmonyOS Kit API、错误码、导入路径、权限、版本兼容、FAQ、最佳实践时，必须读取 `references/harmonyos-sdk/` 下对应 Kit 资料。

先按本 skill 实践确定组件结构、布局分层和代码生成边界，再按任务场景读取对应 Kit 的 `routing.md` / `guides.md`。API、导入、权限、错误码、版本兼容以 Kit references 和 sources 为准。排障、适配或行为异常必须读取对应 Kit 的 `best-practices-and-faq.md`。当本 skill 原规则与 Kit 资料冲突时，保留工程分层和 ownership，用 Kit 知识修正具体 API 调用。不确定时调用 `arkts-knowledge-verifier`。

### 本 skill 已融合的 Kit

Kit 任务场景覆盖见 `references/harmonyos-sdk/kit-task-scenarios.md`。

- ArkUI：用于组件迁移、布局构建、列表渲染、样式表达和组件复用；入口路径 `references/harmonyos-sdk/arkui/routing.md`。

## API 版本

本 skill 的代码模板基于 **API 12+**（HarmonyOS 5.0.0+）。生成代码前，先确认用户的目标 API 版本。检查方法：读取项目的 `build-profile.json5` 中的 `compatibleSdkVersion` 字段，括号内的数字就是 API 级别。

- 使用 `@kit.*` 导入（不要用 `@ohos.*`）
- 使用 Navigation 导航（不要用 @ohos.router）
- @Prop 必须初始化默认值
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 arkts-knowledge-verifier skill

---

## 输入模式

### 模式 A: 描述驱动（默认）

输入: 文字描述 + 可选 design tokens
输出: ArkTS 组件代码
适用: 新建轨、无 Android 参考的组件

### 模式 B: Android 源码参照（精细迁移）

输入:
  - android_layout: XML 布局文件路径（必须）— Agent 必须先 Read 此文件
  - android_class: Java/Kotlin 类文件路径（必须）— Agent 必须先 Read 此文件
  - design_tokens: 共享样式常量路径（可选）— 来自 ui-framework Task 的产出

执行规则:
  1. **先读后写**: 必须先 Read android_layout 和 android_class 的完整内容，禁止跳过
  2. **提取属性**: 从 XML 中提取所有 View 及其属性（尺寸、间距、颜色、字号、圆角、阴影、可见性）
  3. **组件映射**: 按以下对照表逐组件转写:
     - FrameLayout → Stack
     - LinearLayout (vertical) → Column
     - LinearLayout (horizontal) → Row
     - RelativeLayout / ConstraintLayout → RelativeContainer 或 Column+Row 组合
     - RecyclerView (horizontal) → List({ listDirection: Axis.Horizontal })
     - RecyclerView (vertical) → List + LazyForEach
     - CardView → Column + .borderRadius() + .shadow()
     - ImageView → Image
     - TextView → Text
     - ProgressBar (linear) → Progress({ type: ProgressType.Linear })
     - ProgressBar (circular) → Progress({ type: ProgressType.Ring })
     - SwipeRefreshLayout → Refresh
  4. **属性转换**: dp → vp (1:1), sp → fp (1:1), 颜色值直接复制, match_parent → '100%', wrap_content → 默认
  5. **共享 tokens**: 如提供 design_tokens 路径，必须使用其中定义的常量而非硬编码
  6. **交互保持**: onClick → .onClick(), onLongClick → LongPressGesture, SwipeAction 保留

### SymbolGlyph 图标预验证

生成 UI 代码前，如果需要使用系统图标：
1. 读取 arkts-knowledge-verifier/references/verified-symbols.md 获取已验证名称列表
2. 只使用列表中的名称，不要猜测或创造新名称
3. 如果 Android 对应图标在验证列表中找不到等价物，使用最接近的替代或使用自定义图片资源

已知不存在的常见名称: music_note (用 music), doc_on_doc (用 list_bullet), copy (用 checkmark), tray_fill (用 envelope), square_and_arrow_up (用 share)

适用: 精细迁移轨（轨道 0）的页面框架和组件生成

触发判断: 当 task 包含 android_layout 或 android_source 字段时，自动使用模式 B

---

## 核心约束

ArkTS 的声明式 UI 与 React/Flutter 表面相似，但有本质差异。以下约束是 LLM 最容易忽略的：

### 1. struct 不是 class

```typescript
// 错误 — LLM 常犯：把 @Component 写成 class
@Component
class MyComponent { ... }

// 正确 — 必须用 struct
@Component
struct MyComponent {
  build() { ... }
}
```

**为什么**：ArkTS 的 @Component 只能装饰 struct。struct 是值类型，由框架管理生命周期，不能用 new 实例化。

### 2. build() 内只放 UI 描述，不放逻辑语句

```typescript
// 错误 — build() 里写了 if-let、变量声明、console.log
build() {
  let name = this.user.name  // 不允许
  console.log('rendering')    // 不允许
  Column() {
    Text(name)
  }
}

// 正确 — 逻辑写成方法或计算属性，build() 只描述 UI 树
build() {
  Column() {
    Text(this.getUserName())
    if (this.isLoggedIn) {  // if 可以用于条件渲染
      Text('Welcome')
    }
  }
}
```

**为什么**：build() 是 UI 描述函数，框架会多次调用它来重建 UI 树。只有条件渲染（if/else）和循环渲染（ForEach）是允许的控制流。

### 3. 单根节点规则

```typescript
// 错误 — 多个根节点
build() {
  Text('Hello')
  Text('World')
}

// 正确 — 单个根容器
build() {
  Column() {
    Text('Hello')
    Text('World')
  }
}
```

### 4. 链式属性调用

```typescript
// ArkTS 属性是在组件后面链式调用的
Text('Hello')
  .fontSize(16)
  .fontColor('#333')
  .fontWeight(FontWeight.Bold)
  .margin({ top: 8 })
```

---

## 标准组件骨架

生成任何组件时，使用此骨架：

```typescript
@Component
struct ComponentName {
  // 1. 状态声明
  @State private count: number = 0

  // 2. 生命周期（如需要）
  // 默认数据加载模板（禁止使用 loadMockData）
  async aboutToAppear(): Promise<void> {
    try {
      // 调用真实 Service/DBReader 方法
      this.dataList = await DBReader.getXxxList()
    } catch (e) {
      // 兜底: 空数组或默认值
      this.dataList = []
    }
  }

  // 3. @Builder 抽取复杂子 UI
  @Builder
  itemBuilder(item: ItemType) {
    Row() {
      Text(item.title)
        .fontSize(16)
    }
    .padding(12)
  }

  // 4. build() — 只有 UI 描述
  build() {
    Column() {
      // UI 树
    }
    .width('100%')
    .height('100%')
  }
}
```

**入口页面**额外加 `@Entry`：
```typescript
@Entry
@Component
struct IndexPage {
  build() {
    Column() { ... }
  }
}
```

---

## 布局选型决策树

根据 UI 需求选择容器：

```
需要什么布局？
│
├─ 垂直排列子元素 → Column
├─ 水平排列子元素 → Row
├─ 子元素重叠/覆盖 → Stack
├─ 等间距均分空间 → Flex（配合 justifyContent）
├─ 固定行列的网格 → Grid + GridItem
│   └─ columnsTemplate: '1fr 1fr 1fr'（3列等宽）
├─ 滚动长列表 → List + ListItem
│   ├─ <20 项 → ForEach
│   └─ ≥20 项 → LazyForEach + IDataSource
└─ 轮播/翻页 → Swiper
```

### 常用布局属性速查

```typescript
// Column/Row 主轴与交叉轴
Column() { ... }
  .justifyContent(FlexAlign.Center)    // 主轴居中
  .alignItems(HorizontalAlign.Start)   // 交叉轴左对齐

Row() { ... }
  .justifyContent(FlexAlign.SpaceBetween) // 两端对齐
  .alignItems(VerticalAlign.Center)       // 垂直居中

// 通用尺寸
.width('100%')
.height(200)
.padding({ left: 16, right: 16 })
.margin({ top: 12 })

// Stack 对齐
Stack({ alignContent: Alignment.BottomEnd }) { ... }

// Grid 模板
Grid() { ... }
  .columnsTemplate('1fr 1fr')        // 2列等宽
  .rowsGap(12)
  .columnsGap(12)
```

---

## @Builder / @Styles / @Extend 复用

### @Builder — 抽取可复用 UI 片段

当一个 UI 片段在 build() 中出现 2+ 次，或超过 10 行时，抽取为 @Builder：

```typescript
// 组件内 @Builder
@Builder
cardItem(title: string, desc: string) {
  Column() {
    Text(title).fontSize(18).fontWeight(FontWeight.Bold)
    Text(desc).fontSize(14).fontColor('#666')
  }
  .padding(16)
  .borderRadius(12)
  .backgroundColor(Color.White)
}

// build() 中使用
build() {
  Column() {
    this.cardItem('标题1', '描述1')
    this.cardItem('标题2', '描述2')
  }
}
```

### @Styles — 复用属性组合

```typescript
// 定义（组件外部全局或组件内部）
@Styles function cardStyle() {
  .padding(16)
  .borderRadius(12)
  .backgroundColor(Color.White)
  .shadow({ radius: 4, color: '#1A000000' })
}

// 使用
Column() { ... }
  .cardStyle()
```

### @Extend — 扩展特定组件

```typescript
// 只能扩展指定组件类型
@Extend(Text)
function titleText() {
  .fontSize(20)
  .fontWeight(FontWeight.Bold)
  .fontColor('#222')
}

// 使用
Text('Hello').titleText()
```

---

## ForEach vs LazyForEach

### ForEach — 少量数据（<20 项）

```typescript
ForEach(this.items, (item: ItemType, index: number) => {
  ListItem() {
    this.itemBuilder(item)
  }
}, (item: ItemType) => item.id.toString())  // 必须提供 keyGenerator
```

**keyGenerator 必须返回唯一字符串，且必须包含会变化的字段**。ForEach 通过 key 判断是否需要重建子组件，key 不变则复用旧组件（即使数据已变）。

```typescript
// 错误：只用 id，当 name/favorite 变化时 UI 不刷新
(item: ItemType) => item.id.toString()

// 正确：包含变化字段，数据变化时 key 也变 → 触发组件重建
(item: ItemType) => `${item.id}_${item.name}_${item.modified}`
```

### LazyForEach — 大量数据（≥20 项）

```typescript
// 需要实现 IDataSource
LazyForEach(this.dataSource, (item: ItemType) => {
  ListItem() {
    this.itemBuilder(item)
  }
}, (item: ItemType) => item.id.toString())
```

**为什么**：LazyForEach 只渲染可见区域的子组件，大幅减少内存和渲染开销。配合 `cachedCount` 预加载。

---

## 资源引用规范

```typescript
// 引用 resources/ 下的资源，不要硬编码字符串
Text($r('app.string.title'))           // 字符串
Image($r('app.media.icon_home'))       // 图片
.backgroundColor($r('app.color.bg'))   // 颜色

// rawfile 资源
Image($rawfile('images/banner.png'))
```

---

## 常见错误 vs 正确写法

### 错误 1：在 build() 中调用异步函数

```typescript
// 错误
build() {
  Column() {
    await this.loadData()  // build() 不能 async
  }
}

// 正确 — 在生命周期中加载
aboutToAppear(): void {
  this.loadData()
}
```

### 错误 2：组件属性顺序错误

```typescript
// 错误 — 事件必须在属性前面？不，但某些布局属性有顺序要求
// 实际上链式调用顺序无严格限制，但建议保持一致

// 推荐顺序：尺寸 → 布局 → 外观 → 交互
Text('Hello')
  .width('100%')                    // 尺寸
  .padding(16)                      // 布局
  .fontSize(16)                     // 外观
  .fontColor('#333')
  .backgroundColor(Color.White)
  .borderRadius(8)
  .onClick(() => { ... })           // 交互
```

### 错误 3：忘记 ListItem 包裹

```typescript
// 错误 — List 的直接子组件必须是 ListItem
List() {
  ForEach(this.items, (item) => {
    Text(item.name)  // 直接放 Text 会报错
  })
}

// 正确
List() {
  ForEach(this.items, (item) => {
    ListItem() {
      Text(item.name)
    }
  }, (item) => item.id)
}
```

### 错误 4：Grid 没有 GridItem

```typescript
// 错误
Grid() {
  ForEach(this.items, (item) => {
    Column() { ... }  // 必须用 GridItem 包裹
  })
}

// 正确
Grid() {
  ForEach(this.items, (item) => {
    GridItem() {
      Column() { ... }
    }
  }, (item) => item.id)
}
```

### 错误 5：@Builder 参数传递错误

```typescript
// 错误 — @Builder 中直接修改状态
@Builder
itemView(item: ItemType) {
  Text(item.name)
    .onClick(() => {
      item.selected = true  // 不会触发 UI 更新
    })
}

// 正确 — 通过回调或修改 @State 变量
@Builder
itemView(item: ItemType, onSelect: () => void) {
  Text(item.name)
    .onClick(() => onSelect())
}
```

---

## 生成检查清单

生成 UI 代码后，逐项检查：

- [ ] 使用 `@Component struct`（不是 class）
- [ ] `build()` 内只有 UI 描述，无变量声明和 console.log
- [ ] 单根节点
- [ ] ForEach/LazyForEach 提供了 keyGenerator
- [ ] List 内用 ListItem 包裹，Grid 内用 GridItem 包裹
- [ ] 字符串和图片使用 $r() 资源引用（如适用）
- [ ] 属性使用链式调用语法
- [ ] 数据加载在 aboutToAppear() 中而非 build() 中
- [ ] @Builder 方法在 build() 中通过 `this.xxx()` 调用
- [ ] 事件回调按三级策略生成（L1/L2/L3），无空注释回调
- [ ] @Prop / @State / @Link 变量名不在禁用列表中（参考 references/prop-naming-rules.md）
- [ ] 所有用户可见文本使用 $r('app.string.xxx')，禁止硬编码中文/英文（纯数字、标点、格式占位符除外）
- [ ] aboutToAppear() 中使用 DBReader/Service 真实调用 + try-catch 空数组兜底，不使用 loadMockData()
- [ ] 所有 $r('sys.symbol.xxx') 图标名称已在 arkts-knowledge-verifier/references/verified-symbols.md 中确认存在

---

## 回调生成规则（三级策略）

生成 UI 组件中的事件回调（onClick、onPlayClick、onAddToQueue 等）时，**必须按以下三级策略生成**，禁止留空注释：

### 判断流程

```
生成回调代码前:
  │
  ├─ Step 1: Grep 项目中是否存在对应 Controller/Manager/DAO
  │   例: grep -rn "class PlaybackController" entry/src/
  │
  ├─ 存在 → L1 完整接线
  ├─ 不存在但项目有 EventBus/emitter → L2 事件桥接
  └─ 都不满足 → L3 签名占位符
```

### 三级策略

| 级别 | 条件 | 生成内容 | 示例 |
|------|------|---------|------|
| **L1 完整接线** | Controller/Manager/DAO 已存在于项目中 | 直接调用真实方法 | `PlaybackController.getInstance().play(item.getMedia())` |
| **L2 事件桥接** | Controller 未就绪但 EventBus/emitter 已配置 | 发射事件 + 留接收端 TODO | `emitter.emit('PLAY_MEDIA', { itemId: item.id })` |
| **L3 签名占位符** | 以上都不满足 | console.info 占位符 + 自动注册到 placeholder-registry | `console.info('TODO:PLAY_MEDIA:FeedDetailComponent')` |

### 关键约束

1. **禁止空注释回调**: `onClick: () => { /* Start playback */ }` 是**被禁止的**。这种回调用户无法发现问题（不报错、不可 grep），是 BF-001 类缺陷的根源。
2. **L3 格式强制**: 占位符必须用 `console.info('TODO:<ACTION>:<COMPONENT>')` 格式，以便 grep 扫描发现。
3. **自动注册**: 每个 L3 占位符必须追加到 `spec/placeholder-registry.md`，格式：
   ```
   | PH-xxx | 文件路径 | 行号 | function | <ACTION> in <COMPONENT> | 对应 Controller | pending |
   ```
4. **扫描先行**: 生成回调前 MUST grep 项目，不能假设 Controller 不存在。

### 示例对比

```typescript
// 被禁止 — 空注释回调（BF-001 根源）
Button('Play')
  .onClick(() => {
    // Start playback
  })

// L1 — Controller 存在时
Button('Play')
  .onClick(() => {
    PlaybackController.getInstance().playMedia(this.item.getMedia())
  })

// L2 — 有 EventBus 但无 Controller
Button('Play')
  .onClick(() => {
    emitter.emit({ eventId: EventIds.PLAY_MEDIA }, { data: { itemId: this.item.id } })
  })

// L3 — 占位符（同时注册到 placeholder-registry）
Button('Play')
  .onClick(() => {
    console.info('TODO:PLAY_MEDIA:EpisodeItemBuilder')
  })
```

---

## 跨 Skill 协作

当用户需求超出纯 UI 范围时，读取以下 skill 的内容来补充：

| 需要什么 | 读取哪里 |
|---------|---------|
| 完整业务功能（列表详情、搜索、登录等） | `arkts-pattern-library/SKILL.md` — 它有编排协议引导完整流程 |
| 列表数据源（LazyForEach + IDataSource） | `arkts-data-layer/references/datasource-patterns.md` |
| 页面导航（Navigation + NavDestination） | `arkts-navigation-builder/SKILL.md` |
| 状态管理（@State/@Link/@Provide 选择） | `arkts-state-manager/SKILL.md` 决策树 |
| 动画效果（animateTo/transition） | `arkts-animation-builder/SKILL.md` |
| 媒体播放 | `arkts-media-playback/SKILL.md` |
| 文件下载 | `arkts-download-manager/SKILL.md` |
| Android UI 对齐 | `arkts-ui-alignment/SKILL.md` |

> 完整路由矩阵见 `arkts-knowledge-verifier/references/skill-routing-guide.md`

---

## References

当需要更详细的模板和示例时，查阅以下参考文件：

- `references/layout-patterns.md` — 6 种布局容器的完整模板与适用场景
- `references/common-components.md` — Text/Image/Button/TextInput/Swiper/Tabs/Search 等常用组件的属性速查
- `references/responsive-design.md` — 响应式断点设计和折叠屏适配完整方案
- `references/media-app-components.md` — 媒体应用组件：MiniPlayer、自定义 Tab 栏、封面 fallback、空状态
- `references/component-lifecycle-patterns.md` — 组件生命周期：EventBus 订阅、ViewModel 加载、ForEach key
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 **arkts-knowledge-verifier** skill
