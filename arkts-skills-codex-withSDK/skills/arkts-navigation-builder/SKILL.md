---
name: arkts-navigation-builder
description: 生成 ArkTS/HarmonyOS 页面导航和路由代码。当用户需要实现页面跳转、使用 Navigation 容器、NavPathStack 导航栈、NavDestination 页面注册、Tab 标签导航、底部导航栏、侧边栏导航、@Builder 路由映射、pushPathByName 传参跳转、页面返回传值、路由拦截等功能时，务必触发此 skill。即使用户只说"做个多页面应用"或"页面怎么跳转"，也应触发。
---

# ArkTS Navigation Builder — 导航路由生成器

## HarmonyOS Kit 知识使用规则

本 skill 的工程实践、迁移步骤和 ownership 以当前 skill 原内容为准。涉及具体 HarmonyOS Kit API、错误码、导入路径、权限、版本兼容、FAQ、最佳实践时，必须读取 `references/harmonyos-sdk/` 下对应 Kit 资料。

先按本 skill 实践确定页面结构、导航栈和路由 ownership，再按任务场景读取对应 Kit 的 `routing.md` / `guides.md`。API、导入、权限、错误码、版本兼容以 Kit references 和 sources 为准。排障、适配或行为异常必须读取对应 Kit 的 `best-practices-and-faq.md`。当本 skill 原规则与 Kit 资料冲突时，保留工程分层和 ownership，用 Kit 知识修正具体 API 调用。不确定时调用 `arkts-knowledge-verifier`。

### 本 skill 已融合的 Kit

Kit 任务场景覆盖见 `references/harmonyos-sdk/kit-task-scenarios.md`。

- ArkUI：用于应用内页面栈、标签页、路由参数和页面容器迁移；入口路径 `references/harmonyos-sdk/arkui/routing.md`。
- Ability Kit：用于跨应用跳转、能力启动、返回链路和系统级导航协作；入口路径 `references/harmonyos-sdk/ability-kit/routing.md`。

## API 版本

本 skill 的代码模板基于 **API 12+**（HarmonyOS 5.0.0+）。

> **重要**：`@ohos.router` 在 API 12+ 已废弃。所有新项目必须使用 `Navigation` + `NavPathStack` 进行页面导航。如果用户的现有代码使用 router，应引导其迁移到 Navigation 方案。迁移详细步骤参阅 arkts-knowledge-verifier skill。

- 使用 `Navigation` + `NavPathStack`（不要用 `@ohos.router`）
- 使用 `@kit.*` 导入
- 生成代码前，先确认用户的目标 API 版本（读 `build-profile.json5` 的 `compatibleSdkVersion`）

---

## 导航方案选择

ArkTS 有两种主要导航模式，根据应用类型选择：

```
你的应用需要什么导航？
│
├─ 底部 Tab 切换（如微信/淘宝主页）
│   └─ Tabs + TabContent
│       适合：3-5 个平级主要功能入口
│
└─ 页面跳转（列表→详情、登录→首页）
    └─ Navigation + NavPathStack + NavDestination
        适合：层级式页面导航
        │
        ├─ 手机端 → mode: NavigationMode.Stack（栈模式）
        ├─ 平板端 → mode: NavigationMode.Split（分栏模式）
        └─ 自适应 → mode: NavigationMode.Auto
```

---

## 方案 1：Navigation + NavPathStack（页面跳转）

这是 HarmonyOS **API 12+** 推荐的页面导航方案，`@ohos.router` 已废弃。

### 标准入口模板

```typescript
@Entry
@Component
struct MainPage {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack()

  // 路由映射：页面名称 → 页面 Builder
  @Builder
  pageMap(name: string, param?: object) {
    if (name === 'DetailPage') {
      DetailPage()
    } else if (name === 'SettingsPage') {
      SettingsPage()
    }
  }

  build() {
    Navigation(this.navPathStack) {
      // 首页内容
      Column() {
        Text('首页')
          .fontSize(24)
        Button('进入详情')
          .onClick(() => {
            this.navPathStack.pushPathByName('DetailPage', { id: '123' })
          })
      }
    }
    .navDestination(this.pageMap)
    .title('我的应用')
    .mode(NavigationMode.Stack)
  }
}
```

