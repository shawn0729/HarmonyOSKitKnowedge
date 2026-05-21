---
name: arkts-pattern-library
description: 提供 ArkTS/HarmonyOS 常见功能的完整实现方案。当用户需要实现搜索功能、列表详情页、登录注册、下拉刷新加载更多、Tab 内容切换、个人中心页面、设置页面、主题切换、空状态页面、骨架屏加载、或任何完整的业务功能时，务必触发此 skill。即使用户只说"做个搜索"或"写个列表页"，也应触发。这是一个综合模式库，与其他 skill 配合使用。当用户请求涉及完整业务功能（不仅仅是单个组件或技术点），优先触发此 skill。
---

# ArkTS Pattern Library — 综合功能模式库

## API 版本

本 skill 的代码模板基于 **API 12+**（HarmonyOS 5.0.0+）。生成代码前，先确认用户的目标 API 版本。检查方法：读取项目的 `build-profile.json5` 中的 `compatibleSdkVersion` 字段。

- 使用 `@kit.*` 导入（不要用 `@ohos.*`）
- 使用 Navigation 导航（不要用 @ohos.router）
- @Prop 必须初始化默认值
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 arkts-knowledge-verifier skill

---

## 模式索引

| 模式名称 | 一句话描述 | 涉及技术 |
|---------|----------|---------|
| 列表详情页 | 列表页 → 点击 → 详情页 | Navigation + LazyForEach + NavDestination |
| 搜索功能 | 搜索框 + 历史 + 实时搜索 + 结果列表 | TextInput + Preferences + 防抖 |
| 下拉刷新加载更多 | 上拉触底加载更多 + 下拉刷新 | Refresh + List.onReachEnd + BasicDataSource |
| Tab 内容切换 | 顶部/底部标签切换不同内容 | Tabs + TabContent + @Builder |
| 登录状态管理 | 登录/未登录切换显示 | AppStorage + @StorageLink |
| 设置页面 | 开关/选项/版本信息列表 | List + ListItem + Toggle |
| 空状态 & 加载态 | 加载中/空数据/错误状态切换 | if/else + @State 枚举 |
| 瀑布流 | 不等高卡片网格 | WaterFlow + FlowItem |
| 播放器 UI | MiniPlayer + FullPlayer 双态播放器 | AVPlayer + @StorageLink + NavDestination |
| 下载管理 UI | 进度环 + 取消按钮 + 完成状态 | Progress Ring + request.agent |
| Feed 列表+详情页 | 网格订阅列表 → Feed 详情 → 剧集详情 | List + Grid + NavPathStack |

---

## 模式 1：列表详情页

最常见的应用模式。列表展示数据，点击进入详情。

### 核心结构

```typescript
// 入口页 — 列表
@Entry
@Component
struct ListPage {
  @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack()
  @State items: ArticleModel[] = []

  @Builder
  pageMap(name: string) {
    if (name === 'DetailPage') {
      DetailPage()
    }
  }

  aboutToAppear(): void {
    this.loadData()
  }

  async loadData(): Promise<void> {
    this.items = await ArticleService.getList()
  }

  build() {
    Navigation(this.navPathStack) {
      List() {
        ForEach(this.items, (item: ArticleModel) => {
          ListItem() {
            ArticleCard({ article: item })
              .onClick(() => {
                this.navPathStack.pushPathByName('DetailPage', { id: item.id })
              })
          }
        }, (item: ArticleModel) => item.id)
      }
    }
    .navDestination(this.pageMap)
    .title('文章列表')
    .mode(NavigationMode.Stack)
  }
}

// 详情页
@Component
struct DetailPage {
  @Consume('navPathStack') navPathStack: NavPathStack
  @State article: ArticleModel | null = null

  build() {
    NavDestination() {
      if (this.article) {
        Scroll() {
          Column() {
            Image(this.article.coverUrl)
              .width('100%')
              .height(200)
            Text(this.article.title)
              .fontSize(22)
              .fontWeight(FontWeight.Bold)
              .padding(16)
            Text(this.article.content)
              .fontSize(16)
              .padding({ left: 16, right: 16 })
          }
        }
      } else {
        LoadingView()
      }
    }
    .title('文章详情')
    .onReady((context: NavDestinationContext) => {
      const param = context.pathInfo.param as Record<string, string>
      this.loadDetail(param?.id ?? '')
    })
  }

  async loadDetail(id: string): Promise<void> {
    this.article = await ArticleService.getDetail(id)
  }
}
```

**配合使用**：arkts-component-builder（UI组件）+ arkts-navigation-builder（导航）+ arkts-data-layer（数据层）

---

## 模式 2：搜索功能

### 核心结构

