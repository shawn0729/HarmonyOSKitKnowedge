# 动态语言切换实现

> 完整的运行时语言切换代码模板，包括状态管理和 UI 刷新

---

## ⚠️ API 验证状态

| API | 状态 | 说明 |
|-----|------|------|
| `resourceManager.setPreferredLanguage()` | ⚠️ 未验证 | 需查官方文档确认 API 存在性 |
| `resourceManager.getPreferredLanguage()` | ⚠️ 未验证 | 需查官方文档确认 API 存在性 |
| `@State` 触发 UI 刷新 | ✅ 已验证 | ArkTS 标准机制 |
| `onLanguageConfigurationUpdate()` | ⚠️ 未验证 | 需确认生命周期回调是否正确 |

> **建议**：使用前请查阅官方文档
> - resourceManager API：https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-resource-manager-V5
> - 如 API 不存在，可使用应用内状态管理替代

---

## 基本实现模式

### 简单实现（单页面）

```typescript
import { resourceManager } from '@kit.LocalizationKit'
import { common } from '@kit.AbilityKit'
import { hilog } from '@kit.PerformanceAnalysisKit'

const DOMAIN = 0x0001
const TAG = 'I18nDemo'

@Entry
@Component
struct LanguageSwitchDemo {
  private context = getContext(this) as common.UIAbilityContext
  @State private currentLanguage: string = 'zh'
  @State private refreshKey: number = 0

  aboutToAppear(): void {
    this.loadCurrentLanguage()
  }

  async loadCurrentLanguage(): Promise<void> {
    try {
      const resMgr = this.context.resourceManager
      const langs = await resMgr.getPreferredLanguage()
      this.currentLanguage = langs[0] || 'zh'
      hilog.info(DOMAIN, TAG, `Current language: ${this.currentLanguage}`)
    } catch (e) {
      hilog.error(DOMAIN, TAG, `Failed to get language: ${e.message}`)
    }
  }

  async switchLanguage(lang: string): Promise<void> {
    try {
      hilog.info(DOMAIN, TAG, `Switching to: ${lang}`)

      const resMgr = this.context.resourceManager
      await resMgr.setPreferredLanguage([lang])

      this.currentLanguage = lang
      this.refreshKey++

      hilog.info(DOMAIN, TAG, `Language switched to: ${lang}`)
    } catch (e) {
      hilog.error(DOMAIN, TAG, `Failed to switch language: ${e.message}`)
    }
  }

  build() {
    Column({ space: 20 }) {
      Text($r('app.string.app_name'))
        .fontSize(24)
        .fontWeight(FontWeight.Bold)

      Text($r('app.string.welcome'))
        .fontSize(16)

      Text($r('app.string.settings_language'))
        .fontSize(14)
        .fontColor('#666666')

      Row({ space: 12 }) {
        Button('中文')
          .onClick(() => this.switchLanguage('zh'))
          .backgroundColor(this.currentLanguage === 'zh' ? '#007AFF' : '#CCCCCC')

        Button('English')
          .onClick(() => this.switchLanguage('en'))
          .backgroundColor(this.currentLanguage === 'en' ? '#007AFF' : '#CCCCCC')

        Button('日本語')
          .onClick(() => this.switchLanguage('ja'))
          .backgroundColor(this.currentLanguage === 'ja' ? '#007AFF' : '#CCCCCC')
      }

      Text(`Current: ${this.currentLanguage}`)
        .fontSize(12)
        .fontColor('#999999')
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .id('lang_container_' + this.refreshKey)
  }
}
```

---

## 完整实现（设置页面 + 全局状态）

### 1. 全局状态管理

```typescript
// common/GlobalState.ets
import { resourceManager } from '@kit.LocalizationKit'
import { common } from '@kit.AbilityKit'
import { AppStorage } from '@kit.ArkAppKit'
import { hilog } from '@kit.PerformanceAnalysisKit'

const DOMAIN = 0x0000
const TAG = 'LanguageState'

class LanguageState {
  private static instance: LanguageState | undefined = undefined
  @StorageLink('currentLanguage') currentLanguage: string = 'zh'
  @StorageLink('languageRefreshKey') refreshKey: number = 0

  static getInstance(): LanguageState {
    if (LanguageState.instance === undefined) {
      LanguageState.instance = new LanguageState()
    }
    return LanguageState.instance
  }

  async init(context: common.UIAbilityContext): Promise<void> {
    try {
      const resMgr = context.resourceManager
      const langs = await resMgr.getPreferredLanguage()
      this.currentLanguage = langs[0] || 'zh'
    } catch (e) {
      this.currentLanguage = 'zh'
    }
  }

  async setLanguage(context: common.UIAbilityContext, lang: string): Promise<void> {
    try {
      const resMgr = context.resourceManager
      await resMgr.setPreferredLanguage([lang])
      this.currentLanguage = lang
      this.refreshKey++
    } catch (e) {
      hilog.error(0x0000, 'GlobalState', `Failed to set language: ${e.message}`)
    }
  }
}
```

