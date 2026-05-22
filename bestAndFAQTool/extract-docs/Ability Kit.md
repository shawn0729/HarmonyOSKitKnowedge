# 1 Ability Kit（程序框架服务）开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-kit

## 1.1 Ability Kit简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilitykit-overview

## 1.2 应用模型:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-models

## 1.3 Stage模型开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stage-model-development

### 1.3.1 Stage模型开发概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stage-model-development-overview

### 1.3.2 Stage模型应用组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stage-model-application-components

#### 1.3.2.1 应用/组件级配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-component-configuration-stage

#### 1.3.2.2 UIAbility组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability

##### 1.3.2.2.1 UIAbility组件概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-overview

##### 1.3.2.2.2 UIAbility组件生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-lifecycle

##### 1.3.2.2.3 UIAbility组件启动模式:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type

##### 1.3.2.2.4 UIAbility组件基本用法:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-usage

##### 1.3.2.2.5 UIAbility组件与UI的数据同步:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-data-sync-with-ui

##### 1.3.2.2.6 启动应用内的UIAbility组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-intra-device-interaction

##### 1.3.2.2.7 通过Call调用实现多端协同:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-cross-device-interaction

##### 1.3.2.2.8 UIAbility备份恢复:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-recover-guideline

#### 1.3.2.3 ExtensionAbility组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview

##### 1.3.2.3.1 EmbeddedUIExtensionAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/embeddeduiextensionability

##### 1.3.2.3.2 使用AppServiceExtensionAbility组件实现后台服务:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-service-extension-ability

#### 1.3.2.4 AbilityStage组件管理器:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/abilitystage

#### 1.3.2.5 应用上下文Context:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-stage

#### 1.3.2.6 信息传递载体Want:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/want

##### 1.3.2.6.1 Want概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/want-overview

##### 1.3.2.6.2 显式Want与隐式Want匹配规则:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/explicit-implicit-want-mappings

##### 1.3.2.6.3 使用显式Want启动应用组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-startup-with-explicit-want

##### 1.3.2.6.4 常见action与entities（不推荐使用）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/actions-entities

#### 1.3.2.7 组件启动规则（Stage模型）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules

#### 1.3.2.8 应用启动框架AppStartup:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup

#### 1.3.2.9 应用预加载:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/preload-application

#### 1.3.2.10 获取应用异常退出原因:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-exit-info-record

#### 1.3.2.11 获取/设置环境变量:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes

### 1.3.3 应用间跳转:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/inter-app-redirection

#### 1.3.3.1 应用间跳转概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/link-between-apps-overview

#### 1.3.3.2 拉起指定应用:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/directional-redirection

##### 1.3.3.2.1 拉起指定应用概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-startup-overview

##### 1.3.3.2.2 （可选）使用canOpenLink判断应用是否可访问:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canopenlink

##### 1.3.3.2.3 获取目标应用的URL信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtaining-target-app-url-info

##### 1.3.3.2.4 使用App Linking实现应用间跳转:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-linking-startup

##### 1.3.3.2.5 使用Deep Linking实现应用间跳转:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-linking-startup

##### 1.3.3.2.6 显式Want跳转切换应用链接跳转适配指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-startup-adjust

##### 1.3.3.2.7 应用链接说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-uri-config

#### 1.3.3.3 拉起指定类型的应用:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/specified-type-app-redirection

##### 1.3.3.3.1 拉起指定类型的应用概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-intent-panel

##### 1.3.3.3.2 拉起导航类应用（startAbilityByType）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-navigation-apps

##### 1.3.3.3.3 拉起邮件类应用（startAbilityByType）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-email-apps

##### 1.3.3.3.4 拉起邮件类应用（mailto方式）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-email-apps-by-mailto

##### 1.3.3.3.5 拉起金融类应用（startAbilityByType）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-finance-apps

##### 1.3.3.3.6 拉起航班类应用（startAbilityByType）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-flight-apps

##### 1.3.3.3.7 拉起快递类应用（startAbilityByType）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-express-apps

##### 1.3.3.3.8 拉起图片编辑类应用（startAbilityByType）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/photoeditorextensionability

##### 1.3.3.3.9 拉起文件处理类应用（startAbility）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/file-processing-apps-startup

#### 1.3.3.4 拉起系统应用:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-app-startup

### 1.3.4 进程模型:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/process-model-stage

### 1.3.5 线程模型:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/thread-model-stage

### 1.3.6 Stage模型应用配置文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/config-file-stage

### 1.3.7 意图框架开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent

