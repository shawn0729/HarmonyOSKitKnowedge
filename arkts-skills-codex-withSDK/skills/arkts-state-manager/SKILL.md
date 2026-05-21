---
name: arkts-state-manager
description: 生成 ArkTS/HarmonyOS 状态管理代码。当用户需要使用 @State、@Prop、@Link、@Provide/@Consume、@ObjectLink、@Observed、@StorageLink、@StorageProp、@Watch、AppStorage、PersistentStorage、LocalStorage，或需要解决组件间数据通信、全局状态共享、数据持久化、UI 刷新不触发等问题时，务必触发此 skill。即使用户只是说"父子组件传值"或"全局变量"，也应触发。
---

# ArkTS State Manager — 状态管理生成器

## HarmonyOS Kit 知识使用规则

本 skill 的工程实践、迁移步骤和 ownership 以当前 skill 原内容为准。涉及具体 HarmonyOS Kit API、错误码、导入路径、权限、版本兼容、FAQ、最佳实践时，必须读取 `references/harmonyos-sdk/` 下对应 Kit 资料。

先按本 skill 实践确定状态来源、状态传播范围和刷新边界，再按任务场景读取对应 Kit 的 `routing.md` / `guides.md`。API、导入、权限、错误码、版本兼容以 Kit references 和 sources 为准。排障、适配或行为异常必须读取对应 Kit 的 `best-practices-and-faq.md`。当本 skill 原规则与 Kit 资料冲突时，保留工程分层和 ownership，用 Kit 知识修正具体 API 调用。不确定时调用 `arkts-knowledge-verifier`。

### 本 skill 已融合的 Kit

Kit 任务场景覆盖见 `references/harmonyos-sdk/kit-task-scenarios.md`。

- ArkUI：用于组件状态迁移、刷新语义、跨组件数据流和复用场景；入口路径 `references/harmonyos-sdk/arkui/routing.md`。
- ArkData：用于持久化状态、本地配置、数据同步和恢复场景；入口路径 `references/harmonyos-sdk/arkdata/routing.md`。

## API 版本

本 skill 的代码模板基于 **API 12+**（HarmonyOS 5.0.0+）。状态管理在 API 12 有重要变化：

- **@Prop 必须本地初始化**：`@Prop title: string = ''`（API 11 及之前可以不初始化）
- **@Link 传参不再需要 $ 前缀**：`Child({ link: this.parentVar })`（旧写法 `$parentVar` 仍可用但不推荐）
- **新增 @Track 装饰器**（API 12+）：属性级观察，精确控制 UI 刷新
- **新增 @Reusable 装饰器**（API 12+）：配合 LazyForEach 的组件复用优化

生成代码前，先确认用户的目标 API 版本。检查方法：读取 `build-profile.json5` 的 `compatibleSdkVersion` 字段。遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 arkts-knowledge-verifier skill。

---

## 核心原理

ArkTS 的状态管理基于**装饰器驱动的响应式系统**。框架通过装饰器标记需要观察的变量，当变量变化时自动触发 UI 重渲染。理解"哪个装饰器管哪个范围"是避免 bug 的关键。

---

## 状态装饰器选择决策树

```
数据在哪些组件间共享？
│
├─ 只在当前组件内使用
│   └─ @State
│       值类型和 @Observed 类的第一层属性变化会触发刷新
│
├─ 父 → 子 单向传递
│   └─ @Prop
│       子组件拿到副本，修改不影响父组件
│
├─ 父 ↔ 子 双向同步
│   └─ @Link
│       子组件修改会同步回父组件
│
├─ 跨层级（祖先 → 后代）
│   └─ @Provide（祖先）+ @Consume（后代）
│       无需逐层传递，自动向下查找匹配
│
├─ 引用 @Observed 类实例
│   └─ @ObjectLink
│       直接引用父组件的 @Observed 对象，修改同步
│
├─ 全局共享（所有页面）
│   ├─ AppStorage + @StorageLink（双向）
│   └─ AppStorage + @StorageProp（单向）
│
└─ 持久化（应用重启保留）
    └─ PersistentStorage.persistProp()
        底层自动同步到 AppStorage
```