### 2. 设置页面

```typescript
// pages/SettingsPage.ets
import { GlobalState } from '../common/GlobalState'
import { common } from '@kit.AbilityKit'

@Entry
@Component
struct SettingsPage {
  @StorageLink('currentLanguage') currentLanguage: string = 'zh'
  @StorageLink('languageRefreshKey') refreshKey: number = 0
  private globalState = GlobalState.getInstance()

  @Builder
  LanguageItem(lang: string, label: string) {
    Row() {
      Text(label)
        .fontSize(16)

      if (this.currentLanguage === lang) {
        Text('✓')
          .fontSize(16)
          .fontColor('#007AFF')
      }
    }
    .width('100%')
    .padding(16)
    .backgroundColor(this.currentLanguage === lang ? '#F0F8FF' : '#FFFFFF')
    .onClick(() => {
      const context = getContext(this) as common.UIAbilityContext
      this.globalState.setLanguage(context, lang)
    })
  }

  build() {
    Column() {
      Text($r('app.string.settings_title'))
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .padding(16)

      List() {
        ListItem() {
          this.LanguageItem('zh', '简体中文')
        }

        ListItem() {
          this.LanguageItem('zh-Hans', '简体中文 (简体)')
        }

        ListItem() {
          this.LanguageItem('zh-Hant', '繁体中文 (繁体)')
        }

        ListItem() {
          this.LanguageItem('en', 'English')
        }

        ListItem() {
          this.LanguageItem('ja', '日本語')
        }
      }
    }
    .width('100%')
    .height('100%')
    .id('settings_' + this.refreshKey)
  }
}
```

---

## 语言切换后刷新页面的方法

### 方法 1：状态更新 + ID 变化

```typescript
@State private refreshKey: number = 0

async switchLanguage(lang: string) {
  await resourceManager.setPreferredLanguage([lang])
  this.refreshKey++
}

build() {
  Column() {
    Text($r('app.string.hello'))
  }
  .id('page_' + this.refreshKey)  // ID 变化触发重建
}
```

### 方法 2：router.replaceUrl 重新加载

```typescript
import { router } from '@kit.ArkUI'

async switchLanguage(lang: string) {
  await resourceManager.setPreferredLanguage([lang])
  router.replaceUrl({ url: 'pages/SettingsPage' })
}
```

### 方法 3：Navigation 模式

```typescript
@State private navPathStack: NavPathStack = new NavPathStack()

build() {
  Navigation(this.navPathStack) {
    // 内容
  }
  .id('nav_' + this.refreshKey)
}
```

---

## 获取支持的语言列表

```typescript
import { resourceManager } from '@kit.LocalizationKit'

interface LanguageInfo {
  language: string   // 如 'zh'
  region?: string    // 如 'CN'
  displayName: string // 如 '简体中文'
}

async function getSupportedLanguages(): Promise<LanguageInfo[]> {
  // 这是一个示例，实际 API 可能不同
  const supported = ['zh', 'zh-Hans', 'zh-Hant', 'en', 'ja', 'ko']
  const displayNames: Record<string, string> = {
    'zh': '中文',
    'zh-Hans': '简体中文',
    'zh-Hant': '繁体中文',
    'en': 'English',
    'ja': '日本語',
    'ko': '한국어'
  }

  return supported.map(lang => ({
    language: lang,
    displayName: displayNames[lang] || lang
  }))
}
```

---

## 监听系统语言变化

### 在 UIAbility 中处理

```typescript
// EntryAbility.ets
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit'
import { hilog } from '@kit.PerformanceAnalysisKit'

export default class EntryAbility extends UIAbility {
  onLanguageConfigurationUpdate(): void {
    hilog.info(0x0000, 'EntryAbility', 'System language configuration updated')

    // 1. 重新获取当前语言
    const newLang = this.context.resourceManager.getPreferredLanguage()

    // 2. 更新 AppStorage
    AppStorage.setOrCreate('currentLanguage', newLang)
    AppStorage.setOrCreate('languageRefreshKey',
      AppStorage.get<number>('languageRefreshKey', 0) + 1)

    // 3. 可以选择重启应用或导航到首页
    // hilog.info(0x0000, 'EntryAbility', 'Restarting app to apply language change')
  }

  onConfigurationUpdate(configuration: AbilityConstant.Configuration): void {
    hilog.info(0x0000, 'EntryAbility', 'Configuration updated: %{public}s',
      JSON.stringify(configuration))

    // 处理语言或地区变化
    if (configuration.language !== undefined) {
      hilog.info(0x0000, 'EntryAbility', `Language changed to: ${configuration.language}`)
    }
  }
}
```

---

## 完整页面刷新机制