#### 1.3.7.1 意图框架概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-overview

#### 1.3.7.2 开发意图:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-development

##### 1.3.7.2.1 意图开发概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-definition

##### 1.3.7.2.2 使用配置文件开发意图:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-config-development

##### 1.3.7.2.3 使用装饰器开发意图:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-decorator-development

##### 1.3.7.2.4 附录：标准意图接入规范:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-access-specifications

#### 1.3.7.3 调试意图:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/insight-intent-debug

## 1.4 FA模型开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fa-model-development

### 1.4.1 FA模型开发概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fa-model-development-overview

### 1.4.2 FA模型应用组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fa-model-application-components

#### 1.4.2.1 应用/组件级配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-component-configuration-fa

#### 1.4.2.2 PageAbility组件开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pageability

##### 1.4.2.2.1 PageAbility组件概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pageability-overview

##### 1.4.2.2.2 PageAbility组件配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pageability-configuration

##### 1.4.2.2.3 PageAbility的生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pageability-lifecycle

##### 1.4.2.2.4 PageAbility的启动模式:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pageability-launch-type

##### 1.4.2.2.5 创建PageAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-pageability

##### 1.4.2.2.6 启动本地PageAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-local-pageability

##### 1.4.2.2.7 停止PageAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/stop-pageability

##### 1.4.2.2.8 启动指定页面:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-page

##### 1.4.2.2.9 窗口属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-properties

##### 1.4.2.2.10 申请授权:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/request-permissions

##### 1.4.2.2.11 跳转规则:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/redirection-rules

#### 1.4.2.3 ServiceAbility组件开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serviceability

##### 1.4.2.3.1 ServiceAbility组件概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serviceability-overview

##### 1.4.2.3.2 ServiceAbility组件配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serviceability-configuration

##### 1.4.2.3.3 ServiceAbility的生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serviceability-lifecycle

##### 1.4.2.3.4 创建ServiceAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-serviceability

##### 1.4.2.3.5 启动ServiceAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-serviceability

##### 1.4.2.3.6 连接ServiceAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/connect-serviceability

#### 1.4.2.4 DataAbility组件开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability

##### 1.4.2.4.1 DataAbility组件概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-overview

##### 1.4.2.4.2 DataAbility组件配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-configuration

##### 1.4.2.4.3 DataAbility的生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-lifecycle

##### 1.4.2.4.4 创建DataAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/create-dataability

##### 1.4.2.4.5 启动DataAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-dataability

##### 1.4.2.4.6 访问DataAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/access-dataability

##### 1.4.2.4.7 DataAbility权限控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/dataability-permission-control

#### 1.4.2.5 FA模型的Context:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-context-fa

#### 1.4.2.6 信息传递载体Want:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/want-fa

#### 1.4.2.7 组件启动规则（FA模型）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/component-startup-rules-fa

### 1.4.3 进程模型概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/process-model-fa

### 1.4.4 线程模型:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/thread-model-fa

### 1.4.5 FA模型应用配置文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/config-file-fa

## 1.5 Native子进程开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-childprocess-development

### 1.5.1 创建/终止Native子进程（C/C++）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi-nativechildprocess-development-guideline

### 1.5.2 获取Native子进程退出信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/capi-nativechildprocess-exit-info

## 1.6 Ability Kit术语:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-terminology

---

# 2 Ability Kit（程序框架服务）API参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-api

## 2.1 ArkTS API:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts

### 2.1.1 Stage模型能力的接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/stage-model

#### 2.1.1.1 @ohos.app.ability.Ability (Ability基类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-ability

#### 2.1.1.2 @ohos.app.ability.AbilityConstant (Ability相关常量):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilityconstant

#### 2.1.1.3 @ohos.app.ability.abilityLifecycleCallback (UIAbility生命周期回调监听器):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitylifecyclecallback

#### 2.1.1.4 @ohos.app.ability.AbilityStage (AbilityStage组件管理器):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitystage

#### 2.1.1.5 @ohos.app.ability.ActionExtensionAbility (支持业务操作自定义的ExtensionAbility组件):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-actionextensionability

#### 2.1.1.6 @ohos.app.ability.application (应用工具类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application

#### 2.1.1.7 @ohos.app.ability.ApplicationStateChangeCallback (应用进程状态变化监听器):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-applicationstatechangecallback

#### 2.1.1.8 @ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability

#### 2.1.1.9 @ohos.app.ability.AtomicServiceOptions (openAtomicService可选参数):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-atomicserviceoptions

#### 2.1.1.10 @ohos.app.ability.autoFillManager (自动填充框架):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autofillmanager