---

## 每种装饰器的标准用法

### @State — 组件内部状态

```typescript
@Component
struct Counter {
  @State count: number = 0  // 必须初始化

  build() {
    Column() {
      Text(`Count: ${this.count}`)
      Button('+1')
        .onClick(() => {
          this.count++  // 触发 UI 刷新
        })
    }
  }
}
```

### @Prop — 父到子单向

```typescript
// 父组件
@Component
struct Parent {
  @State title: string = 'Hello'

  build() {
    Child({ title: this.title })  // 传值
  }
}

// 子组件
@Component
struct Child {
  @Prop title: string = ''  // 接收副本，API 12+ 必须初始化

  build() {
    Text(this.title)
  }
}
```

### @Link — 父子双向

```typescript
// 父组件
@Component
struct Parent {
  @State isOn: boolean = false

  build() {
    Child({ isOn: this.isOn })  // 注意：@Link 传参不加 $
    // API 11 及之前用 $isOn，API 12+ 直接传
  }
}

// 子组件
@Component
struct Child {
  @Link isOn: boolean  // 不初始化，由父组件提供

  build() {
    Toggle({ type: ToggleType.Switch, isOn: this.isOn })
      .onChange((value: boolean) => {
        this.isOn = value  // 修改会同步回父组件
      })
  }
}
```

### @Provide / @Consume — 跨层级

```typescript
@Component
struct Ancestor {
  @Provide('theme') theme: string = 'light'
  build() { Column() { MiddleLayer() } }  // 中间层无需传递
}

@Component
struct Descendant {
  @Consume('theme') theme: string  // 自动匹配祖先的 @Provide
  build() { Text('Theme: ' + this.theme) }
}
```

### @Observed + @ObjectLink — 观察类对象

```typescript
@Observed
class TaskItem {
  id: string = ''
  title: string = ''
  done: boolean = false
}

// 父组件持有 @Observed 数组
@Component
struct TaskList {
  @State tasks: TaskItem[] = []
  build() {
    ForEach(this.tasks, (task: TaskItem) => {
      TaskItemView({ task: task })
    }, (task: TaskItem) => task.id)
  }
}

// 子组件用 @ObjectLink 引用
@Component
struct TaskItemView {
  @ObjectLink task: TaskItem  // 属性变化触发刷新
  build() {
    Row() {
      Text(this.task.title)
      Toggle({ type: ToggleType.Checkbox, isOn: this.task.done })
        .onChange((v: boolean) => { this.task.done = v })
    }
  }
}
```

### @StorageLink / @StorageProp — 全局状态

```typescript
// 1. 在 EntryAbility 中初始化（最早时机）
// EntryAbility.ets
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  AppStorage.setOrCreate('isLoggedIn', false)
  AppStorage.setOrCreate('userName', '')
}

// 2. 在任意组件中使用
@Component
struct ProfilePage {
  @StorageLink('isLoggedIn') isLoggedIn: boolean = false  // 双向
  @StorageProp('userName') userName: string = ''            // 单向

  build() {
    Column() {
      if (this.isLoggedIn) {
        Text('Welcome, ' + this.userName)
      } else {
        Button('Login')
          .onClick(() => {
            this.isLoggedIn = true  // StorageLink 可写，同步到 AppStorage
          })
      }
    }
  }
}
```

### @Watch — 监听变化

```typescript
@Component
struct SearchPage {
  @State @Watch('onKeywordChange') keyword: string = ''

  onKeywordChange(): void {
    this.performSearch(this.keyword)  // keyword 变化时自动调用
  }

  build() {
    TextInput({ placeholder: '搜索...' })
      .onChange((value: string) => { this.keyword = value })
  }
}
```

---

## 触发 UI 刷新的正确方式

这是 ArkTS 状态管理中**最常见的 bug 来源**。框架只能检测到特定类型的变化。

### 规则：框架能观察什么