```typescript
@Component
struct SearchView {
  @State keyword: string = ''
  @State searchHistory: string[] = []
  @State searchResults: ArticleModel[] = []
  @State isSearching: boolean = false
  private searchTimer: number = -1

  aboutToAppear(): void {
    this.loadHistory()
  }

  async loadHistory(): Promise<void> {
    const historyStr = await PreferencesUtil.get('search_history', '[]') as string
    this.searchHistory = JSON.parse(historyStr)
  }

  // 防抖搜索：用户停止输入 300ms 后触发
  onKeywordChange(value: string): void {
    this.keyword = value
    clearTimeout(this.searchTimer)
    if (value.length > 0) {
      this.searchTimer = setTimeout(() => {
        this.performSearch(value)
      }, 300)
    } else {
      this.searchResults = []
      this.isSearching = false
    }
  }

  async performSearch(keyword: string): Promise<void> {
    this.isSearching = true
    this.searchResults = await ArticleService.search(keyword)
    this.isSearching = false
    // 保存搜索历史
    await this.saveHistory(keyword)
  }

  async saveHistory(keyword: string): Promise<void> {
    const filtered = this.searchHistory.filter(item => item !== keyword)
    filtered.unshift(keyword)
    this.searchHistory = filtered.slice(0, 20)
    await PreferencesUtil.put('search_history', JSON.stringify(this.searchHistory))
  }

  async clearHistory(): Promise<void> {
    this.searchHistory = []
    await PreferencesUtil.delete('search_history')
  }

  @Builder
  historySection() {
    if (this.searchHistory.length > 0 && this.keyword.length === 0) {
      Column() {
        Row() {
          Text('搜索历史').fontSize(16).fontWeight(FontWeight.Bold)
          Blank()
          Text('清空')
            .fontSize(14)
            .fontColor('#999')
            .onClick(() => this.clearHistory())
        }
        .width('100%')
        .padding({ left: 16, right: 16, top: 12, bottom: 8 })

        Flex({ wrap: FlexWrap.Wrap }) {
          ForEach(this.searchHistory, (item: string) => {
            Text(item)
              .fontSize(14)
              .padding({ left: 12, right: 12, top: 6, bottom: 6 })
              .margin(4)
              .borderRadius(16)
              .backgroundColor('#F5F5F5')
              .onClick(() => {
                this.keyword = item
                this.performSearch(item)
              })
          }, (item: string) => item)
        }
        .padding({ left: 12, right: 12 })
      }
    }
  }

  build() {
    Column() {
      // 搜索框
      Search({ value: this.keyword, placeholder: '搜索文章...' })
        .width('100%')
        .padding({ left: 16, right: 16, top: 8 })
        .onChange((value: string) => this.onKeywordChange(value))
        .onSubmit((value: string) => this.performSearch(value))

      // 搜索历史
      this.historySection()

      // 搜索结果
      if (this.isSearching) {
        LoadingView()
      } else if (this.keyword.length > 0 && this.searchResults.length === 0) {
        EmptyView({ message: '没有找到相关内容' })
      } else {
        List() {
          ForEach(this.searchResults, (item: ArticleModel) => {
            ListItem() {
              ArticleCard({ article: item })
            }
          }, (item: ArticleModel) => item.id)
        }
      }
    }
    .width('100%')
    .height('100%')
  }
}
```

---

## 模式 3：下拉刷新 + 加载更多

核心结构骨架（完整代码见 `references/list-detail-pattern.md`）：

```typescript
@Component
struct RefreshableList {
  @State isRefreshing: boolean = false
  @State isLoadingMore: boolean = false
  @State hasMore: boolean = true
  @State page: number = 1
  private dataSource: BasicDataSource<ArticleModel> = new BasicDataSource()

  build() {
    Refresh({ refreshing: $$this.isRefreshing }) {
      List() {
        LazyForEach(this.dataSource, (item: ArticleModel) => {
          ListItem() { ArticleCard({ article: item }) }
        }, (item: ArticleModel) => item.id)
      }
      .cachedCount(5)
      .onReachEnd(() => { /* 加载更多 */ })
    }
    .onRefreshing(async () => { /* 刷新数据 */ })
  }
}
```

**关键点**：Refresh 包裹 List，List.onReachEnd 触发加载更多，BasicDataSource.pushDataArray 追加数据。

---

## 模式 4：登录状态管理

核心骨架（完整代码见 `references/auth-pattern.md`）：

```typescript
@Component
struct ProfileView {
  @StorageLink('isLoggedIn') isLoggedIn: boolean = false

  build() {
    Column() {
      if (this.isLoggedIn) {
        this.loggedInView()    // 头像 + 昵称 + 退出按钮
      } else {
        this.loginGuideView()  // 占位图 + 登录按钮
      }
    }
  }
}
```

**关键点**：AppStorage + @StorageLink 管理全局登录状态，EntryAbility.onCreate 中初始化。

---

## 模式 5：空状态 & 加载态