#### 2.1.1.11 @ohos.app.ability.ChildProcess (子进程基类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocess

#### 2.1.1.12 @ohos.app.ability.childProcessManager (子进程管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessmanager

#### 2.1.1.13 @ohos.app.ability.ChildProcessArgs (子进程参数):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessargs

#### 2.1.1.14 @ohos.app.ability.ChildProcessOptions (子进程启动选项):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-childprocessoptions

#### 2.1.1.15 @ohos.app.ability.common (Ability公共模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-common

#### 2.1.1.16 @ohos.app.ability.CompletionHandler (拉起应用结果的操作类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-completionhandler

#### 2.1.1.17 @ohos.app.ability.CompletionHandlerForAtomicService (打开元服务结果的操作类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/apis-app-ability-completionhandlerforatomicservice

#### 2.1.1.18 @ohos.app.ability.CompletionHandlerForAbilityStartCallback (拉起应用结果回调的操作类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/p-ability-completionhandlerforabilitystartcallback

#### 2.1.1.19 @ohos.app.ability.contextConstant (Context相关常量):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-contextconstant

#### 2.1.1.20 @ohos.app.ability.EmbeddableUIAbility (可嵌入式UIAbility组件):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddableuiability

#### 2.1.1.21 @ohos.app.ability.EmbeddedUIExtensionAbility (支持跨进程界面嵌入的ExtensionAbility组件):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-embeddeduiextensionability

#### 2.1.1.22 @ohos.app.ability.EnvironmentCallback (系统环境变化监听器):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-environmentcallback

#### 2.1.1.23 @ohos.app.ability.ExtensionAbility (扩展能力基类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-extensionability

#### 2.1.1.24 @ohos.app.ability.insightIntent (意图框架基础定义):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintent

#### 2.1.1.25 @ohos.app.ability.InsightIntentContext (意图执行上下文):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentcontext

#### 2.1.1.26 @ohos.app.ability.InsightIntentDecorator (意图装饰器定义):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentdecorator

#### 2.1.1.27 @ohos.app.ability.InsightIntentEntryExecutor (@InsightIntentEntry的意图执行基类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintententryexecutor

#### 2.1.1.28 @ohos.app.ability.InsightIntentExecutor (意图执行基类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-insightintentexecutor

#### 2.1.1.29 @ohos.app.ability.PhotoEditorExtensionAbility (支持图片编辑能力的ExtensionAbility组件):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensionability

#### 2.1.1.30 @ohos.app.ability.OpenLinkOptions (openLink的可选参数):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-openlinkoptions

#### 2.1.1.31 @ohos.app.ability.ShareExtensionAbility (支持分享详情页接入的ExtensionAbility组件):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-shareextensionability

#### 2.1.1.32 @ohos.app.ability.StartOptions (startAbility的可选参数):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-startoptions

#### 2.1.1.33 @ohos.app.ability.UIAbility (带界面的应用组件):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability

#### 2.1.1.34 @ohos.app.ability.UIExtensionAbility (带界面的ExtensionAbility组件):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability

#### 2.1.1.35 @ohos.app.ability.UIExtensionContentSession (UIExtensionAbility界面操作类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensioncontentsession

#### 2.1.1.36 @ohos.app.ability.sendableContextManager (sendable上下文管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-sendablecontextmanager

#### 2.1.1.37 @ohos.app.appstartup.StartupConfig (启动框架配置信息):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfig

#### 2.1.1.38 @ohos.app.appstartup.StartupConfigEntry (启动框架配置):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupconfigentry

#### 2.1.1.39 @ohos.app.appstartup.StartupListener (启动框架任务监听器):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuplistener

#### 2.1.1.40 @ohos.app.appstartup.startupManager (启动框架管理能力):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startupmanager

#### 2.1.1.41 @ohos.app.appstartup.StartupTask (启动框架任务):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-appstartup-startuptask

#### 2.1.1.42 @ohos.app.ability.autoStartupManager (开机自启管理能力):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-autostartupmanager

#### 2.1.1.43 @ohos.continuation.continuationManager (流转/协同管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationmanager

#### 2.1.1.44 continuation:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/stage-model-continuation

##### 2.1.1.44.1 ContinuationExtraParams:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationextraparams

##### 2.1.1.44.2 ContinuationResult:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-continuation-continuationresult

### 2.1.2 FA模型能力的接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fa-model

#### 2.1.2.1 @ohos.ability.ability (Ability模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-ability

