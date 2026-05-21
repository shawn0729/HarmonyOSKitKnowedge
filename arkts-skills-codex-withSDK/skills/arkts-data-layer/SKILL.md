---
name: arkts-data-layer
description: 生成 ArkTS/HarmonyOS 数据层代码。当用户需要创建数据模型、网络请求服务、IDataSource 数据源、LazyDataSource、BasicDataSource 实现、EventHub 事件通信、HTTP 请求、Promise/async-await 异步处理、Preferences 数据持久化、文件读写、JSON 解析、或任何与数据获取/存储/传输相关的代码时，务必触发此 skill。即使用户只是说"怎么请求接口"或"存一下数据"，也应触发。如果用户需要的是完整业务功能（如下拉刷新列表、列表详情页），应优先触发 arkts-pattern-library。
---

# ArkTS Data Layer — 数据层生成器

## HarmonyOS Kit 知识使用规则

本 skill 的工程实践、迁移步骤和 ownership 以当前 skill 原内容为准。涉及具体 HarmonyOS Kit API、错误码、导入路径、权限、版本兼容、FAQ、最佳实践时，必须读取 `references/harmonyos-sdk/` 下对应 Kit 资料。

先按本 skill 实践确定数据层边界、模型结构、异步接口和持久化 ownership，再按任务场景读取对应 Kit 的 `routing.md` / `guides.md`。API、导入、权限、错误码、版本兼容以 Kit references 和 sources 为准。排障、适配或行为异常必须读取对应 Kit 的 `best-practices-and-faq.md`。当本 skill 原规则与 Kit 资料冲突时，保留工程分层和 ownership，用 Kit 知识修正具体 API 调用。不确定时调用 `arkts-knowledge-verifier`。

### 本 skill 已融合的 Kit

Kit 任务场景覆盖见 `references/harmonyos-sdk/kit-task-scenarios.md`。

- Network Kit：用于网络数据请求、长连接通信、连接状态处理和异常恢复；入口路径 `references/harmonyos-sdk/network-kit/routing.md`。
- ArkData：用于本地数据保存、结构化存取、缓存状态和数据同步；入口路径 `references/harmonyos-sdk/arkdata/routing.md`。
- ArkTS：用于数据建模、序列化转换、类型约束和迁移语法校正；入口路径 `references/harmonyos-sdk/arkts/routing.md`。

## API 版本

本 skill 的代码模板基于 **API 12+**（HarmonyOS 5.0.0+）。数据层相关的导入变化：

- HTTP 请求：`import { http } from '@kit.NetworkKit'`（不要用 `@ohos.net.http`）
- 网络状态：`import { connection } from '@kit.NetworkKit'`（不要用 `@ohos.net.connection`）
- 本地存储：`import { preferences } from '@kit.ArkData'`（不要用 `@ohos.data.preferences`）
- Ability：`import { common } from '@kit.AbilityKit'`（不要用 `@ohos.app.ability.common`）

生成代码前，先确认用户的目标 API 版本。检查方法：读取 `build-profile.json5` 的 `compatibleSdkVersion` 字段。遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 arkts-knowledge-verifier skill。

---

## 数据层架构

ArkTS 应用的数据层通常包含三个层次：

```
UI 层（@Component）
    ↓ 使用 @State/@ObjectLink 持有
Model 层（@Observed class）
    ↓ 调用方法获取数据
Service 层（网络请求/本地存储）
    ↓ 返回 Promise<T>
外部（HTTP API / Preferences / 文件系统）
```

### 数据存储决策树

```
数据要存哪里？
│
├─ 网络 API（远程数据）
│   └─ HttpUtil + Service 层（见下方第 3 节）
│
├─ 键值对设置（用户偏好、配置）
│   └─ Preferences（见下方第 5 节）
│       ⚠️ 只支持基础类型，复杂类型需 JSON 序列化
│
├─ 本地关系型数据库（结构化数据、需要 SQL 查询）
│   └─ RdbStore / relationalStore（见 references/rdbstore-dao-patterns.md）
│       · 单例初始化 + SecurityLevel
│       · 手写 CREATE TABLE SQL（替代 Room @Entity）
│       · DAO 类 + querySql()（替代 Room @Dao）
│       · ResultSet 必须 close()
│
└─ 事件通信（组件间数据传递）
    └─ EventHub（见下方第 4 节）
```

---

## 1. 数据模型（Model）

### @Observed 类标准骨架

所有需要驱动 UI 刷新的数据类都要加 `@Observed`：

```typescript
@Observed
export class ArticleModel {
  id: string
  title: string
  content: string
  author: string
  coverUrl: string
  likeCount: number
  isLiked: boolean
  createTime: number

  constructor(data?: Partial<ArticleModel>) {
    this.id = data?.id ?? ''
    this.title = data?.title ?? ''
    this.content = data?.content ?? ''
    this.author = data?.author ?? ''
    this.coverUrl = data?.coverUrl ?? ''
    this.likeCount = data?.likeCount ?? 0
    this.isLiked = data?.isLiked ?? false
    this.createTime = data?.createTime ?? 0
  }
}
```