### pageMap 自动生成规则（迁移项目专用）

当存在 `spec/baseline/ui-manifest.md` 时，pageMap 的 if-else 路由表**必须**从 ui-manifest.md 的页面清单自动生成，不要手动编写。

**生成方法：**
1. 读取 ui-manifest.md 的页面清单表
2. 提取所有 "ArkTS 产出" 列的页面名
3. 为每个页面生成一个 if 分支
4. 参数统一通过 NavDestination.onReady(context) 接收，不使用 wrapper component 中转

**生成结果示例：**
```typescript
@Builder
pageMap(name: string, param?: object) {
  // 自动从 ui-manifest.md 生成，不要手动编写
  if (name === 'HomePage') { HomePage() }
  else if (name === 'FeedDetailPage') { FeedDetailPage() }
  else if (name === 'EpisodeDetailPage') { EpisodeDetailPage() }
  else if (name === 'SearchPage') { SearchPage() }
  else if (name === 'DownloadsPage') { DownloadsPage() }
  else if (name === 'SettingsPage') { SettingsPage() }
  // ... 全部页面，不遗漏
}
```

**参数传递标准模式（禁止 wrapper component）：**
```typescript
// 跳转时传参
this.navPathStack.pushPathByName('FeedDetailPage', { 'feedId': feedId } as Record<string, string>)

// 接收参数（在 NavDestination 的 onReady 中）
NavDestination() {
  // 页面内容
}
.onReady((context: NavDestinationContext) => {
  const param = context.pathInfo.param as Record<string, string>
  this.feedId = param?.feedId ?? ''
})
```

**禁止的模式（wrapper component 传参 — 容易遗漏参数转发）：**
```typescript
// ❌ 不要这样做
@Component struct FeedDetailPageContent {
  build() {
    FeedDetailPage({ feedId: this.feedId })  // 容易忘记传参
  }
}
```

### NavDestination 页面模板

```typescript
@Component
struct DetailPage {
  @Consume('navPathStack') navPathStack: NavPathStack
  @State itemId: string = ''

  build() {
    NavDestination() {
      Column() {
        Text('详情页 ID: ' + this.itemId)
        Button('返回')
          .onClick(() => {
            this.navPathStack.pop()
          })
      }
    }
    .title('详情')
    .onReady((context: NavDestinationContext) => {
      // 接收跳转参数
      let param = context.pathInfo.param as Record<string, string>
      this.itemId = param?.id ?? ''
    })
  }
}
```

### 跳转操作速查

```typescript
// 前进
navPathStack.pushPathByName('PageName', { key: 'value' })

// 返回
navPathStack.pop()                    // 返回上一页
navPathStack.popToName('PageName')    // 返回到指定页面
navPathStack.clear()                  // 清空栈，回到根页面

// 替换当前页
navPathStack.replacePath({ name: 'NewPage', param: {} })

// 获取栈信息
navPathStack.size()                   // 栈深度
navPathStack.getAllPathName()         // 所有页面名称
```

### 用 @Provide/@Consume 注入 NavPathStack

**为什么这样做**：子页面需要 NavPathStack 来执行跳转/返回操作，但 NavPathStack 只在入口页面创建。使用 @Provide/@Consume 让所有子页面都能访问，无需逐层传递。

```typescript
// 入口页面
@Entry
@Component
struct MainPage {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack()
  // ...
}

// 任意子页面
@Component
struct AnyChildPage {
  @Consume('navPathStack') navPathStack: NavPathStack

  build() {
    NavDestination() {
      Button('跳转到其他页面')
        .onClick(() => {
          this.navPathStack.pushPathByName('OtherPage', {})
        })
    }
  }
}
```

---

## 方案 2：动态路由注册（推荐用于大型项目）

当页面较多时，用 `if-else` 映射不可维护。使用 `WrappedBuilder` 动态注册：