#### 2.1.2.2 @ohos.ability.featureAbility (FeatureAbility模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability

#### 2.1.2.3 @ohos.ability.particleAbility (ParticleAbility模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-particleability

#### 2.1.2.4 ability:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fa-model-ability

##### 2.1.2.4.1 DataAbilityOperation:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityoperation

##### 2.1.2.4.2 DataAbilityResult:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityresult

##### 2.1.2.4.3 StartAbilityParameter:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-startabilityparameter

#### 2.1.2.5 app:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/app

##### 2.1.2.5.1 AppVersionInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-appversioninfo

##### 2.1.2.5.2 Context (FA模型的上下文基类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-context

##### 2.1.2.5.3 ProcessInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-app-processinfo

### 2.1.3 通用能力的接口(推荐):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/both-models

#### 2.1.3.1 @ohos.abilityAccessCtrl (程序访问控制管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-abilityaccessctrl

#### 2.1.3.2 @ohos.ability.screenLockFileManager (锁屏敏感数据管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screenlockfilemanager

#### 2.1.3.3 @ohos.app.ability.abilityManager (Ability信息管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-abilitymanager

#### 2.1.3.4 @ohos.app.ability.appManager (应用管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appmanager

#### 2.1.3.5 @ohos.app.ability.appRecovery (应用故障恢复):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-apprecovery

#### 2.1.3.6 @ohos.app.ability.Configuration (环境变量):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configuration

#### 2.1.3.7 @ohos.app.ability.ConfigurationConstant (环境变量相关的常量定义):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant

#### 2.1.3.8 @ohos.app.ability.continueManager (跨端迁移):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-continuemanager

#### 2.1.3.9 @ohos.app.ability.dataUriUtils (DataUriUtils模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-datauriutils

#### 2.1.3.10 @ohos.app.ability.dialogRequest (dialogRequest模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-dialogrequest

#### 2.1.3.11 @ohos.app.ability.errorManager (错误管理模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-errormanager

#### 2.1.3.12 @ohos.app.ability.kioskManager (Kiosk模式管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-kioskmanager

#### 2.1.3.13 @ohos.app.ability.Want (Want):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want

#### 2.1.3.14 @ohos.app.ability.wantAgent (WantAgent模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantagent

#### 2.1.3.15 @ohos.app.ability.wantConstant (Want常量):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-wantconstant

#### 2.1.3.16 @ohos.bundle.bundleManager (应用程序包管理模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager

#### 2.1.3.17 @ohos.bundle.defaultAppManager (默认应用管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-defaultappmanager

#### 2.1.3.18 @ohos.bundle.launcherBundleManager (launcherBundleManager模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-launcherbundlemanager

#### 2.1.3.19 @ohos.bundle.overlay (overlay模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-overlay

#### 2.1.3.20 @ohos.bundle.shortcutManager (shortcutManager模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-shortcutmanager

### 2.1.4 接口依赖的元素及定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-api-interface-depend

#### 2.1.4.1 ability:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability

##### 2.1.4.1.1 AbilityResult:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-abilityresult

##### 2.1.4.1.2 ConnectOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-connectoptions

##### 2.1.4.1.3 DataAbilityHelper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-dataabilityhelper

#### 2.1.4.2 application:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts-application

##### 2.1.4.2.1 AbilityMonitor:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitymonitor

##### 2.1.4.2.2 AbilityRunningInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilityrunninginfo

##### 2.1.4.2.3 AbilityStageContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagecontext

##### 2.1.4.2.4 AbilityStageMonitor:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystagemonitor

##### 2.1.4.2.5 AbilityStartCallback:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystartcallback

##### 2.1.4.2.6 AbilityStateData:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-abilitystatedata

##### 2.1.4.2.7 ApplicationContext (应用上下文):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationcontext

##### 2.1.4.2.8 ApplicationStateObserver:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-applicationstateobserver

##### 2.1.4.2.9 AppServiceExtensionContext (应用后台服务扩展组件上下文):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-apis-inner-application-appserviceextensioncontext

##### 2.1.4.2.10 AppStateData:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-appstatedata

##### 2.1.4.2.11 BaseContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-basecontext

##### 2.1.4.2.12 Context (Stage模型的上下文基类):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-context

##### 2.1.4.2.13 EmbeddableUIAbilityContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-apis-inner-application-embeddableuiabilitycontext

##### 2.1.4.2.14 ErrorObserver:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-errorobserver

##### 2.1.4.2.15 EventHub:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-eventhub

##### 2.1.4.2.16 ExtensionContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext

