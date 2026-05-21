# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 Ability Kit API 参考入口时，读取本文件。

## API 总入口

- 2 Ability Kit（程序框架服务）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts
- 2.2 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-c

## 主题到 API 的映射规则

### Stage模型能力的接口 相关接口

- 通用入口
  - 2.1.1 Stage模型能力的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/stage-model

### Ability基类 相关接口

- ArkTS API
  - 2.1.1.1 @ohos.app.ability.Ability (Ability基类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability

### Ability相关常量 相关接口

- ArkTS API
  - 2.1.1.2 @ohos.app.ability.AbilityConstant (Ability相关常量)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant

### UIAbility生命周期回调监听器 相关接口

- ArkTS API
  - 2.1.1.3 @ohos.app.ability.abilityLifecycleCallback (UIAbility生命周期回调监听器)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitylifecyclecallback

### AbilityStage组件管理器 相关接口

- ArkTS API
  - 2.1.1.4 @ohos.app.ability.AbilityStage (AbilityStage组件管理器)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage

### 支持业务操作自定义的ExtensionAbility组件 相关接口

- ArkTS API
  - 2.1.1.5 @ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-actionextensionability

### 应用工具类 相关接口

- ArkTS API
  - 2.1.1.6 @ohos.app.ability.application (应用工具类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application

### 应用进程状态变化监听器 相关接口

- ArkTS API
  - 2.1.1.7 @ohos.app.ability.ApplicationStateChangeCallback (应用进程状态变化监听器)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-applicationstatechangecallback

### 应用后台服务扩展组件 相关接口

- ArkTS API
  - 2.1.1.8 @ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability

### openAtomicService可选参数 相关接口

- ArkTS API
  - 2.1.1.9 @ohos.app.ability.AtomicServiceOptions (openAtomicService可选参数)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-atomicserviceoptions

### 自动填充框架 相关接口

- ArkTS API
  - 2.1.1.10 @ohos.app.ability.autoFillManager (自动填充框架)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autofillmanager

### 子进程基类 相关接口

- ArkTS API
  - 2.1.1.11 @ohos.app.ability.ChildProcess (子进程基类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess

### 子进程管理 相关接口

- ArkTS API
  - 2.1.1.12 @ohos.app.ability.childProcessManager (子进程管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessmanager

### 子进程参数 相关接口

- ArkTS API
  - 2.1.1.13 @ohos.app.ability.ChildProcessArgs (子进程参数)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessargs

### 子进程启动选项 相关接口

- ArkTS API
  - 2.1.1.14 @ohos.app.ability.ChildProcessOptions (子进程启动选项)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessoptions

### Ability公共模块 相关接口

- ArkTS API
  - 2.1.1.15 @ohos.app.ability.common (Ability公共模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common

### 拉起应用结果的操作类 相关接口

- ArkTS API
  - 2.1.1.16 @ohos.app.ability.CompletionHandler (拉起应用结果的操作类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-completionhandler

### 打开元服务结果的操作类 相关接口

- ArkTS API
  - 2.1.1.17 @ohos.app.ability.CompletionHandlerForAtomicService (打开元服务结果的操作类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/apis-app-ability-completionhandlerforatomicservice

### 拉起应用结果回调的操作类 相关接口

- ArkTS API
  - 2.1.1.18 @ohos.app.ability.CompletionHandlerForAbilityStartCallback (拉起应用结果回调的操作类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/p-ability-completionhandlerforabilitystartcallback

### Context相关常量 相关接口

- ArkTS API
  - 2.1.1.19 @ohos.app.ability.contextConstant (Context相关常量)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-contextconstant

### 可嵌入式UIAbility组件 相关接口

- ArkTS API
  - 2.1.1.20 @ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddableuiability

### 支持跨进程界面嵌入的ExtensionAbility组件 相关接口

- ArkTS API
  - 2.1.1.21 @ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability

### 系统环境变化监听器 相关接口

- ArkTS API
  - 2.1.1.22 @ohos.app.ability.EnvironmentCallback (系统环境变化监听器)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-environmentcallback

### 扩展能力基类 相关接口

- ArkTS API
  - 2.1.1.23 @ohos.app.ability.ExtensionAbility (扩展能力基类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability

### 意图框架基础定义 相关接口

- ArkTS API
  - 2.1.1.24 @ohos.app.ability.insightIntent (意图框架基础定义)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintent

### 意图执行上下文 相关接口

- ArkTS API
  - 2.1.1.25 @ohos.app.ability.InsightIntentContext (意图执行上下文)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentcontext

### 意图装饰器定义 相关接口

- ArkTS API
  - 2.1.1.26 @ohos.app.ability.InsightIntentDecorator (意图装饰器定义)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentdecorator

### @InsightIntentEntry的意图执行基类 相关接口

- ArkTS API
  - 2.1.1.27 @ohos.app.ability.InsightIntentEntryExecutor (@InsightIntentEntry的意图执行基类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintententryexecutor

### 意图执行基类 相关接口

- ArkTS API
  - 2.1.1.28 @ohos.app.ability.InsightIntentExecutor (意图执行基类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentexecutor

### 图片编辑和 PixelMap 操作

- ArkTS API
  - 2.1.1.29 @ohos.app.ability.PhotoEditorExtensionAbility (支持图片编辑能力的ExtensionAbility组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensionability

### openLink的可选参数 相关接口

- ArkTS API
  - 2.1.1.30 @ohos.app.ability.OpenLinkOptions (openLink的可选参数)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-openlinkoptions

### 支持分享详情页接入的ExtensionAbility组件 相关接口

- ArkTS API
  - 2.1.1.31 @ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-shareextensionability

### startAbility的可选参数 相关接口

- ArkTS API
  - 2.1.1.32 @ohos.app.ability.StartOptions (startAbility的可选参数)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-startoptions

### 带界面的应用组件 相关接口

- ArkTS API
  - 2.1.1.33 @ohos.app.ability.UIAbility (带界面的应用组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability

### 带界面的ExtensionAbility组件 相关接口

- ArkTS API
  - 2.1.1.34 @ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability

### UIExtensionAbility界面操作类 相关接口

- ArkTS API
  - 2.1.1.35 @ohos.app.ability.UIExtensionContentSession (UIExtensionAbility界面操作类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensioncontentsession

### sendable上下文管理 相关接口

- ArkTS API
  - 2.1.1.36 @ohos.app.ability.sendableContextManager (sendable上下文管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-sendablecontextmanager

### 启动框架配置信息 相关接口

- ArkTS API
  - 2.1.1.37 @ohos.app.appstartup.StartupConfig (启动框架配置信息)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfig

### 启动框架配置 相关接口

- ArkTS API
  - 2.1.1.38 @ohos.app.appstartup.StartupConfigEntry (启动框架配置)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfigentry

### 启动框架任务监听器 相关接口

- ArkTS API
  - 2.1.1.39 @ohos.app.appstartup.StartupListener (启动框架任务监听器)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuplistener

### 启动框架管理能力 相关接口

- ArkTS API
  - 2.1.1.40 @ohos.app.appstartup.startupManager (启动框架管理能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupmanager

### 启动框架任务 相关接口

- ArkTS API
  - 2.1.1.41 @ohos.app.appstartup.StartupTask (启动框架任务)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuptask

### 开机自启管理能力 相关接口

- ArkTS API
  - 2.1.1.42 @ohos.app.ability.autoStartupManager (开机自启管理能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autostartupmanager

### 流转/协同管理 相关接口

- ArkTS API
  - 2.1.1.43 @ohos.continuation.continuationManager (流转/协同管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager

### continuation 相关接口

- 通用入口
  - 2.1.1.44 continuation：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/stage-model-continuation
  - 2.1.5.12 continuation：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability--continuation

### ContinuationExtraParams 相关接口

- ArkTS API
  - 2.1.1.44.1 ContinuationExtraParams：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams

### ContinuationResult 相关接口

- ArkTS API
  - 2.1.1.44.2 ContinuationResult：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult

### FA模型能力的接口 相关接口

- 通用入口
  - 2.1.2 FA模型能力的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fa-model

### Ability模块 相关接口

- ArkTS API
  - 2.1.2.1 @ohos.ability.ability (Ability模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-ability

### FeatureAbility模块 相关接口

- ArkTS API
  - 2.1.2.2 @ohos.ability.featureAbility (FeatureAbility模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability

### ParticleAbility模块 相关接口

- ArkTS API
  - 2.1.2.3 @ohos.ability.particleAbility (ParticleAbility模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-particleability

### ability 相关接口

- 通用入口
  - 2.1.2.4 ability：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fa-model-ability
  - 2.1.4.1 ability：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability
  - 2.1.5.11 ability：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-deprecated

### DataAbilityOperation 相关接口

- ArkTS API
  - 2.1.2.4.1 DataAbilityOperation：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityoperation

### DataAbilityResult 相关接口

- ArkTS API
  - 2.1.2.4.2 DataAbilityResult：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityresult

### StartAbilityParameter 相关接口

- ArkTS API
  - 2.1.2.4.3 StartAbilityParameter：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-startabilityparameter

### app 相关接口

- 通用入口
  - 2.1.2.5 app：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/app

### FA模型的上下文基类 相关接口

- ArkTS API
  - 2.1.2.5.2 Context (FA模型的上下文基类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context

### 推荐 相关接口

- 通用入口
  - 2.1.3 通用能力的接口(推荐)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/both-models

### 程序访问控制管理 相关接口

- ArkTS API
  - 2.1.3.1 @ohos.abilityAccessCtrl (程序访问控制管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl

### 锁屏敏感数据管理 相关接口

- ArkTS API
  - 2.1.3.2 @ohos.ability.screenLockFileManager (锁屏敏感数据管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screenlockfilemanager

### Ability信息管理 相关接口

- ArkTS API
  - 2.1.3.3 @ohos.app.ability.abilityManager (Ability信息管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitymanager

### 应用管理 相关接口

- ArkTS API
  - 2.1.3.4 @ohos.app.ability.appManager (应用管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appmanager
  - 2.1.5.10 @system.package (应用管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-package

### 应用故障恢复 相关接口

- ArkTS API
  - 2.1.3.5 @ohos.app.ability.appRecovery (应用故障恢复)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-apprecovery

### 环境变量 相关接口

- ArkTS API
  - 2.1.3.6 @ohos.app.ability.Configuration (环境变量)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration

### 环境变量相关的常量定义 相关接口

- ArkTS API
  - 2.1.3.7 @ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant

### 跨端迁移 相关接口

- ArkTS API
  - 2.1.3.8 @ohos.app.ability.continueManager (跨端迁移)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-continuemanager

### DataUriUtils模块 相关接口

- ArkTS API
  - 2.1.3.9 @ohos.app.ability.dataUriUtils (DataUriUtils模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-datauriutils
  - 2.1.5.1 @ohos.ability.dataUriUtils (DataUriUtils模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-datauriutils

### dialogRequest模块 相关接口

- ArkTS API
  - 2.1.3.10 @ohos.app.ability.dialogRequest (dialogRequest模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-dialogrequest

### 错误码与异常定位

- 通用入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts-errcode
  - 2.3.1 元能力子系统错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ability
  - 2.3.2 DistributedSchedule错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule
  - 2.3.3 包管理子系统通用错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bundle
  - 2.3.4 访问控制错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token
  - 2.3.5 锁屏敏感数据管理错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-screenlockfilemanager

- ArkTS API
  - 2.1.3.11 @ohos.app.ability.errorManager (错误管理模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-errormanager
  - 2.1.4.2.14 ErrorObserver：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-errorobserver
  - 2.1.5.2 @ohos.ability.errorCode (ErrorCode)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-errorcode

### Kiosk模式管理 相关接口

- ArkTS API
  - 2.1.3.12 @ohos.app.ability.kioskManager (Kiosk模式管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-kioskmanager

### Want 相关接口

- ArkTS API
  - 2.1.3.13 @ohos.app.ability.Want (Want)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want
  - 2.1.5.7 @ohos.application.Want (Want)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want
  - 2.1.5.11.1 Want：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want

### WantAgent模块 相关接口

- ArkTS API
  - 2.1.3.14 @ohos.app.ability.wantAgent (WantAgent模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent
  - 2.1.5.8 @ohos.wantAgent (WantAgent模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wantagent

### Want常量 相关接口

- ArkTS API
  - 2.1.3.15 @ohos.app.ability.wantConstant (Want常量)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantconstant

### 应用程序包管理模块 相关接口

- ArkTS API
  - 2.1.3.16 @ohos.bundle.bundleManager (应用程序包管理模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager

### 默认应用管理 相关接口

- ArkTS API
  - 2.1.3.17 @ohos.bundle.defaultAppManager (默认应用管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-defaultappmanager

### launcherBundleManager模块 相关接口

- ArkTS API
  - 2.1.3.18 @ohos.bundle.launcherBundleManager (launcherBundleManager模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-launcherbundlemanager

### overlay模块 相关接口

- ArkTS API
  - 2.1.3.19 @ohos.bundle.overlay (overlay模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-overlay

### shortcutManager模块 相关接口

- ArkTS API
  - 2.1.3.20 @ohos.bundle.shortcutManager (shortcutManager模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-shortcutmanager

### 接口依赖的元素及定义 相关接口

- 通用入口
  - 2.1.4 接口依赖的元素及定义：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-api-interface-depend

### AbilityResult 相关接口

- ArkTS API
  - 2.1.4.1.1 AbilityResult：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-abilityresult

### DataAbilityHelper 相关接口

- ArkTS API
  - 2.1.4.1.3 DataAbilityHelper：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper

### application 相关接口

- 通用入口
  - 2.1.4.2 application：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts-application

### AbilityMonitor 相关接口

- ArkTS API
  - 2.1.4.2.1 AbilityMonitor：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitymonitor

### AbilityStageContext 相关接口

- ArkTS API
  - 2.1.4.2.3 AbilityStageContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext

### AbilityStageMonitor 相关接口

- ArkTS API
  - 2.1.4.2.4 AbilityStageMonitor：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagemonitor

### AbilityStartCallback 相关接口

- ArkTS API
  - 2.1.4.2.5 AbilityStartCallback：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystartcallback

### AbilityStateData 相关接口

- ArkTS API
  - 2.1.4.2.6 AbilityStateData：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystatedata

### 应用上下文 相关接口

- ArkTS API
  - 2.1.4.2.7 ApplicationContext (应用上下文)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext

### ApplicationStateObserver 相关接口

- ArkTS API
  - 2.1.4.2.8 ApplicationStateObserver：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationstateobserver

### 应用后台服务扩展组件上下文 相关接口

- 通用入口
  - 2.1.4.2.9 AppServiceExtensionContext (应用后台服务扩展组件上下文)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-apis-inner-application-appserviceextensioncontext

### AppStateData 相关接口

- ArkTS API
  - 2.1.4.2.10 AppStateData：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-appstatedata

### BaseContext 相关接口

- ArkTS API
  - 2.1.4.2.11 BaseContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext

### Stage模型的上下文基类 相关接口

- ArkTS API
  - 2.1.4.2.12 Context (Stage模型的上下文基类)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context

### EmbeddableUIAbilityContext 相关接口

- 通用入口
  - 2.1.4.2.13 EmbeddableUIAbilityContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-apis-inner-application-embeddableuiabilitycontext

### EventHub 相关接口

- ArkTS API
  - 2.1.4.2.15 EventHub：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub

### ExtensionContext 相关接口

- ArkTS API
  - 2.1.4.2.16 ExtensionContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext

### Kiosk状态信息 相关接口

- ArkTS API
  - 2.1.4.2.17 KioskStatus (Kiosk状态信息)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-kioskstatus

### LoopObserver 相关接口

- ArkTS API
  - 2.1.4.2.18 LoopObserver：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-loopobserver

### ProcessInformation 相关接口

- ArkTS API
  - 2.1.4.2.19 ProcessInformation：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processinformation

### UIAbilityContext 相关接口

- ArkTS API
  - 2.1.4.2.21 UIAbilityContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext

### UIExtensionContext 相关接口

- ArkTS API
  - 2.1.4.2.22 UIExtensionContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext

### UIServiceExtensionConnectCallback 相关接口

- 通用入口
  - 2.1.4.2.23 UIServiceExtensionConnectCallback：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nner-application-uiserviceextensionconnectcallback

### UIServiceProxy 相关接口

- ArkTS API
  - 2.1.4.2.24 UIServiceProxy：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiserviceproxy

### ProcessData 相关接口

- ArkTS API
  - 2.1.4.2.25 ProcessData：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processdata

### PhotoEditorExtensionContext 相关接口

- ArkTS API
  - 2.1.4.2.26 PhotoEditorExtensionContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensioncontext

### SendableContext 相关接口

- ArkTS API
  - 2.1.4.2.27 SendableContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext

### bundleManager 相关接口

- 通用入口
  - 2.1.4.3 bundleManager：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/bundlemanager

### ElementName 相关接口

- ArkTS API
  - 2.1.4.3.4 ElementName：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-elementname
  - 2.1.5.13.5 ElementName：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-elementname

### 元数据 / EXIF / Picture / AuxiliaryPicture

- ArkTS API
  - 2.1.4.3.8 Metadata：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-metadata

### Skill 相关接口

- ArkTS API
  - 2.1.4.3.10 Skill：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-skill

### security 相关接口

- 通用入口
  - 2.1.4.4 security：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-security

### PermissionRequestResult 相关接口

- ArkTS API
  - 2.1.4.4.1 PermissionRequestResult：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-permissionrequestresult

### wantAgent 相关接口

- 通用入口
  - 2.1.4.5 wantAgent：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wantagent

### 已停止维护的接口 相关接口

- 通用入口
  - 2.1.5 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts-dep

### wantConstant 相关接口

- ArkTS API
  - 2.1.5.3 @ohos.ability.wantConstant (wantConstant)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-wantconstant

### appManager 相关接口

- ArkTS API
  - 2.1.5.4 @ohos.application.appManager (appManager)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-appmanager

### Configuration 相关接口

- ArkTS API
  - 2.1.5.5 @ohos.application.Configuration (Configuration)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configuration

### ConfigurationConstant 相关接口

- ArkTS API
  - 2.1.5.6 @ohos.application.ConfigurationConstant (ConfigurationConstant)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configurationconstant

### Bundle模块 相关接口

- ArkTS API
  - 2.1.5.9 @ohos.bundle (Bundle模块)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle

### bundle 相关接口

- 通用入口
  - 2.1.5.13 bundle：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/bundle

### CustomizeData 相关接口

- ArkTS API
  - 2.1.5.13.4 CustomizeData：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-customizedata

### AbilityAccessControl 相关接口

- C API
  - 2.2.1.1 AbilityAccessControl：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityaccesscontrol

### AbilityBase 相关接口

- C API
  - 2.2.1.2 AbilityBase：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase

### AbilityRuntime 相关接口

- C API
  - 2.2.1.3 AbilityRuntime：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime

### ChildProcess 相关接口

- C API
  - 2.2.1.5 ChildProcess：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess

## 直接映射

- `Stage模型能力的接口`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/stage-model
- `Ability基类`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability
- `Ability相关常量`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant
- `UIAbility生命周期回调监听器`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitylifecyclecallback
- `AbilityStage组件管理器`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage
- `支持业务操作自定义的ExtensionAbility组件`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-actionextensionability
- `应用工具类`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application
- `应用进程状态变化监听器`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-applicationstatechangecallback
- `应用后台服务扩展组件`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability
- `openAtomicService可选参数`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-atomicserviceoptions
- `自动填充框架`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autofillmanager
- `子进程基类`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 Ability Kit（程序框架服务）、Stage模型能力的接口、Ability基类、Ability相关常量、UIAbility生命周期回调监听器 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
