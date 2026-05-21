# ArkTS vs TypeScript 关键差异

> ArkTS 基于 TypeScript，但有大量语法和语义限制。
> LLM 最常见的错误就是把 TypeScript 习惯直接带入 ArkTS。
> 本文件列出所有关键差异，每条附带代码示例。

---

## 1. struct vs class — 组件必须用 struct

ArkTS 的 UI 组件只能用 `struct` 声明，不能用 `class`。

```typescript
// ✗ TypeScript 习惯 — 用 class
@Component
class MyComponent {
  build() { ... }
}

// ✓ ArkTS 正确写法 — 用 struct
@Component
struct MyComponent {
  build() { ... }
}
```

**差异要点**：
- `struct` 是值类型，由框架管理生命周期
- `struct` 不能用 `new` 实例化（`new MyComponent()` 编译错误）
- `struct` 不能继承（`struct Child extends Parent` 不允许）
- `struct` 没有 `constructor`，初始化通过声明属性默认值完成

---

## 2. build() 内的特殊规则

`build()` 是 UI 描述函数，不是普通方法。框架会多次调用它来构建/更新 UI 树。

```typescript
// ✗ TypeScript 习惯 — 在 build() 里写逻辑
build() {
  let name = this.user.name        // 不允许声明局部变量
  console.log('rendering')          // 不允许 console.log
  const items = this.list.filter(x => x.active)  // 不允许
  Column() {
    Text(name)
  }
}

// ✓ ArkTS 正确写法 — build() 只描述 UI 树
build() {
  Column() {
    Text(this.getUserName())       // 逻辑封装成方法
    if (this.isLoggedIn) {         // if/else 用于条件渲染
      Text('Welcome')
    }
    ForEach(this.items, (item: ItemType) => {  // ForEach 用于循环渲染
      Text(item.name)
    }, (item: ItemType) => item.id)
  }
}
```

**build() 内允许的控制流**：
- `if / else if / else` — 条件渲染
- `ForEach()` / `LazyForEach()` — 循环渲染

**build() 内禁止的操作**：
- 声明变量（`let`/`const`/`var`）
- `console.log()` / `console.info()`
- 调用异步函数（`await`）
- `for` / `while` / `switch` 循环和分支
- 复杂表达式和计算

---

## 3. 类型系统限制

ArkTS 的类型系统比 TypeScript 严格得多。

```typescript
// ✗ TypeScript 习惯 — 使用 any
let data: any = fetchData()

// ✓ ArkTS — 禁止 any/unknown，必须明确类型
let data: ResponseData = fetchData()
```

```typescript
// ✗ TypeScript 习惯 — 联合类型自由使用
let value: string | number | boolean = getVal()

// ✓ ArkTS — 联合类型受限，简单联合可用，复杂联合需避免
// 推荐使用明确的接口或类替代复杂联合类型
```

```typescript
// ✗ TypeScript 习惯 — 动态属性访问
const key = 'name'
const val = obj[key]

// ✓ ArkTS — 使用类型安全的访问方式
const val = (obj as Record<string, string>)['name']
// 或直接使用 obj.name
```

---

## 4. UI 描述方式 — 不是 JSX

ArkTS 的 UI 不是 JSX/TSX，而是基于链式属性调用的声明式语法。

```typescript
// ✗ React/JSX 习惯
return (
  <div style={{ fontSize: 16, color: '#333' }}>
    <span>Hello</span>
  </div>
)

// ✓ ArkTS — 链式属性调用
Column() {
  Text('Hello')
    .fontSize(16)
    .fontColor('#333')
}
.width('100%')
.padding(16)
```

**关键差异**：
- 没有 `<Component />` 语法，直接调用 `Component() { ... }`
- 属性通过 `.method()` 链式调用设置，不是 `prop={value}`
- 子组件写在 `{ }` 闭包内，不是 `<Parent><Child/></Parent>`
- 事件处理写成 `.onClick(() => { ... })`，不是 `onClick={handler}`

---

## 5. 解构和展开运算符限制

```typescript
// ✗ TypeScript 习惯 — 对象解构
const { name, age } = user

// ✓ ArkTS — 限制使用解构，建议直接访问
const name = user.name
const age = user.age
```