##### 2.1.4.2.17 KioskStatus (Kiosk状态信息):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-kioskstatus

##### 2.1.4.2.18 LoopObserver:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-loopobserver

##### 2.1.4.2.19 ProcessInformation:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processinformation

##### 2.1.4.2.20 ProcessRunningInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processrunninginfo

##### 2.1.4.2.21 UIAbilityContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext

##### 2.1.4.2.22 UIExtensionContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext

##### 2.1.4.2.23 UIServiceExtensionConnectCallback:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nner-application-uiserviceextensionconnectcallback

##### 2.1.4.2.24 UIServiceProxy:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiserviceproxy

##### 2.1.4.2.25 ProcessData:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-processdata

##### 2.1.4.2.26 PhotoEditorExtensionContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-photoeditorextensioncontext

##### 2.1.4.2.27 SendableContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-sendablecontext

#### 2.1.4.3 bundleManager:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/bundlemanager

##### 2.1.4.3.1 AbilityInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-abilityinfo

##### 2.1.4.3.2 ApplicationInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-applicationinfo

##### 2.1.4.3.3 BundleInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo

##### 2.1.4.3.4 ElementName:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-elementname

##### 2.1.4.3.5 ExtensionAbilityInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-extensionabilityinfo

##### 2.1.4.3.6 HapModuleInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo

##### 2.1.4.3.7 LauncherAbilityInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-launcherabilityinfo

##### 2.1.4.3.8 Metadata:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-metadata

##### 2.1.4.3.9 OverlayModuleInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-overlaymoduleinfo

##### 2.1.4.3.10 Skill:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-skill

##### 2.1.4.3.11 ShortcutInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-shortcutinfo

#### 2.1.4.4 security:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-security

##### 2.1.4.4.1 PermissionRequestResult:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-permissionrequestresult

#### 2.1.4.5 wantAgent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wantagent

##### 2.1.4.5.1 TriggerInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-triggerinfo

##### 2.1.4.5.2 WantAgentInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-wantagent-wantagentinfo

### 2.1.5 已停止维护的接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts-dep

#### 2.1.5.1 @ohos.ability.dataUriUtils (DataUriUtils模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-datauriutils

#### 2.1.5.2 @ohos.ability.errorCode (ErrorCode):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-errorcode

#### 2.1.5.3 @ohos.ability.wantConstant (wantConstant):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-wantconstant

#### 2.1.5.4 @ohos.application.appManager (appManager):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-appmanager

#### 2.1.5.5 @ohos.application.Configuration (Configuration):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configuration

#### 2.1.5.6 @ohos.application.ConfigurationConstant (ConfigurationConstant):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configurationconstant

#### 2.1.5.7 @ohos.application.Want (Want):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-want

#### 2.1.5.8 @ohos.wantAgent (WantAgent模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-wantagent

#### 2.1.5.9 @ohos.bundle (Bundle模块):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle

#### 2.1.5.10 @system.package (应用管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-package

#### 2.1.5.11 ability:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-deprecated

##### 2.1.5.11.1 Want:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-want

#### 2.1.5.12 continuation:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability--continuation

#### 2.1.5.13 bundle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/bundle

##### 2.1.5.13.1 AbilityInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo

##### 2.1.5.13.2 ApplicationInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo

##### 2.1.5.13.3 BundleInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo

##### 2.1.5.13.4 CustomizeData:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-customizedata

##### 2.1.5.13.5 ElementName:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-elementname

##### 2.1.5.13.6 HapModuleInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-hapmoduleinfo

##### 2.1.5.13.7 ModuleInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-moduleinfo

##### 2.1.5.13.8 ShortcutInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-shortcutinfo

## 2.2 C API:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-c

### 2.2.1 模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-module

#### 2.2.1.1 AbilityAccessControl:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityaccesscontrol

#### 2.2.1.2 AbilityBase:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase

#### 2.2.1.3 AbilityRuntime:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime

#### 2.2.1.4 Native_Bundle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle

#### 2.2.1.5 ChildProcess:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-childprocess

### 2.2.2 头文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-headerfile

#### 2.2.2.1 ability_access_control.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-access-control-h

#### 2.2.2.2 ability_base_common.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-base-common-h

#### 2.2.2.3 ability_runtime_common.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h

#### 2.2.2.4 application_context.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-application-context-h

#### 2.2.2.5 context_constant.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-context-constant-h

#### 2.2.2.6 native_child_process.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-child-process-h