**为什么 Partial**：网络返回的 JSON 字段可能不完整，Partial 允许只传部分字段，其余用默认值兜底。

> fromJson / fromJsonArray 等构建方法见 `references/model-patterns.md`

---

## 2. IDataSource / BasicDataSource（列表数据源）

LazyForEach 要求数据源实现 `IDataSource` 接口。通常封装 `BasicDataSource` 基类（完整实现见 `references/datasource-patterns.md`）。

### 使用 BasicDataSource

```typescript
@Component
struct ArticleListPage {
  private dataSource: BasicDataSource<ArticleModel> = new BasicDataSource()

  aboutToAppear(): void {
    this.loadArticles()
  }

  async loadArticles(): Promise<void> {
    const articles = await ArticleService.getList(1, 20)
    this.dataSource.reloadData(articles)
  }

  build() {
    List() {
      LazyForEach(this.dataSource, (item: ArticleModel) => {
        ListItem() {
          ArticleCard({ article: item })
        }
      }, (item: ArticleModel) => item.id)
    }
    .cachedCount(5)  // 预加载 5 个屏幕外的项
  }
}
```

---

## 3. 网络请求

### HTTP 请求封装

```typescript
import { http } from '@kit.NetworkKit'

export class HttpUtil {
  private static BASE_URL: string = 'https://api.example.com'

  static async get<T>(path: string, params?: Record<string, string>): Promise<T> {
    let url = `${HttpUtil.BASE_URL}${path}`
    if (params) {
      const query = Object.entries(params)
        .map(([k, v]) => `${k}=${encodeURIComponent(v)}`)
        .join('&')
      url += `?${query}`
    }

    const request = http.createHttp()
    try {
      const response = await request.request(url, {
        method: http.RequestMethod.GET,
        header: {
          'Content-Type': 'application/json'
        },
        readTimeout: 10000,
        connectTimeout: 10000,
      })

      if (response.responseCode === 200) {
        return JSON.parse(response.result as string) as T
      } else {
        throw new Error(`HTTP ${response.responseCode}`)
      }
    } finally {
      request.destroy()
    }
  }

  static async post<T>(path: string, body: object): Promise<T> {
    const url = `${HttpUtil.BASE_URL}${path}`
    const request = http.createHttp()
    try {
      const response = await request.request(url, {
        method: http.RequestMethod.POST,
        header: {
          'Content-Type': 'application/json'
        },
        extraData: JSON.stringify(body),
        readTimeout: 10000,
        connectTimeout: 10000,
      })

      if (response.responseCode === 200) {
        return JSON.parse(response.result as string) as T
      } else {
        throw new Error(`HTTP ${response.responseCode}`)
      }
    } finally {
      request.destroy()
    }
  }
}
```

### Service 层使用

```typescript
export class ArticleService {
  static async getList(page: number, size: number): Promise<ArticleModel[]> {
    interface ApiResponse {
      code: number
      data: Object[]
    }
    const res = await HttpUtil.get<ApiResponse>('/articles', {
      page: page.toString(),
      size: size.toString()
    })
    if (res.code === 0) {
      return ArticleModel.fromJsonArray(res.data)
    }
    return []
  }

  static async getDetail(id: string): Promise<ArticleModel | null> {
    interface ApiResponse {
      code: number
      data: Record<string, Object>
    }
    const res = await HttpUtil.get<ApiResponse>(`/articles/${id}`)
    if (res.code === 0) {
      return ArticleModel.fromJson(res.data)
    }
    return null
  }
}
```

### 网络状态检测

```typescript
import { connection } from '@kit.NetworkKit'

async function checkNetwork(): Promise<boolean> {
  try {
    const hasNet = await connection.hasDefaultNet()
    return hasNet
  } catch {
    return false
  }
}
```

**注意**：网络请求需要在 `module.json5` 中声明权限：
```json5
"requestPermissions": [
  { "name": "ohos.permission.INTERNET" }
]
```

---

## 4. EventHub 事件通信

适用于没有直接父子关系的组件间通信：

```typescript
import { common } from '@kit.AbilityKit'

// 发送事件
const context = getContext(this) as common.UIAbilityContext
context.eventHub.emit('cartUpdated', { count: 5 })

// 接收事件
aboutToAppear(): void {
  const context = getContext(this) as common.UIAbilityContext
  context.eventHub.on('cartUpdated', (data: Record<string, number>) => {
    this.cartCount = data.count
  })
}

// 取消订阅（防止内存泄漏）
aboutToDisappear(): void {
  const context = getContext(this) as common.UIAbilityContext
  context.eventHub.off('cartUpdated')
}
```