```typescript
// 1. 定义路由注册表（单独文件）
// router/RouteMap.ets
export class RouteMap {
  private static builders: Map<string, WrappedBuilder<[object]>> = new Map()

  static register(name: string, builder: WrappedBuilder<[object]>): void {
    RouteMap.builders.set(name, builder)
  }

  static getBuilder(name: string): WrappedBuilder<[object]> | undefined {
    return RouteMap.builders.get(name)
  }
}

// 2. 各页面自注册
// pages/DetailPage.ets
@Builder
function DetailPageBuilder(param: object) {
  DetailPage()
}

// 在模块加载时注册
const _reg = (() => {
  RouteMap.register('DetailPage', wrapBuilder(DetailPageBuilder))
})()

// 3. 入口页面使用动态路由
@Entry
@Component
struct MainPage {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack()

  @Builder
  pageMap(name: string, param?: object) {
    // 动态获取 Builder
    RouteMap.getBuilder(name)?.builder(param ?? {})
  }

  build() {
    Navigation(this.navPathStack) {
      // 首页内容
    }
    .navDestination(this.pageMap)
    .mode(NavigationMode.Stack)
  }
}
```

---

## 方案 3：Tabs + TabContent（底部导航）

### 标准底部导航模板

```typescript
@Entry
@Component
struct MainTabsPage {
  @State currentIndex: number = 0

  private tabItems: TabItem[] = [
    { title: '首页', icon: $r('app.media.ic_home'), selectedIcon: $r('app.media.ic_home_selected') },
    { title: '发现', icon: $r('app.media.ic_discover'), selectedIcon: $r('app.media.ic_discover_selected') },
    { title: '消息', icon: $r('app.media.ic_message'), selectedIcon: $r('app.media.ic_message_selected') },
    { title: '我的', icon: $r('app.media.ic_mine'), selectedIcon: $r('app.media.ic_mine_selected') }
  ]

  @Builder
  tabBuilder(item: TabItem, index: number) {
    Column() {
      Image(this.currentIndex === index ? item.selectedIcon : item.icon)
        .width(24)
        .height(24)
      Text(item.title)
        .fontSize(10)
        .fontColor(this.currentIndex === index ? '#007DFF' : '#999')
        .margin({ top: 4 })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }

  build() {
    Tabs({ barPosition: BarPosition.End, index: this.currentIndex }) {
      TabContent() {
        HomePage()
      }
      .tabBar(this.tabBuilder(this.tabItems[0], 0))

      TabContent() {
        DiscoverPage()
      }
      .tabBar(this.tabBuilder(this.tabItems[1], 1))

      TabContent() {
        MessagePage()
      }
      .tabBar(this.tabBuilder(this.tabItems[2], 2))

      TabContent() {
        MinePage()
      }
      .tabBar(this.tabBuilder(this.tabItems[3], 3))
    }
    .barHeight(56)
    .scrollable(false)
    .onChange((index: number) => {
      this.currentIndex = index
    })
  }
}

interface TabItem {
  title: string
  icon: Resource
  selectedIcon: Resource
}
```

---

## Tabs + Navigation 组合模式

大多数应用同时需要 Tab 切换和页面跳转。标准做法：**外层 Tabs，每个 Tab 内嵌 Navigation**。

```typescript
@Entry
@Component
struct MainPage {
  @State currentIndex: number = 0
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack()

  @Builder
  pageMap(name: string, param?: object) {
    if (name === 'DetailPage') {
      DetailPage()
    }
  }

  build() {
    Tabs({ barPosition: BarPosition.End }) {
      TabContent() {
        Navigation(this.navPathStack) {
          HomePage()
        }
        .navDestination(this.pageMap)
        .mode(NavigationMode.Stack)
        .hideTitleBar(true)
      }
      .tabBar('首页')

      TabContent() {
        MinePage()
      }
      .tabBar('我的')
    }
    .scrollable(false)
  }
}
```

---

## Navigation 模式选择

