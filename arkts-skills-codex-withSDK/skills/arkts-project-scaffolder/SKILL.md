---
name: arkts-project-scaffolder
description: 生成 ArkTS/HarmonyOS 项目结构和配置文件。当用户需要创建新项目、设计模块结构、编写 module.json5、build-profile.json5、oh-package.json5、app.json5 配置文件、设计多模块架构（commons/features/products）、创建 EntryAbility、配置权限、设置 Index.ets 导出、或搭建任何 HarmonyOS 项目骨架时，务必触发此 skill。即使用户只是说"新建个项目"或"项目怎么搭建"，也应触发。当用户说"从零搭建完整应用"，优先触发此 skill，它会引导使用其他 skill 搭建完整项目。
---

# ArkTS Project Scaffolder — 项目脚手架

## HarmonyOS Kit 知识使用规则

本 skill 的工程实践、迁移步骤和 ownership 以当前 skill 原内容为准。涉及具体 HarmonyOS Kit API、错误码、导入路径、权限、版本兼容、FAQ、最佳实践时，必须读取 `references/harmonyos-sdk/` 下对应 Kit 资料。

先按本 skill 实践确定项目结构、模块边界、配置文件和 EntryAbility ownership，再按任务场景读取对应 Kit 的 `routing.md` / `guides.md`。API、导入、权限、错误码、版本兼容以 Kit references 和 sources 为准。排障、适配或行为异常必须读取对应 Kit 的 `best-practices-and-faq.md`。当本 skill 原规则与 Kit 资料冲突时，保留工程分层和 ownership，用 Kit 知识修正具体 API 调用。不确定时调用 `arkts-knowledge-verifier`。

### 本 skill 已融合的 Kit

Kit 任务场景覆盖见 `references/harmonyos-sdk/kit-task-scenarios.md`。

- Ability Kit：用于应用入口、模块配置、页面承载和跨能力启动链路；入口路径 `references/harmonyos-sdk/ability-kit/routing.md`。

## API 版本

本 skill 的配置模板基于 **API 12+**（HarmonyOS 5.0.0+）。项目配置中的版本字段：

- `build-profile.json5` 中的 `compileSdkVersion` 和 `compatibleSdkVersion`：编译和兼容的 API 级别
  - 数字格式：`12`（推荐）
  - 字符串格式：`"5.0.0(12)"`（部分 DevEco Studio 版本使用，括号内为 API 级别）
- `app.json5` 中的 `minAPIVersion` 和 `targetAPIVersion`：与 `compatibleSdkVersion` / `compileSdkVersion` 对应
- 所有模板使用 `@kit.*` 导入（不要用 `@ohos.*`）
- EntryAbility 使用 `import { ... } from '@kit.AbilityKit'`

生成配置文件时，根据用户的目标版本设置正确的 SDK 版本号。遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 arkts-knowledge-verifier skill。

---

## 项目复杂度决策

```
你的项目有多复杂？
│
├─ 简单应用（<5 页面，单人开发）
│   └─ 单模块项目
│       一个 entry 模块搞定一切
│
├─ 中等应用（5-15 页面，小团队）
│   └─ 单模块 + 功能目录划分
│       entry 模块内按 features/ 组织
│
└─ 大型应用（>15 页面，多团队协作）
    └─ 多模块项目
        commons/ + features/ + products/
        每个模块独立编译、独立测试
```

---

## 单模块项目结构

适合绝大多数场景，从这里开始：