**事件名称建议定义为常量**：

```typescript
export class EventConstants {
  static readonly CART_UPDATED = 'cartUpdated'
  static readonly LOGIN_STATE_CHANGED = 'loginStateChanged'
  static readonly THEME_CHANGED = 'themeChanged'
}
```

---

## 5. Preferences 本地持久化

适合存储少量键值对数据（用户设置、搜索历史等）：

```typescript
import { preferences } from '@kit.ArkData'

export class PreferencesUtil {
  private static readonly STORE_NAME = 'app_preferences'
  private static prefs: preferences.Preferences | null = null

  // 初始化（在 EntryAbility.onCreate 中调用）
  static async init(context: Context): Promise<void> {
    PreferencesUtil.prefs = await preferences.getPreferences(context, PreferencesUtil.STORE_NAME)
  }

  static async put(key: string, value: preferences.ValueType): Promise<void> {
    if (!PreferencesUtil.prefs) return
    await PreferencesUtil.prefs.put(key, value)
    await PreferencesUtil.prefs.flush()
  }

  static async get(key: string, defaultValue: preferences.ValueType): Promise<preferences.ValueType> {
    if (!PreferencesUtil.prefs) return defaultValue
    return await PreferencesUtil.prefs.get(key, defaultValue)
  }

  static async delete(key: string): Promise<void> {
    if (!PreferencesUtil.prefs) return
    await PreferencesUtil.prefs.delete(key)
    await PreferencesUtil.prefs.flush()
  }

  static async has(key: string): Promise<boolean> {
    if (!PreferencesUtil.prefs) return false
    return await PreferencesUtil.prefs.has(key)
  }
}
```

**初始化**：在 `EntryAbility.onCreate()` 中调用 `PreferencesUtil.init(this.context)`，之后即可在任何地方使用 `put/get/delete/has`。

---

## 常见错误 vs 正确写法

### 错误 1：HTTP 请求没有 destroy

```typescript
// 错误 — 内存泄漏
const request = http.createHttp()
const response = await request.request(url, options)
// 忘记 destroy

// 正确 — 用 try-finally 确保清理
const request = http.createHttp()
try {
  const response = await request.request(url, options)
  return response
} finally {
  request.destroy()
}
```

### 错误 2：BasicDataSource 通知方式错误

```typescript
// 错误 — 批量添加后只通知一次 reload
pushDataArray(items: T[]): void {
  this.dataArray.push(...items)
  this.notifyDataReload()  // 整体刷新，性能差
}

// 正确 — 逐个通知 add（或根据场景选择 reload）
pushDataArray(items: T[]): void {
  const start = this.dataArray.length
  this.dataArray.push(...items)
  for (let i = start; i < this.dataArray.length; i++) {
    this.notifyDataAdd(i)
  }
}
```

### 错误 3：Preferences 没有 flush

```typescript
// 错误 — 数据只在内存中，应用退出丢失
await prefs.put('key', 'value')

// 正确 — put 后必须 flush
await prefs.put('key', 'value')
await prefs.flush()
```

### 错误 4：EventHub 没有取消订阅

```typescript
// 错误 — 组件销毁后仍然接收事件，可能崩溃
aboutToAppear() {
  context.eventHub.on('event', (data) => { this.data = data })
}
// 没有 aboutToDisappear + off

// 正确
private handler = (data: SomeType) => { this.data = data }

aboutToAppear() {
  context.eventHub.on('event', this.handler)
}
aboutToDisappear() {
  context.eventHub.off('event', this.handler)
}
```

---

## 生成检查清单

- [ ] 数据模型类添加了 @Observed（如果需要驱动 UI）
- [ ] 构造函数使用 Partial + 默认值防御
- [ ] HTTP 请求有 destroy 清理
- [ ] module.json5 声明了 INTERNET 权限
- [ ] async/await 正确使用
- [ ] Preferences 写入后调用了 flush
- [ ] EventHub 在 aboutToDisappear 中取消订阅
- [ ] BasicDataSource 通知方法与操作匹配

---

## References

- `references/model-patterns.md` — 完整的 Model 模式示例（带 fromJson、单例等）
- `references/datasource-patterns.md` — LazyDataSource / BasicDataSource 完整实现
- `references/network-service.md` — 网络请求封装、拦截器、错误处理完整模板（使用 @kit.NetworkKit）
- `references/rdbstore-dao-patterns.md` — RdbStore 单例初始化 + 建表模板 + ResultSet 解析 + DAO CRUD + 冲突处理策略
- `references/advanced-dao-patterns.md` — 多表 JOIN、ResultSet 安全、批量操作、ON CONFLICT
- `references/feed-update-service.md` — HTTP→XML→DB→EventBus 刷新管线
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 **arkts-knowledge-verifier** skill