```typescript
// Stack 模式 — 手机端，全屏切换
.mode(NavigationMode.Stack)

// Split 模式 — 平板端，左侧列表 + 右侧详情
.mode(NavigationMode.Split)
.navBarWidth('40%')  // 左侧宽度

// Auto 模式 — 根据屏幕宽度自动切换
.mode(NavigationMode.Auto)
// 宽度 >= 600vp 时用 Split，否则用 Stack
```

---

## 常见错误 vs 正确写法

### 错误 1：使用 router 而非 Navigation

```typescript
// 废弃（API 12+）— @ohos.router 已废弃，不要在新项目中使用
import router from '@ohos.router'
router.pushUrl({ url: 'pages/Detail' })

// 正确（API 12+）— 使用 Navigation + NavPathStack
this.navPathStack.pushPathByName('DetailPage', params)
```

**为什么**：`@ohos.router` 在 API 12+ 已正式废弃。Navigation 支持更丰富的转场动画、状态管理和多设备适配（Stack/Split/Auto 模式）。迁移步骤参阅 arkts-knowledge-verifier skill。

### 错误 2：NavDestination 没有接收参数

```typescript
// 错误 — 忘记 onReady
@Component
struct DetailPage {
  @State id: string = ''

  build() {
    NavDestination() {
      Text('ID: ' + this.id)  // 永远是空字符串
    }
  }
}

// 正确 — 在 onReady 中获取参数
build() {
  NavDestination() {
    Text('ID: ' + this.id)
  }
  .onReady((context: NavDestinationContext) => {
    let param = context.pathInfo.param as Record<string, string>
    this.id = param?.id ?? ''
  })
}
```

### 错误 3：Tabs onChange 不更新 index

```typescript
// 错误 — 点击 Tab 后不更新 currentIndex
Tabs({ barPosition: BarPosition.End }) { ... }
// 忘记添加 .onChange

// 正确
Tabs({ barPosition: BarPosition.End, index: this.currentIndex }) { ... }
  .onChange((index: number) => {
    this.currentIndex = index
  })
```

### 错误 4：Navigation 不设置 mode

```typescript
// 不指定 mode 可能在平板上出现意外的 Split 布局
Navigation(this.navPathStack) { ... }

// 明确指定
Navigation(this.navPathStack) { ... }
  .mode(NavigationMode.Stack)  // 或 Split / Auto
```

---

## 生成检查清单

- [ ] 选择了合适的导航方案（Tabs / Navigation / 组合）
- [ ] Navigation 有明确的 mode 设置
- [ ] NavPathStack 通过 @Provide/@Consume 注入
- [ ] NavDestination 在 onReady 中接收参数
- [ ] 页面 Builder 在 navDestination 中正确映射
- [ ] Tabs 设置了 onChange 回调更新 currentIndex
- [ ] 返回操作使用 navPathStack.pop()

---

## 跨 Skill 协作

当用户需求超出纯导航范围时，读取以下 skill 的内容来补充：

| 需要什么 | 读取哪里 |
|---------|---------|
| 完整业务功能（列表详情页需要导航+数据+UI） | `arkts-pattern-library/SKILL.md` — 它有编排协议引导完整流程 |
| 列表页 UI 组件（List + ForEach + 卡片） | `arkts-component-builder/SKILL.md` |
| 数据模型和网络请求 | `arkts-data-layer/SKILL.md` |
| 全局状态（登录状态驱动导航守卫） | `arkts-state-manager/references/global-state.md` |
| 页面转场动画 | `arkts-animation-builder/SKILL.md`"transition"节 |

> 完整路由矩阵见 `arkts-knowledge-verifier/references/skill-routing-guide.md`

---

## References

- `references/nav-patterns.md` — 完整导航模板（从 hmosworld 提取的多模块导航方案）
- `references/tab-navigation.md` — 自定义 TabBar 完整实现，含图标切换动画
- `references/advanced-nav-patterns.md` — 路由参数类、routerMap @Builder、FullPlayer 隐藏 Tab、onReady 参数、路由常量
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 **arkts-knowledge-verifier** skill