```typescript
// ✗ TypeScript 习惯 — 对象展开
const newUser = { ...user, name: 'newName' }

// ✓ ArkTS — 数组展开可用，对象展开受限
// 对于 @Observed 类，创建新实例替代
const newUser = new UserModel()
newUser.name = 'newName'
newUser.age = user.age
```

**注意**：数组的展开运算符 `[...arr]` 通常可用，但对象展开 `{...obj}` 在某些场景下受限。

---

## 6. 模块导入差异

```typescript
// ✗ TypeScript/Node.js 习惯
import express from 'express'
import { readFile } from 'fs'
import * as path from 'path'

// ✓ ArkTS — 使用 @kit.* 系统模块
import { http } from '@kit.NetworkKit'
import { preferences } from '@kit.ArkData'
import { hilog } from '@kit.PerformanceAnalysisKit'
import { window } from '@kit.ArkUI'
```

ArkTS 没有 Node.js 生态，不能用 npm 包。系统 API 通过 `@kit.*` 导入。

---

## 7. 异步编程差异

```typescript
// ✗ TypeScript 习惯 — Promise.all 随意使用
const [a, b, c] = await Promise.all([fetchA(), fetchB(), fetchC()])

// ✓ ArkTS — async/await 基本可用，但注意：
// 1. build() 中不能使用 await
// 2. 异步操作放在 aboutToAppear() 或事件回调中
aboutToAppear(): void {
  this.loadData()  // 在生命周期中调用异步方法
}

async loadData(): Promise<void> {
  const data = await HttpUtil.get<ResponseType>('/api/data')
  this.items = data.list
}
```

---

## 8. 没有 DOM API

```typescript
// ✗ TypeScript/Web 习惯
document.getElementById('myDiv')
window.localStorage.setItem('key', 'value')
window.addEventListener('resize', handler)

// ✓ ArkTS — 没有 DOM，使用框架 API
// 存储用 Preferences
import { preferences } from '@kit.ArkData'
// 窗口操作用 window 模块
import { window } from '@kit.ArkUI'
// 无需手动操作 DOM，UI 由声明式状态驱动
```

---

## 9. 装饰器是 ArkTS 专有的

ArkTS 使用大量框架专有装饰器，TypeScript 中没有对应物：

| ArkTS 装饰器 | 用途 | TypeScript 中无等价物 |
|---|---|---|
| `@Component` | 声明 UI 组件 | React 用 function/class |
| `@Entry` | 标记入口页面 | 无 |
| `@State` | 组件内响应式状态 | React useState |
| `@Prop` | 父→子单向传递 | React props |
| `@Link` | 父↔子双向同步 | 无直接等价 |
| `@Provide` / `@Consume` | 跨层级注入 | React Context |
| `@Observed` | 可观察类 | MobX observable |
| `@ObjectLink` | 引用可观察对象 | 无直接等价 |
| `@Builder` | 可复用 UI 片段 | React 组件 |
| `@Styles` | 复用属性组合 | CSS class |
| `@Extend` | 扩展组件属性 | 无 |
| `@StorageLink` | 绑定全局存储 | 无 |
| `@Watch` | 监听状态变化 | React useEffect |

---

## 10. 错误处理差异

```typescript
// ✗ TypeScript 习惯 — try/catch 捕获 any
try {
  await doSomething()
} catch (e: any) {
  console.error(e.message)
}

// ✓ ArkTS — 不能用 any
try {
  await doSomething()
} catch (err) {
  // err 类型为 Error 或需要显式转换
  hilog.error(0x0000, 'TAG', 'Error: %{public}s', (err as Error).message)
}
```

---

## 总结速查表

| 特性 | TypeScript | ArkTS |
|---|---|---|
| 组件声明 | `class` | `struct`（不能继承、不能 new） |
| UI 语法 | JSX/TSX | 链式属性调用 |
| build() 规则 | 无限制 | 只能放 UI 描述，禁止逻辑语句 |
| `any` 类型 | 允许 | 禁止 |
| 对象解构 | 自由使用 | 受限 |
| 对象展开 | 自由使用 | 受限 |
| DOM API | 可用 | 不存在 |
| npm 包 | 可用 | 不可用 |
| 模块导入 | `from 'package'` | `from '@kit.*'` |
| 异步 | 自由使用 | build() 内禁止 |