#### 2.2.2.7 native_interface_bundle.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-bundle-h

#### 2.2.2.8 start_options.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-start-options-h

#### 2.2.2.9 want.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-want-h

#### 2.2.2.10 ability_resource_info.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-resource-info-h

#### 2.2.2.11 bundle_manager_common.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-bundle-manager-common-h

### 2.2.3 结构体:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-struct

#### 2.2.3.1 AbilityBase_Element:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase-element

#### 2.2.3.2 AbilityBase_Want:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilitybase-want

#### 2.2.3.3 AbilityRuntime_StartOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-startoptions

#### 2.2.3.4 NativeChildProcess_Fd:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fd

#### 2.2.3.5 NativeChildProcess_FdList:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-fdlist

#### 2.2.3.6 NativeChildProcess_Options:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-options

#### 2.2.3.7 NativeChildProcess_Args:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativechildprocess-args

#### 2.2.3.8 Ability_ChildProcessConfigs:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-childprocessconfigs

#### 2.2.3.9 OH_NativeBundle_ApplicationInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-applicationinfo

#### 2.2.3.10 OH_NativeBundle_ElementName:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-elementname

#### 2.2.3.11 OH_NativeBundle_Metadata:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-metadata

#### 2.2.3.12 OH_NativeBundle_ModuleMetadata:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-bundle-oh-nativebundle-modulemetadata

#### 2.2.3.13 OH_NativeBundle_AbilityResourceInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-native-bundle-oh-nativebundle-abilityresourceinfo

## 2.3 错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ability-arkts-errcode

### 2.3.1 元能力子系统错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ability

### 2.3.2 DistributedSchedule错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedschedule

### 2.3.3 包管理子系统通用错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bundle

### 2.3.4 访问控制错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-access-token

### 2.3.5 锁屏敏感数据管理错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-screenlockfilemanager

---

# 3 最佳实践-程序包结构:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-package-structure

## 3.1 桌面快捷方式:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-desktop-shortcuts

## 3.2 跨模块资源访问:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-module-resource-access

## 3.3 Native侧跨HAR/HSP模块接口调用:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-module-reference

## 3.4 应用图标配置与开发:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-icon-configuration

---

# 4 最佳实践-程序框架:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-program-framework

## 4.1 应用间跳转实践概览:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-link-between-apps-overview

## 4.2 社交分享跳转:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-social-share

## 4.3 广告跳转:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ads-jump

## 4.4 特殊文本识别跳转:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-special-text-recognition

## 4.5 Web和应用的跳转与拉起:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-app-jump-and-pull-up

---

# 5 FAQ-程序包结构:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure

## 5.1 HSP打包后，为什么会生成HAR包，它是否会导致App包大小膨胀:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-2

## 5.2 从包管理的角度，保证代码安全的措施有哪些:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-4

## 5.3 如何理解App、HAP、HAR、HSP的关系:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-5

## 5.4 HSP/HAR包中如何引用外部编译的so库文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-6

## 5.5 SharedLibrary能否在配置文件中声明abilities、extensionAbilities标签:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-7

## 5.6 HAR包中使用window作为Toast时无法引入页面组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-8

## 5.7 业务模块HAR如何获取宿主HAP的数据:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-9

## 5.8 如何安装打包出来的App包（通过什么命令安装）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-13

## 5.9 如何判断应用可被卸载:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-14

## 5.10 HAR、HSP不能支持Ability、Page声明，限制的理由是什么？后续是否会支持:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-15

## 5.11 是否允许HAR的循环依赖:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-16

## 5.12 HAP依赖HAR A，HAR A依赖HAR B。HAP能否调用HAR B提供的接口？如果不支持间接依赖HAR，设计的原因是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-17

## 5.13 通过resourceManager.getStringResource接口获取HSP资源文件报“Resource id invalid”错误:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-18

## 5.14 HAP/HAR/HSP的关系是什么？是否都可以声明注册Ability和Page？三种类型分别推荐哪些的使用场景？选择原则是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-19

## 5.15 如何正确引用HAR/HSP包模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-21

## 5.16 从HAP的拆包中，如何区分是HAR和HSP:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-23

## 5.17 在HAP中调用createModuleContext方法获取的Context是什么层级:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-25

## 5.18 如何获取当前HAP的BundleName:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-26

## 5.19 如何实现在不使用UIAbility的情况下，能够模块化管理代码，并且各个模块之间可以相互路由跳转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-27

## 5.20 Entry模块的HAP和Feature模块的HAP在使用和功能上的区别是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-28