```
MyApp/
├── AppScope/
│   ├── app.json5                # 应用级配置
│   └── resources/               # 应用级资源
├── entry/                       # 主模块
│   ├── src/main/
│   │   ├── ets/
│   │   │   ├── entryability/
│   │   │   │   └── EntryAbility.ets    # 应用入口
│   │   │   ├── pages/
│   │   │   │   ├── Index.ets           # 首页（@Entry）
│   │   │   │   ├── DetailPage.ets
│   │   │   │   └── SettingsPage.ets
│   │   │   ├── components/             # 公共组件
│   │   │   │   ├── CommonHeader.ets
│   │   │   │   └── LoadingView.ets
│   │   │   ├── model/                  # 数据模型
│   │   │   │   └── ArticleModel.ets
│   │   │   ├── service/                # 网络服务
│   │   │   │   └── ApiService.ets
│   │   │   ├── common/                 # 工具/常量
│   │   │   │   ├── Constants.ets
│   │   │   │   └── PreferencesUtil.ets
│   │   │   └── viewmodel/             # 视图模型（可选）
│   │   ├── resources/
│   │   │   ├── base/
│   │   │   │   ├── element/
│   │   │   │   │   ├── string.json
│   │   │   │   │   └── color.json
│   │   │   │   ├── media/              # 图片资源
│   │   │   │   └── profile/
│   │   │   │       ├── main_pages.json # 页面路由注册
│   │   │   │       └── backup_rules.json
│   │   │   ├── en_US/                  # 英文资源
│   │   │   └── zh_CN/                  # 中文资源
│   │   └── module.json5               # 模块配置
│   ├── oh-package.json5               # 依赖管理
│   └── hvigorfile.ts                  # 构建脚本
├── build-profile.json5                # 构建配置
├── oh-package.json5                   # 项目级依赖
└── hvigorfile.ts                      # 项目级构建脚本
```

---

## 各配置文件模板

### app.json5（应用级）

```json5
{
  "app": {
    "bundleName": "com.example.myapp",        // 应用包名，全局唯一
    "vendor": "example",                       // 开发者/公司
    "versionCode": 1000000,                    // 版本号（整数，用于升级判断）
    "versionName": "1.0.0",                    // 版本名（展示给用户）
    "icon": "$media:app_icon",                 // 应用图标
    "label": "$string:app_name",               // 应用名称
    "minAPIVersion": 12,                       // 最低兼容 API 版本
    "targetAPIVersion": 12                     // 目标 API 版本
  }
}
```

### module.json5（模块级）

```json5
{
  "module": {
    "name": "entry",                           // 模块名
    "type": "entry",                           // entry=主模块, feature=功能模块
    "description": "$string:module_desc",
    "mainElement": "EntryAbility",             // 入口 Ability
    "deviceTypes": [                           // 支持的设备类型
      "phone",
      "tablet"
    ],
    "deliveryWithInstall": true,
    "installationFree": false,
    "pages": "$profile:main_pages",            // 页面路由文件
    "abilities": [
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility_desc",
        "icon": "$media:layered_image",
        "label": "$string:EntryAbility_label",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start_window_background",
        "exported": true,
        "skills": [
          {
            "entities": ["entity.system.home"],
            "actions": ["action.system.home"]
          }
        ]
      }
    ],
    // 权限配置
    "requestPermissions": [
      {
        "name": "ohos.permission.INTERNET"     // 网络访问
      }
    ]
  }
}
```

### 常用权限速查表

```json5
// 网络访问（几乎所有应用都需要）
{ "name": "ohos.permission.INTERNET" }

// 获取网络信息
{ "name": "ohos.permission.GET_NETWORK_INFO" }

// 相机
{ "name": "ohos.permission.CAMERA" }

// 麦克风
{ "name": "ohos.permission.MICROPHONE" }

// 位置
{ "name": "ohos.permission.APPROXIMATELY_LOCATION" }
{ "name": "ohos.permission.LOCATION" }

// 读写媒体文件
{ "name": "ohos.permission.READ_MEDIA" }
{ "name": "ohos.permission.WRITE_MEDIA" }

// 通知
{ "name": "ohos.permission.NOTIFICATION_CONTROLLER" }

// 后台任务
{ "name": "ohos.permission.KEEP_BACKGROUND_RUNNING" }
```

### main_pages.json（页面路由）