| 数据类型 | 能观察到的变化 | 不能观察到的变化 |
|---------|-------------|---------------|
| number/string/boolean | 重新赋值 | — |
| 对象（@Observed） | 第一层属性赋值 | 嵌套属性变化 |
| 数组 | 整体重新赋值 | push/splice/下标修改元素属性 |

### 数组更新 — 3 种正确方式

```typescript
@State items: ItemType[] = []

// 方式 1：展开运算符（推荐）
addItem(newItem: ItemType): void {
  this.items = [...this.items, newItem]
}

// 方式 2：slice 创建新数组
removeItem(index: number): void {
  this.items.splice(index, 1)
  this.items = this.items.slice()  // 重新赋值触发刷新
}

// 方式 3：filter/map 返回新数组
toggleAll(): void {
  this.items = this.items.map(item => {
    item.done = true
    return item
  })
}
```

⚠️ `push/splice/下标修改` 不触发刷新，必须重新赋值。

### 嵌套对象更新

`@State` 只观察第一层。`this.user.address.city = 'Beijing'` 不触发刷新。
**解决**：用 `@ObjectLink` 让子组件直接持有嵌套对象，或重新赋值整个对象。

---

## AppStorage 初始化时机

**关键规则**：AppStorage.setOrCreate() 必须在任何 @StorageLink/@StorageProp 使用之前调用。

```
时间线：
EntryAbility.onCreate() → 在这里 setOrCreate ✓
        ↓
Page 组件构造 → @StorageLink 读取值
        ↓
aboutToAppear() → 也可以用 AppStorage API
```

```typescript
// 错误 — 组件已经构造了，但 AppStorage 还没初始化
@Entry
@Component
struct MainPage {
  @StorageLink('token') token: string = ''  // 可能读到默认值而非真实值

  aboutToAppear() {
    AppStorage.setOrCreate('token', 'abc')  // 太晚了
  }
}

// 正确 — 在 EntryAbility 中初始化
export default class EntryAbility extends UIAbility {
  onCreate() {
    AppStorage.setOrCreate('token', '')
  }
}
```

---

## 常见陷阱对照

### 陷阱 1：@Prop 传对象后修改不同步

```typescript
// 错误理解 — 以为 @Prop 是引用传递
@Prop user: UserInfo  // 这是深拷贝！修改不影响父组件

// 正确选择
@Link user: UserInfo       // 需要双向同步时
@ObjectLink user: UserInfo // user 是 @Observed 类时（推荐）
```

### 陷阱 2：@StorageLink key 拼写不一致

```typescript
// 初始化
AppStorage.setOrCreate('isLoggedIn', false)

// 错误 — key 大小写不同
@StorageLink('isLoggedin') isLoggedIn: boolean = false  // 小写 i → 不同的 key！

// 正确 — 完全一致
@StorageLink('isLoggedIn') isLoggedIn: boolean = false
```

**建议**：把所有 AppStorage key 定义为常量。

```typescript
export class StorageKeys {
  static readonly IS_LOGGED_IN = 'isLoggedIn'
  static readonly USER_NAME = 'userName'
}
```

### 持久化双层模式决策树

很多应用需要同时实现"磁盘持久化"和"UI 实时响应"。以下决策树帮助选择正确的方案：

```
数据需要怎样存储和响应？
│
├─ 只在运行时使用，不需持久化
│   └─ AppStorage + @StorageLink/@StorageProp
│       应用退出后数据丢失
│
├─ 需要持久化，但不需要驱动 UI 实时刷新
│   └─ Preferences（通过 PreferencesUtil）
│       直接读写磁盘，UI 在下次读取时获取新值
│
├─ 需要持久化 + UI 实时刷新（最常见）
│   └─ Preferences + AppStorage 双层模式
│       · Preferences 负责磁盘持久化
│       · AppStorage + @StorageLink 负责 UI 实时响应
│       · 修改时同时更新两处
│
└─ 简单类型持久化（重启保留）
    └─ PersistentStorage.persistProp()
        ⚠️ 只支持简单类型（string/number/boolean）
        底层自动同步到 AppStorage
```