## 5.21 在HSP export类时，ts文件是按.d.ts导出还是.d.ets导出:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-29

## 5.22 如何避免模块下文件打包进HAR包后，存在的不可预期的资料、配置或信息安全风险:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-31

## 5.23 HAR包多账号如何上传:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-32

## 5.24 HSP包编译之后的.har文件的作用是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-33

## 5.25 如何使HSP包版本号统一:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-34

## 5.26 如何将多工程的HAP打包成一个App:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-35

## 5.27 对于HAP包中引用的HSP包是否有数量限制:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-36

## 5.28 HAR如何转换为HSP:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-37

## 5.29 HAR包是否支持依赖传递:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-38

## 5.30 如何实现跨模块的页面跳转功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-39

## 5.31 如何卸载debug包:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-40

## 5.32 应用安装、卸载时是否有数据上报:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-41

## 5.33 如何解决依赖的版本冲突问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-43

## 5.34 为什么同一App下的HSP文件vendor参数不同时会安装失败:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-44

## 5.35 如何让两个HSP不相互依赖，使用对方的组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-45

## 5.36 应用安装到设备的方式有哪些:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-47

## 5.37 HAR和HSP的使用场景介绍:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-48

## 5.38 一个HSP模块如何快速切换成HAR模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-49

## 5.39 是否推荐使用BM QuickFix制造修复包:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-50

## 5.40 使用hdc命令安装release HAP包到设备时上报“INSTALL_FAILED_APP_SOURCE_NOT_TRUSTED”错误:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-51

## 5.41 如何查询应用包的名称、供应商、版本号、版本文本、安装时间、更新时间等信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-52

## 5.42 如何安装打包出来的App包（通过什么命令安装）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-54

## 5.43 应用免安装的限制、字段解释以及如何自测:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-56

## 5.44 安装HAP包报“failed to install bundle. install debug type not same”错误:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-57

## 5.45 除应用市场外，是否存在其它途径下载安装应用包:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-58

## 5.46 如何判断当前应用程序是Debug包还是Release包:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-61

## 5.47 如何判断应用程序是否安装:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-62

## 5.48 如何跨HSP包调用rawfile目录下的文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-63

## 5.49 如何获取应用包的签名指纹信息，即.p12文件信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-64

## 5.50 使用发布证书进行调试时出现安装错误: Install Failed: error: failed to install bundle.:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-65

## 5.51 使用HSP的多包场景下，直接崩溃并产生cppcrash异常日志，错误信息为resolveBufferCallback get buffer failed:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-66

## 5.52 HAP包中的“--BEGIN CERTIFICATE--”是什么格式的数据:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-67

## 5.53 sign包和unsign包产物之间是否有差异:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-68

## 5.54 如何在应用内共享HSP:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-69

## 5.55 如何通过代码获取Hap包的打包时间:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-70

## 5.56 应用静态快捷方式如何接入X键:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-71

---

# 6 FAQ-程序框架:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability

## 6.1 程序框架（Ability）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-kit

### 6.1.1 如何获取设备屏幕方向的状态变化通知:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-1

### 6.1.2 如何使用AbilityStage的生命周期函数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-2

### 6.1.3 如何在UIAbility调用terminateSelf()后设置不保留最近任务列表中的快照:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-4

### 6.1.4 如何主动退出当前应用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-5

### 6.1.5 部署HAP时上报“Failure[INSTALL_FAILED_SIZE_TOO_LARGE] error while deploying hap”错误:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-13

### 6.1.6 如何获取当前应用程序缓存目录:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-14

### 6.1.7 如何获取应用级别的temp路径和files路径:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-15

### 6.1.8 服务卡片EntryFormAbility生命周期回调函数在哪个ArkTS文件中调用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-16

### 6.1.9 多Module应用通过startAbility()启动时报错:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-20

### 6.1.10 UIAbility在onBackground执行耗时操作时是否会影响另外一个UIAbility的onForeground:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-26

### 6.1.11 应用的进程启动过程是怎样的:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-28

### 6.1.12 是否允许三方应用在手机设备上Fork进程:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-29

### 6.1.13 两个UIAbility之间可通过哪些方法实现数据传递:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-31

### 6.1.14 Extension类进程崩溃是否会导致主进程崩溃:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-32

### 6.1.15 多个UIAbility是运行在一个进程还是多个进程中？三方应用是否支持应用运行在多个进程下？主进程结束了，会影响子进程的运行吗:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-34

### 6.1.16 ExtensionAbility如何与主进程通信:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-35