```json
{
  "src": [
    "pages/Index",
    "pages/DetailPage",
    "pages/SettingsPage"
  ]
}
```

**注意**：使用 Navigation + NavDestination 时，只需注册入口页面。其他页面通过 navDestination @Builder 映射。

### oh-package.json5（依赖管理）

```json5
{
  "name": "entry",
  "version": "1.0.0",
  "description": "Main entry module",
  "main": "",
  "author": "",
  "license": "Apache-2.0",
  "dependencies": {
    // 第三方库示例
  },
  "devDependencies": {
    // 开发依赖
  }
}
```

### build-profile.json5（构建配置）

```json5
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compileSdkVersion": 12,
        "compatibleSdkVersion": 12,
        "runtimeOS": "HarmonyOS"
      }
    ]
  },
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        {
          "name": "default",
          "applyToProducts": ["default"]
        }
      ]
    }
  ]
}
```

---

## EntryAbility.ets 标准模板

```typescript
import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit'
import { hilog } from '@kit.PerformanceAnalysisKit'
import { window } from '@kit.ArkUI'

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(0x0000, 'EntryAbility', 'onCreate')

    // 初始化全局状态
    AppStorage.setOrCreate('isLoggedIn', false)

    // 初始化 Preferences（如需要）
    // PreferencesUtil.init(this.context)
  }

  onDestroy(): void {
    hilog.info(0x0000, 'EntryAbility', 'onDestroy')
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    hilog.info(0x0000, 'EntryAbility', 'onWindowStageCreate')

    // 加载主页面
    windowStage.loadContent('pages/Index', (err) => {
      if (err.code) {
        hilog.error(0x0000, 'EntryAbility', 'Failed to load content: %{public}s', JSON.stringify(err))
        return
      }
      hilog.info(0x0000, 'EntryAbility', 'Content loaded successfully')
    })
  }

  onWindowStageDestroy(): void {
    hilog.info(0x0000, 'EntryAbility', 'onWindowStageDestroy')
  }

  onForeground(): void {
    hilog.info(0x0000, 'EntryAbility', 'onForeground')
  }

  onBackground(): void {
    hilog.info(0x0000, 'EntryAbility', 'onBackground')
  }
}
```

---

## 多模块项目结构

当项目达到一定规模时，拆分模块有助于团队协作和编译效率：

```
MyApp/
├── AppScope/
│   └── app.json5
├── commons/                     # 公共模块（工具、基础组件）
│   ├── common/                  # 通用工具
│   │   ├── src/main/ets/
│   │   │   ├── utils/
│   │   │   ├── constants/
│   │   │   └── Index.ets       # barrel export
│   │   ├── oh-package.json5
│   │   └── module.json5        # type: "har"
│   └── uicomponents/           # UI 组件库
│       ├── src/main/ets/
│       │   ├── components/
│       │   └── Index.ets
│       └── module.json5        # type: "har"
├── features/                    # 功能模块
│   ├── discover/
│   │   ├── src/main/ets/
│   │   │   ├── views/
│   │   │   ├── model/
│   │   │   ├── service/
│   │   │   └── Index.ets
│   │   └── module.json5        # type: "har"
│   ├── mine/
│   └── settings/
├── products/                    # 产品模块（entry）
│   └── phone/
│       ├── src/main/ets/
│       │   ├── entryability/
│       │   └── pages/
│       └── module.json5        # type: "entry"
└── build-profile.json5         # 注册所有模块
```

### Index.ets barrel export 模式

每个模块的 `Index.ets` 统一导出公共接口：

```typescript
// features/discover/Index.ets
export { DiscoverView } from './views/DiscoverView'
export { DiscoverModel } from './model/DiscoverModel'
export { ArticleModel } from './model/ArticleModel'
```

### 模块间引用

```json5
// products/phone/oh-package.json5
{
  "dependencies": {
    "@commons/common": "file:../../commons/common",
    "@features/discover": "file:../../features/discover"
  }
}
```