```typescript
enum PageState { Loading, Success, Empty, Error }

@Component
struct StatefulPage {
  @State pageState: PageState = PageState.Loading

  build() {
    Column() {
      if (this.pageState === PageState.Loading) {
        LoadingProgress().width(48).height(48)
      } else if (this.pageState === PageState.Empty) {
        Text('暂无数据')
      } else if (this.pageState === PageState.Error) {
        Button('重试').onClick(() => this.loadData())
      } else {
        List() { /* 数据列表 */ }
      }
    }
  }
}
```

**关键点**：用枚举管理页面状态，根据状态条件渲染不同 UI。

---

## 模式 6：设置页面

核心骨架（用 List + @Builder 构建设置项）：

```typescript
@Component
struct SettingsPage {
  @StorageLink('isDarkMode') isDarkMode: boolean = false

  @Builder
  settingToggle(title: string, isOn: boolean, onChange: (value: boolean) => void) {
    Row() {
      Text(title).fontSize(16)
      Blank()
      Toggle({ type: ToggleType.Switch, isOn: isOn }).onChange(onChange)
    }.width('100%').height(56).padding({ left: 16, right: 16 })
  }

  build() {
    List() {
      ListItem() { this.settingToggle('深色模式', this.isDarkMode, (v) => { this.isDarkMode = v }) }
    }
    .divider({ strokeWidth: 0.5, color: '#F0F0F0', startMargin: 16 })
  }
}
```

**关键点**：@Builder 抽取设置项（Toggle/Action/Info 三种类型），@StorageLink 关联全局设置。

---

## 组合说明

这些模式通常需要组合使用：

| 功能 | 需要配合的 skills |
|------|-----------------|
| 列表详情页 | component-builder + navigation-builder + data-layer |
| 搜索功能 | component-builder + data-layer（Preferences） |
| 下拉刷新列表 | component-builder + data-layer（BasicDataSource） |
| 登录状态 | state-manager（AppStorage） |
| 设置页面 | state-manager + component-builder |
| 完整应用 | project-scaffolder + 以上全部 |

---

## Multi-Skill 编排协议

本 skill 提供的业务模式通常需要多个 skill 协作完成。当你被触发后，根据用户的具体需求，按以下指引读取其他 skill 的 reference 文件来生成完整方案。

### 执行顺序

生成完整业务功能时，按此顺序生成各层代码：

```
Model（数据模型）→ DataSource（数据源）→ State（状态管理）→ Navigation（导航）→ UI（页面组件）→ Animation（动画，可选）
```

### 场景路由表

| 业务场景 | 需要读取的 reference | 生成内容 |
|---------|---------------------|---------|
| **列表详情页** | ① `arkts-data-layer/SKILL.md`"数据模型"节 ② `arkts-data-layer/references/datasource-patterns.md` ③ `arkts-navigation-builder/SKILL.md`"NavDestination 页面模板"节 | Model + BasicDataSource + Navigation 框架 + 列表页 + 详情页 |
| **搜索功能** | ① `arkts-data-layer/references/network-service.md` | 网络请求 + SearchView + Preferences 持久化 |
| **下拉刷新列表** | ① `arkts-data-layer/references/datasource-patterns.md` ② `arkts-data-layer/references/network-service.md` | BasicDataSource + 分页请求 + Refresh 列表 |
| **登录状态** | ① `arkts-state-manager/references/global-state.md` ② `arkts-data-layer/references/network-service.md` | AppStorage 状态 + 登录接口 + 状态切换 UI |
| **设置页面** | ① `arkts-state-manager/references/global-state.md` ② `arkts-component-builder/references/common-components.md` | 持久化设置 + Toggle/List 组件 |

### 编排流程

1. **识别场景**：根据用户请求匹配上方场景路由表
2. **读取 reference**：用 Read 工具按表中顺序读取所需的 reference 文件
3. **按顺序生成**：Model → Service → Page，确保依赖关系正确
4. **分文件输出**：每个文件用 `// === 文件路径 ===` 标注，方便用户复制
5. **验证检查**：读取 `arkts-knowledge-verifier/references/arkts-vs-typescript.md` 确认无 ArkTS 幻觉

> 完整的路由矩阵和输出格式规范见 `arkts-knowledge-verifier/references/skill-routing-guide.md`

---

## References

- `references/list-detail-pattern.md` — 列表+详情页完整方案（含分页、缓存）
- `references/search-pattern.md` — 搜索功能完整方案（搜索框+历史+结果+持久化）
- `references/auth-pattern.md` — 登录/用户状态管理完整方案
- `references/performance-patterns.md` — 性能优化模式（LazyForEach + @Reusable + cachedCount）
- `references/media-app-pattern.md` — 媒体应用模式：播放器 UI、下载管理 UI、Feed 列表+详情页
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 **arkts-knowledge-verifier** skill