### 6.1.17 如何在页面中订阅UIAbility实例的生命周期变化:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-36

### 6.1.18 onUnhandledException与onException回调分别什么时候触发:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-37

### 6.1.19 TaskPool里面是否可以使用EventHub:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-38

### 6.1.20 hdc shell命令是否支持schema uri模拟跳转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-39

### 6.1.21 是否可以通过ApplicationContext启动UIAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-40

### 6.1.22 Stage模型与FA模型在进程内对象共享方面有哪些差异:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-50

### 6.1.23 如何实现通过调用其他已安装的应用来打开特定文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-54

### 6.1.24 如何拉起浏览器应用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-58

### 6.1.25 从一个UIAbility跳转到另外一个Ability时，是否支持自定义转场动画的设置？如何实现:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-62

### 6.1.26 UIAbility和UIExtensionAbility有什么区别？分别推荐在什么场景使用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-65

### 6.1.27 UIAbility/Page/Component之间的关系？如何搭配使用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-66

### 6.1.28 关于emitter、eventHub的使用场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-68

### 6.1.29 如何禁用窗口的全屏显示功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-69

### 6.1.30 如何获取App版本号，版本名，屏幕分辨率等信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-71

### 6.1.31 如何获取指定bundleFlags的Ability信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-72

### 6.1.32 如何在UIAbility、页面和组件中获取UIAbilityContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-73

### 6.1.33 如何在工具类中获取Context:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-74

### 6.1.34 ApplicationContext、UIAbilityContext、Context的区别是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-75

### 6.1.35 在使用UIAbilityContext时报401“The context must be a valid Context”的Context类型错误:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-76

### 6.1.36 应用、元服务和卡片是什么关系:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-77

### 6.1.37 系统应用、三方应用、预置应用有什么差别:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-78

### 6.1.38 如何设置默认语言和应用名称为中文:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-80

### 6.1.39 如何查询应用进程的pid信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-81

### 6.1.40 有了代码签名特性后，开发者的so文件在调试、发布等阶段该如何部署:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-82

### 6.1.41 app.json5文件与工程级build-profile.json5文件的区别:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-88

### 6.1.42 应用流转对账号有什么要求:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-89

### 6.1.43 如何在App启动时让各种权限弹窗的申请自动弹出:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-92

### 6.1.44 如果有多个UIAbility，如何判断应用进入后台:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-94

### 6.1.45 开发非UI功能，使用ts开发而非ets开发对应用有哪些影响（内存、CPU、hap大小等方面）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-98

### 6.1.46 如何判断App的启动来源:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-99

### 6.1.47 如何获取当前应用对应的UIAbility名称:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-100

### 6.1.48 如何判断应用当前在前台/后台:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-101

### 6.1.49 如何设置应用自动重启:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-103

### 6.1.50 如何获取设备上安装的应用列表数据:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-104

### 6.1.51 UIAbility在内存不足的情况下是否会被回收，若被回收是否支持页面栈恢复:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-110

### 6.1.52 如何通过resourceManager获取rawFile路径下的文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-111

### 6.1.53 HarmonyOS是否限制App进程fork子进程，是否允许app里自带的可执行文件运行（fork+exec）执行，并通过ptrace方式读取自身进程？这种方式以后是否会限制并禁止:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-112

### 6.1.54 HarmonyOS提供了两种页面加载方式，两者有何区别，怎么选择:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-113

### 6.1.55 如何跳转到系统文件管理App界面:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-116

### 6.1.56 HarmonyOS Next系统属于大端还是小端:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-117

### 6.1.57 UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-118

## 6.2 后台任务开发（Background Tasks）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-kit

### 6.2.1 如何在Stage模型中创建后台任务:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-1

### 6.2.2 应用在后台如何继续执行业务:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-2

### 6.2.3 如何申请多个长时任务:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-4

### 6.2.4 应用运行时进程资源使用规格:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-6

### 6.2.5 如何确认延迟任务WorkSchedulerExtensionAbility回调方法onWorkStart、onWorkStop实现是否正确、是否可以成功回调:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-8

### 6.2.6 如何查询后台任务中短时任务/长时任务/延迟任务/后台代理提醒相关的系统日志:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-background-tasks-9

## 6.3 进程间通信（IPC）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ipc-kit

### 6.3.1 IPC跨进程通信中是否支持异步返回数据:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ipc-1

## 6.4 卡片开发（Form）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-kit

### 6.4.1 点击服务卡片如何跳转至指定的页面:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-1

### 6.4.2 元服务与服务卡片的区别:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-6