```typescript
// 确保语言切换后所有页面都刷新的完整模式

// 1. 状态管理
class LanguageManager {
  private static instance: LanguageManager | undefined = undefined

  @StorageLink('languageRefreshKey') refreshKey: number = 0

  static getInstance(): LanguageManager {
    if (LanguageManager.instance === undefined) {
      LanguageManager.instance = new LanguageManager()
    }
    return LanguageManager.instance
  }

  async switchLanguage(context: common.UIAbilityContext, lang: string): Promise<void> {
    // 1. 切换语言
    const resMgr = context.resourceManager
    await resMgr.setPreferredLanguage([lang])

    // 2. 更新状态（触发所有 @StorageLink 组件重建）
    this.refreshKey++

    // 3. 发布事件通知所有页面
    // 可通过 EventHub 或 AppEventHub 通知
  }
}

// 2. 页面使用
@Entry
@Component
struct AnyPage {
  @StorageLink('languageRefreshKey') refreshKey: number = 0

  build() {
    Column() {
      Text($r('app.string.any_string'))
        .fontSize(16)
    }
    .id('page_' + this.refreshKey)
  }
}
```

---

## 注意事项

1. **语言代码大小写**：`zh-Hans` vs `zh-hans` — 必须完全匹配
2. **切换后需要时间生效**：异步操作，避免连续快速切换
3. **并非所有页面都需要重建**：只有使用 `@StorageLink` 或 `@State` 监听 `refreshKey` 的组件才会重建
4. **性能考虑**：避免高频调用，建议在语言切换按钮上做防抖

---

## 如果 setPreferredLanguage API 不存在的替代方案

> ⚠️ 如果官方 API 确认不存在 `setPreferredLanguage()`，可以使用以下替代方案

### 方案 1：应用内状态管理（推荐）

```typescript
// common/LanguageManager.ets
import { AppStorage } from '@kit.ArkAppKit'

export class LanguageManager {
  private static instance: LanguageManager | undefined = undefined
  private currentLang: string = 'zh'

  static getInstance(): LanguageManager {
    if (LanguageManager.instance === undefined) {
      LanguageManager.instance = new LanguageManager()
    }
    return LanguageManager.instance
  }

  getCurrentLanguage(): string {
    return this.currentLang
  }

  setLanguage(lang: string): void {
    this.currentLang = lang
    // 通知所有页面刷新
    AppStorage.setOrCreate('currentLanguage', lang)
    AppStorage.setOrCreate('languageRefreshKey', 
      AppStorage.get<number>('languageRefreshKey', 0) + 1)
  }
}
```

**使用方式**：

```typescript
// 页面中使用
@Entry
@Component
struct SettingsPage {
  @StorageLink('currentLanguage') currentLanguage: string = 'zh'
  @StorageLink('languageRefreshKey') refreshKey: number = 0
  private langManager = LanguageManager.getInstance()

  build() {
    Column() {
      Button('中文')
        .onClick(() => {
          this.langManager.setLanguage('zh')
          // UI 会自动刷新，因为使用了 @StorageLink
        })
      
      Button('English')
        .onClick(() => {
          this.langManager.setLanguage('en')
        })
      
      Text($r('app.string.welcome'))
    }
    .id('page_' + this.refreshKey)
  }
}
```

**优点**：
- ✅ 不依赖未知 API
- ✅ 完全可控
- ✅ 即时生效

**缺点**：
- ⚠️ 仅应用内生效，不影响系统语言
- ⚠️ 需要手动维护语言状态

---

### 方案 2：引导用户到系统设置

```typescript
import { common, Want } from '@kit.AbilityKit'
import { promptAction } from '@kit.ArkUI'

async function openSystemLanguageSettings(): Promise<void> {
  try {
    const context = getContext(this) as common.UIAbilityContext
    const want: Want = {
      action: 'action.settings.language',
    }
    
    context.startAbility(want)
      .then(() => {
        hilog.info(DOMAIN, TAG, 'Opened language settings')
      })
      .catch((err: Error) => {
        promptAction.showToast({ message: '无法打开设置' })
      })
  } catch (err) {
    promptAction.showToast({ message: '打开设置失败' })
  }
}
```

**使用场景**：
- 当无法动态切换时
- 用户需要永久修改系统语言

---

### 方案 3：重启应用应用语言

```typescript
import { common } from '@kit.AbilityKit'
import { process } from '@kit.BasicServicesKit'

function restartApp(): void {
  const context = getContext(this) as common.UIAbilityContext
  // ⚠️ 需要查证：HarmonyOS 是否支持应用重启
  // Android: Process.killProcess(Process.myPid())
  // HarmonyOS: 可能需要使用 context.terminateSelf() 然后重新启动
  context.terminateSelf()
}
```

> ⚠️ **注意**：此方案需要查证 HarmonyOS 是否支持应用自重启

---

### 最佳实践推荐

1. **优先尝试官方 API**：查证 `setPreferredLanguage()` 是否存在
2. **方案 1 作为备选**：应用内状态管理是通用解决方案
3. **方案 2 作为兜底**：引导用户到系统设置
4. **避免方案 3**：重启应用体验较差