**双层模式代码模板**：

```typescript
// 用户修改设置时 → 同时更新 AppStorage + Preferences
async onSettingChanged(key: string, newValue: number): Promise<void> {
  // 1. 更新 AppStorage → @StorageLink 立即刷新 UI
  AppStorage.setOrCreate(key, newValue)

  // 2. 更新 Preferences → 磁盘持久化
  await Config.getInstance().setValue(key, newValue)
}

// 应用启动时 → 从 Preferences 读取，同步到 AppStorage
// （在 GlobalState.init() 中执行）
static syncConfigToAppStorage(config: Config): void {
  AppStorage.setOrCreate('viewType', config.viewType)
  AppStorage.setOrCreate('sortOrder', config.sortOrder)
  AppStorage.setOrCreate('showHidden', config.showHidden)
  // ... 同步所有配置项
}
```

**何时用哪种**：

| 场景 | 方案 | 示例 |
|------|------|------|
| 临时 UI 状态 | `@State` | 加载中状态、弹窗显示 |
| 运行时全局状态 | `AppStorage` | 当前登录用户信息 |
| 用户设置/偏好 | Preferences + AppStorage 双层 | 主题、排序方式、视图类型 |
| 简单 token | `PersistentStorage` | 登录 token（简单字符串）|
| 结构化数据持久化 | RdbStore | 用户收藏、历史记录 |

### 陷阱 3：在 @Builder 中使用状态装饰器

```typescript
// 错误 — @Builder 是函数，不能持有状态
@Builder
function myBuilder() {
  @State count: number = 0  // 编译错误
}

// 正确 — 状态放在 @Component struct 中，@Builder 只接收参数
```

### 陷阱 4：PersistentStorage 存复杂对象

```typescript
// 错误 — PersistentStorage 只支持简单类型
PersistentStorage.persistProp('user', new UserInfo())  // 可能丢失方法

// 正确 — 只持久化简单值
PersistentStorage.persistProp('userId', '')
PersistentStorage.persistProp('theme', 'light')
```

### 陷阱 5：@Watch 回调中修改被监听的变量

```typescript
// 危险 — 可能导致无限循环
@State @Watch('onCountChange') count: number = 0

onCountChange(): void {
  this.count = this.count + 1  // 又触发 onCountChange！
}

// 正确 — @Watch 中只修改其他变量
onCountChange(): void {
  this.displayText = `Count is ${this.count}`
}
```

---

## 生成检查清单

- [ ] 根据数据共享范围选择了正确的装饰器
- [ ] @State 变量已初始化
- [ ] @Link 变量未初始化（由父组件提供）
- [ ] @ObjectLink 对应的类有 @Observed 装饰
- [ ] 数组更新使用重新赋值而非 push/splice
- [ ] AppStorage key 拼写完全一致
- [ ] AppStorage 在 EntryAbility.onCreate() 中初始化
- [ ] @Watch 回调不会修改被监听的变量

---

## 跨 Skill 协作

| 需要什么 | 读取哪里 |
|---------|---------|
| 完整业务功能 | `arkts-pattern-library/SKILL.md` |
| UI 组件配合状态 | `arkts-component-builder/SKILL.md` |
| 数据层（Model + Service） | `arkts-data-layer/SKILL.md` |
| 全局状态 + 导航守卫 | `arkts-navigation-builder/SKILL.md` |

> 完整路由矩阵见 `arkts-knowledge-verifier/references/skill-routing-guide.md`

---

## References

- `references/state-decorators.md` — 所有装饰器的完整语法和边界情况（含 @Track API 12+ 用法）
- `references/update-patterns.md` — 各种数据结构的正确更新模式（数组、Map、嵌套对象）
- `references/global-state.md` — AppStorage/PersistentStorage/Preferences 完整使用模板
- `references/real-world-state-patterns.md` — GlobalState key 注册表、双层持久化、PlaybackController 绑定、EventBus 联动
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 **arkts-knowledge-verifier** skill