```typescript
// products/phone/src/main/ets/pages/Index.ets
import { DiscoverView } from '@features/discover'
import { Constants } from '@commons/common'
```

---

## HAR 模块配置

功能模块使用 HAR（Harmony Archive）类型：

```json5
// features/discover/module.json5
{
  "module": {
    "name": "discover",
    "type": "har",           // HAR 类型，不是 entry
    "deviceTypes": ["phone", "tablet"]
  }
}
```

---

## 常见错误 vs 正确写法

### 错误 1：页面未在 main_pages.json 注册

```json
// 错误 — 新建页面忘记注册
{ "src": ["pages/Index"] }
// DetailPage 未注册 → 跳转白屏

// 正确
{ "src": ["pages/Index", "pages/DetailPage"] }
```

### 错误 2：bundleName 格式不规范

```json5
// 错误
"bundleName": "myapp"              // 太短，不符合规范

// 正确 — 反向域名格式
"bundleName": "com.example.myapp"
```

### 错误 3：多模块依赖路径错误

```json5
// 错误 — 路径不对
"dependencies": {
  "@commons/common": "file:../commons/common"  // 少了一级
}

// 正确 — 相对路径从当前 oh-package.json5 出发
"dependencies": {
  "@commons/common": "file:../../commons/common"
}
```

---

## 生成检查清单

- [ ] app.json5 有正确的 bundleName（反向域名格式）
- [ ] module.json5 type 正确（entry / har）
- [ ] 所有页面注册在 main_pages.json
- [ ] 所需权限配置在 requestPermissions
- [ ] EntryAbility 加载了正确的页面
- [ ] AppStorage 在 EntryAbility.onCreate 中初始化
- [ ] 多模块项目的 build-profile.json5 注册了所有模块
- [ ] 模块间 oh-package.json5 依赖路径正确

---

## 完整项目编排指南

当用户要求"从零搭建完整应用"时，本 skill 不仅生成项目骨架，还应引导按以下 6 步序列，读取其他 skill 的内容来生成完整项目代码。

### 6 步生成序列

| 步骤 | 内容 | 读取来源 |
|------|------|---------|
| **Step 1: 项目结构** | 配置文件骨架、EntryAbility、模块结构 | 本 skill 自身模板 |
| **Step 2: 数据层** | Model 类 + Service 网络请求 + BasicDataSource | 读取 `arkts-data-layer/SKILL.md`"数据模型"和"网络请求"节 |
| **Step 3: 状态管理** | 全局状态设计（AppStorage 初始化、key 常量） | 读取 `arkts-state-manager/SKILL.md`"@StorageLink"节 |
| **Step 4: 导航框架** | Navigation + Tabs 主框架、页面路由映射 | 读取 `arkts-navigation-builder/SKILL.md`"Tabs + Navigation 组合模式"节 |
| **Step 5: 业务页面** | 各功能页面 UI（列表、详情、搜索等） | 读取 `arkts-pattern-library/SKILL.md` 选择对应模式 + `arkts-component-builder/SKILL.md` UI 组件 |
| **Step 6: 动画润色** | 转场动画、交互反馈（可选） | 读取 `arkts-animation-builder/SKILL.md`"animateTo"和"transition"节 |

### 输出格式

按文件分块输出，每个文件标注路径：`// === 文件路径 ===`。按依赖顺序排列（配置 → Model → Service → State → Navigation → Page）。

> 完整路由矩阵见 `arkts-knowledge-verifier/references/skill-routing-guide.md`

---

## References

- `references/single-module-template.md` — 最小可运行项目的所有文件完整内容
- `references/multi-module-template.md` — 多模块架构的完整文件和配置
- `references/config-reference.md` — 所有配置文件的字段详细说明（含 SDK 版本格式）
- `references/audio-app-scaffold.md` — 音频应用脚手架：module.json5 模板、GlobalState 清单、层依赖、96 文件清单
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 **arkts-knowledge-verifier** skill
