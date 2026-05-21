# 1 ArkUI（方舟UI框架）开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui

## 1.1 ArkUI简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-overview

## 1.2 UI开发 (ArkTS声明式开发范式):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-development

### 1.2.1 UI开发（ArkTS声明式开发范式）概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-development-overview

### 1.2.2 学习UI范式基本语法:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-paradigm-basic-syntax

#### 1.2.2.1 基本语法概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-basic-syntax-overview

#### 1.2.2.2 UI装饰器总览:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-decorator-overview

#### 1.2.2.3 声明式UI描述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-declarative-ui-description

#### 1.2.2.4 自定义组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components

##### 1.2.2.4.1 创建自定义组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components

##### 1.2.2.4.2 自定义组件生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-custom-components-lifecycle

##### 1.2.2.4.3 自定义组件的自定义布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-custom-components-layout

##### 1.2.2.4.4 自定义组件成员属性访问限定符使用限制:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-access-restrictions

##### 1.2.2.4.5 自定义组件复用:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-component-reusable

###### 1.2.2.4.5.1 @Reusable装饰器：V1组件复用:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-reusable

###### 1.2.2.4.5.2 @ReusableV2装饰器：V2组件复用:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-reusablev2

##### 1.2.2.4.6 自定义组件冻结:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-component-freeze

###### 1.2.2.4.6.1 自定义组件冻结功能（V1）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-freeze

###### 1.2.2.4.6.2 自定义组件冻结功能（V2）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-freezev2

#### 1.2.2.5 组件扩展:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend-components

##### 1.2.2.5.1 组件扩展概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend-components-overview

##### 1.2.2.5.2 @Builder装饰器：自定义构建函数:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder

##### 1.2.2.5.3 @LocalBuilder装饰器： 维持组件关系:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localbuilder

##### 1.2.2.5.4 @BuilderParam装饰器：引用@Builder函数:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builderparam

##### 1.2.2.5.5 wrapBuilder：封装全局@Builder:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder

##### 1.2.2.5.6 mutableBuilder：实现全局@Builder动态更新:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mutablebuilder

##### 1.2.2.5.7 @Styles装饰器：定义组件重用样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style

##### 1.2.2.5.8 @Extend装饰器：定义扩展组件样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend

##### 1.2.2.5.9 stateStyles：多态样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles

##### 1.2.2.5.10 @AnimatableExtend装饰器：定义可动画属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animatable-extend

#### 1.2.2.6 @Require装饰器：校验构造传参:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-require

### 1.2.3 学习UI范式状态管理:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management

#### 1.2.3.1 状态管理概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview

#### 1.2.3.2 状态管理术语:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-glossary

#### 1.2.3.3 状态管理原理介绍:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-introduce

#### 1.2.3.4 状态管理V1和V2更新机制差异:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-update-difference

#### 1.2.3.5 MVVM模式（V1）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mvvm

#### 1.2.3.6 MVVM模式（V2）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mvvm-v2

#### 1.2.3.7 状态管理（V1）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v1

##### 1.2.3.7.1 管理组件拥有的状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-component-state-management

###### 1.2.3.7.1.1 @State装饰器：组件内状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state

###### 1.2.3.7.1.2 @Prop装饰器：父子单向同步:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-prop

###### 1.2.3.7.1.3 @Link装饰器：父子双向同步:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-link

###### 1.2.3.7.1.4 @Provide装饰器和@Consume装饰器：与后代组件双向同步:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-provide-and-consume

###### 1.2.3.7.1.5 @Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink

###### 1.2.3.7.1.6 @Watch装饰器：状态变量更改通知:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch

##### 1.2.3.7.2 管理数据对象的状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-data-object-state-management

###### 1.2.3.7.2.1 @Track装饰器：class对象属性级更新:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-track

##### 1.2.3.7.3 管理应用拥有的状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-application-state-management

###### 1.2.3.7.3.1 管理应用拥有的状态概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-application-state-management-overview

###### 1.2.3.7.3.2 LocalStorage：页面级UI状态存储:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage

###### 1.2.3.7.3.3 AppStorage：应用全局的UI状态存储:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage

###### 1.2.3.7.3.4 PersistentStorage：持久化存储UI状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-persiststorage

###### 1.2.3.7.3.5 Environment：设备环境查询:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-environment

#### 1.2.3.8 状态管理（V2）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v2

##### 1.2.3.8.1 管理组件拥有的状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v2-manage-component-state

###### 1.2.3.8.1.1 @Local装饰器：组件内部状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-local

###### 1.2.3.8.1.2 @Param：组件外部输入:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-param

###### 1.2.3.8.1.3 @Once：初始化同步一次:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-once

###### 1.2.3.8.1.4 @Event装饰器：规范组件输出:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-event

###### 1.2.3.8.1.5 @Provider装饰器和@Consumer装饰器：跨组件层级双向同步:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-provider-and-consumer

##### 1.2.3.8.2 管理数据对象的状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v2-manage-data-object-state

###### 1.2.3.8.2.1 @ObservedV2装饰器和@Trace装饰器：类属性变化观测:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace

###### 1.2.3.8.2.2 @Monitor装饰器：状态变量修改监听:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor

###### 1.2.3.8.2.3 @Computed装饰器：计算属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-computed

###### 1.2.3.8.2.4 @Type装饰器：标记类属性的类型:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-type

##### 1.2.3.8.3 管理应用拥有的状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v2-manage-application-state

###### 1.2.3.8.3.1 AppStorageV2: 应用全局UI状态存储:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2

###### 1.2.3.8.3.2 PersistenceV2: 持久化存储UI状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-persistencev2

#### 1.2.3.9 辅助接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-uiutils

##### 1.2.3.9.1 getTarget接口：获取状态管理框架代理前的原始对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-gettarget

##### 1.2.3.9.2 makeObserved接口：将非观察数据变为可观察数据:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-makeobserved

##### 1.2.3.9.3 addMonitor/clearMonitor接口：动态添加/取消监听:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-addmonitor-clearmonitor

##### 1.2.3.9.4 applySync/flushUpdates/flushUIUpdates接口：同步刷新:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates

#### 1.2.3.10 语法糖:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-syntactic-sugar

##### 1.2.3.10.1 $$语法：系统组件双向同步:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync

##### 1.2.3.10.2 !!语法：双向绑定:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding

#### 1.2.3.11 状态管理V1-V2迁移指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-guide

##### 1.2.3.11.1 V1-V2迁移概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration

##### 1.2.3.11.2 状态管理V1向V2迁移场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v1-v2-migration-guide

###### 1.2.3.11.2.1 组件内状态变量迁移:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-component

###### 1.2.3.11.2.2 数据对象状态变量迁移:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-class

###### 1.2.3.11.2.3 应用内状态变量迁移:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-application

###### 1.2.3.11.2.4 组件复用迁移:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-reusable

###### 1.2.3.11.2.5 循环渲染迁移:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-rendering-control-repeat

###### 1.2.3.11.2.6 内置对象的迁移:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-object

###### 1.2.3.11.2.7 AnimateTo使用迁移:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-animateto

##### 1.2.3.11.3 状态管理V1和V2混用场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/v1v2-mixing

###### 1.2.3.11.3.1 状态管理V1和V2混用指导（API version 19前）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage-before-api-version

###### 1.2.3.11.3.2 状态管理V1和V2混用指导（API version 19及之后）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage

#### 1.2.3.12 状态管理常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq

##### 1.2.3.12.1 组件内状态管理常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-inner-component

##### 1.2.3.12.2 数据对象状态管理常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-inner-class

##### 1.2.3.12.3 应用内状态管理和其他常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-application-and-others

##### 1.2.3.12.4 状态变量改变不触发组件刷新问题常用定位方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/troubleshooting-state-manage

### 1.2.4 学习UI范式渲染控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control

#### 1.2.4.1 渲染控制概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-overview

#### 1.2.4.2 if/else：条件渲染:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse

#### 1.2.4.3 ForEach：循环渲染:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach

#### 1.2.4.4 LazyForEach：数据懒加载:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach

#### 1.2.4.5 Repeat：可复用的循环渲染:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat

#### 1.2.4.6 LazyForEach迁移Repeat指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-lazyforeach-repeat-migration-guide

#### 1.2.4.7 ContentSlot：混合开发:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-contentslot

### 1.2.5 学习响应式环境变量:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-property

#### 1.2.5.1 @Env：环境变量:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-system-property

### 1.2.6 设置组件导航和页面路由:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-set-navigation-routing

#### 1.2.6.1 组件导航和页面路由概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-introduction

#### 1.2.6.2 组件导航(Navigation) (推荐):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation

#### 1.2.6.3 页面路由 (@ohos.router)(不推荐):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing

#### 1.2.6.4 Router切换Navigation:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-router-to-navigation

### 1.2.7 组件布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development

#### 1.2.7.1 布局概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-overview

#### 1.2.7.2 构建布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-build-layout

##### 1.2.7.2.1 线性布局 (Row/Column):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear

##### 1.2.7.2.2 层叠布局 (Stack):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-stack-layout

##### 1.2.7.2.3 弹性布局 (Flex):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-flex-layout

##### 1.2.7.2.4 相对布局 (RelativeContainer):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-relative-layout

##### 1.2.7.2.5 栅格布局 (GridRow/GridCol):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-grid-layout

##### 1.2.7.2.6 选项卡 (Tabs):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-tabs

#### 1.2.7.3 开发应用沉浸式效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects

### 1.2.8 列表与网格:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-list-and-grid

#### 1.2.8.1 列表与网格概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-list-grid-development-overview

#### 1.2.8.2 创建列表 (List):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list

#### 1.2.8.3 弧形列表 (ArcList)（圆形屏幕推荐使用）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist

#### 1.2.8.4 创建网格 (Grid/GridItem):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-grid

#### 1.2.8.5 创建瀑布流（WaterFlow）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-waterflow

### 1.2.9 使用文本:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-text

#### 1.2.9.1 文本概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-introduction

#### 1.2.9.2 文本显示 (Text/Span):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-display

#### 1.2.9.3 文本输入 (TextInput/TextArea/Search):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input

#### 1.2.9.4 富文本编辑（RichEditor）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-richeditor

#### 1.2.9.5 图标小符号 (SymbolGlyph/SymbolSpan):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-symbol

#### 1.2.9.6 属性字符串（StyledString/MutableStyledString）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-styled-string

#### 1.2.9.7 图文混排:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-image-layout

#### 1.2.9.8 管理软键盘:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-manage-keyboard

### 1.2.10 媒体展示:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-media-display

#### 1.2.10.1 显示图片 (Image):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-graphics-display

#### 1.2.10.2 视频播放 (Video):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-video-player

#### 1.2.10.3 创建轮播 (Swiper):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-looping

#### 1.2.10.4 创建弧形轮播 (ArcSwiper)（圆形屏幕推荐使用）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-arcswiper

### 1.2.11 表单选择:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-form-selection

#### 1.2.11.1 表单与选择组件概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-forms-overview

#### 1.2.11.2 按钮 (Button):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-button

#### 1.2.11.3 弧形按钮 (ArcButton):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-advanced-components-arcbutton

#### 1.2.11.4 单选框 (Radio):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-radio-button

#### 1.2.11.5 切换按钮 (Toggle):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-switch

### 1.2.12 添加组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-add-component

#### 1.2.12.1 自定义渲染 (XComponent):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-xcomponent-guidelines

#### 1.2.12.2 进度条 (Progress):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-progress-indicator

### 1.2.13 使用弹窗:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-dialog

#### 1.2.13.1 弹窗概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-overview

#### 1.2.13.2 弹出框 (Dialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-dialogs

##### 1.2.13.2.1 弹出框概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-base-dialog-overview

##### 1.2.13.2.2 不依赖UI组件的全局自定义弹出框 (openCustomDialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-custom-dialog

##### 1.2.13.2.3 基础自定义弹出框 (CustomDialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-custom-dialog

##### 1.2.13.2.4 固定样式弹出框:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-fixes-style-dialog

##### 1.2.13.2.5 页面级弹出框:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-embedded-dialog

##### 1.2.13.2.6 弹出框层级管理:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-levelorder

##### 1.2.13.2.7 弹出框控制器:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-controller

##### 1.2.13.2.8 弹出框焦点策略:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-focusable

##### 1.2.13.2.9 弹出框蒙层控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-mask

#### 1.2.13.3 菜单:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-menu

##### 1.2.13.3.1 菜单概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-menu-overview

##### 1.2.13.3.2 菜单控制（Menu）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-menu

##### 1.2.13.3.3 不依赖UI组件的全局菜单 (openMenu):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-uicontext-menu

#### 1.2.13.4 气泡提示:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-popup

##### 1.2.13.4.1 气泡提示概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-overview

##### 1.2.13.4.2 气泡提示（Popup）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-popup

##### 1.2.13.4.3 不依赖UI组件的全局气泡提示 (openPopup):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-uicontext-popup

#### 1.2.13.5 绑定模态页面:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bind-modal

##### 1.2.13.5.1 绑定模态页面概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modal-overview

##### 1.2.13.5.2 绑定半模态页面（bindSheet）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sheet-page

##### 1.2.13.5.3 绑定全模态页面（bindContentCover）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-contentcover-page

#### 1.2.13.6 即时反馈（Toast）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-toast

#### 1.2.13.7 设置浮层（OverlayManager）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-overlaymanager

### 1.2.14 几何图形绘制:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-draw-graphics

#### 1.2.14.1 几何图形绘制概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shape-overview

#### 1.2.14.2 绘制几何图形 (Shape):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-geometric-shape-drawing

#### 1.2.14.3 形状裁剪（clipShape）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-clip-shape

### 1.2.15 添加交互响应:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-overview

#### 1.2.15.1 交互响应概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-capability-overview

#### 1.2.15.2 交互基础机制说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-basic-principles

#### 1.2.15.3 输入设备与事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rkts-interaction-development-guide-raw-input-event

##### 1.2.15.3.1 支持触屏输入事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-touch-screen

##### 1.2.15.3.2 支持鼠标输入事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-mouse

##### 1.2.15.3.3 支持触控板输入事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-touchpad

##### 1.2.15.3.4 支持键盘输入事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-keyboard

##### 1.2.15.3.5 支持表冠输入事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-crown-event

#### 1.2.15.4 添加手势响应:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/rkts-interaction-development-guide-support-gesture

##### 1.2.15.4.1 绑定手势方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-binding

##### 1.2.15.4.2 单一手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-single-gesture

##### 1.2.15.4.3 组合手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-combined-gestures

##### 1.2.15.4.4 多层级手势事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-multi-level-gesture

##### 1.2.15.4.5 手势冲突处理:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-gesture-judge

#### 1.2.15.5 支持统一拖拽:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-drag-event

#### 1.2.15.6 支持焦点处理:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event

### 1.2.16 使用动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-animation

#### 1.2.16.1 动画概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation

#### 1.2.16.2 属性动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-attribute

##### 1.2.16.2.1 属性动画概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-animation-overview

##### 1.2.16.2.2 实现属性动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-animation-apis

##### 1.2.16.2.3 自定义属性动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-attribute-animation

#### 1.2.16.3 转场动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-transition

##### 1.2.16.3.1 转场动画概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-transition-overview

##### 1.2.16.3.2 出现/消失转场:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-enter-exit-transition

##### 1.2.16.3.3 模态转场:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modal-transition

##### 1.2.16.3.4 共享元素转场 (一镜到底):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shared-element-transition

##### 1.2.16.3.5 旋转屏动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rotation-transition-animation

##### 1.2.16.3.6 页面转场动画 (不推荐):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-transition-animation

#### 1.2.16.4 粒子动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-particle-animation

#### 1.2.16.5 组件动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-component-animation

#### 1.2.16.6 动画曲线:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-curve

##### 1.2.16.6.1 动画曲线概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-curve-overview

##### 1.2.16.6.2 传统曲线:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-traditional-curve

##### 1.2.16.6.3 弹簧曲线:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-spring-curve

#### 1.2.16.7 动画衔接:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-smoothing

#### 1.2.16.8 动画效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-effects

##### 1.2.16.8.1 模糊:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-blur-effect

##### 1.2.16.8.2 阴影:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shadow-effect

##### 1.2.16.8.3 色彩:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-color-effect

#### 1.2.16.9 帧动画（ohos.animator）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animator

### 1.2.17 使用自定义能力:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-capabilities

#### 1.2.17.1 自定义能力概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined

#### 1.2.17.2 自定义组合:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-composition

#### 1.2.17.3 自定义节点:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-nodes

##### 1.2.17.3.1 自定义节点概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-node

##### 1.2.17.3.2 自定义占位节点:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-place-holder

##### 1.2.17.3.3 自定义组件节点 (FrameNode):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-framenode

##### 1.2.17.3.4 自定义渲染节点 (RenderNode):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-rendernode

##### 1.2.17.3.5 自定义声明式节点 (BuilderNode):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode

##### 1.2.17.3.6 设置自定义节点跨语言属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-crosslanguage

#### 1.2.17.4 自定义绘制:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-draw

##### 1.2.17.4.1 使用画布绘制自定义图形 (Canvas):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-drawing-customization-on-canvas

##### 1.2.17.4.2 自定义绘制修改器 (DrawModifier):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-extension-drawmodifier

#### 1.2.17.5 Modifier机制:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-modifier

##### 1.2.17.5.1 自定义扩展能力概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-modifier

##### 1.2.17.5.2 内容修改器 (ContentModifier):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-attributes-content-modifier

##### 1.2.17.5.3 属性修改器 (AttributeModifier):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-extension-attributemodifier

##### 1.2.17.5.4 属性更新器 (AttributeUpdater):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-extension-attributeupdater

### 1.2.18 UI国际化:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-internationalization

### 1.2.19 无障碍与适老化:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-support-accessibility-friendliness

#### 1.2.19.1 无障碍开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-universal-attributes-accessibility

#### 1.2.19.2 支持适老化:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-support-for-aging-adaptation

### 1.2.20 主题设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-theme

#### 1.2.20.1 应用深浅色适配:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-dark-light-color-adaptation

#### 1.2.20.2 设置应用内主题换肤:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning

### 1.2.21 UI系统场景化能力:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-system-scenarization-capability

#### 1.2.21.1 使用UI上下文接口操作界面（UIContext）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface

#### 1.2.21.2 使用组件截图（ComponentSnapshot）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-uicontext-component-snapshot

#### 1.2.21.3 感知组件可见性:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-manage-components-visibility

#### 1.2.21.4 检查页面布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-inspector-overview

#### 1.2.21.5 媒体查询 (@ohos.mediaquery):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-media-query

#### 1.2.21.6 嵌入式组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-cross-process

##### 1.2.21.6.1 全屏启动元服务组件（FullScreenLaunchComponent）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-fullscreencomponent

##### 1.2.21.6.2 同应用进程嵌入式组件 (EmbeddedComponent):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-embedded-components

## 1.3 UI开发 (基于NDK构建UI):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-ndk

### 1.3.1 基于NDK构建UI概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-ui-overview

### 1.3.2 接入ArkTS页面:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-access-the-arkts-page

### 1.3.3 添加交互事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-add-event

#### 1.3.3.1 监听组件事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-listen-to-component-events

#### 1.3.3.2 绑定手势事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-bind-gesture-events

#### 1.3.3.3 拖拽事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-drag-event

#### 1.3.3.4 监听组件布局和绘制送显事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-inspector-component-observer

### 1.3.4 使用动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-use-animation

### 1.3.5 构建布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-build-layout-ndk

#### 1.3.5.1 使用列表:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-loading-long-list

#### 1.3.5.2 使用瀑布流:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-waterflow

### 1.3.6 使用文本:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-build-text-ndk

#### 1.3.6.1 Text组件的文本绘制与显示:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-styled-string

#### 1.3.6.2 监听输入框事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-textarea-event

### 1.3.7 构建弹窗:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-pop-up-window

### 1.3.8 构建自定义组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-custom-components

### 1.3.9 嵌入ArkTS组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embed-arkts-components

### 1.3.10 构建渲染节点:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embed-render-components

### 1.3.11 通过XComponent接入无障碍:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-accessibility-xcomponent

### 1.3.12 自定义绘制:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-draw

### 1.3.13 查询和操作自定义节点:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-node-query-operate

### 1.3.14 通过EmbeddedComponent拉起EmbeddedUIExtensionAbility:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-embedded-component

### 1.3.15 在NDK中保证多实例场景功能正常:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-scope-task

### 1.3.16 使用多线程NDK接口并行化构建UI页面:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ndk-build-on-multi-thread

## 1.4 UI开发 (兼容JS的类Web开发范式):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-dev

### 1.4.1 UI开发 (兼容JS的类Web开发范式)概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-overview

### 1.4.2 框架说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-overview

#### 1.4.2.1 文件组织:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-file

#### 1.4.2.2 js标签配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-js-tag

#### 1.4.2.3 app.js:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-js-file

#### 1.4.2.4 语法:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-syntax

##### 1.4.2.4.1 HML语法参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-syntax-hml

##### 1.4.2.4.2 CSS语法参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-syntax-css

##### 1.4.2.4.3 JS语法参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-syntax-js

#### 1.4.2.5 生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-lifecycle

#### 1.4.2.6 资源限定与访问:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-resource-restriction

#### 1.4.2.7 多语言支持:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-framework-multiple-languages

### 1.4.3 构建用户界面:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui

#### 1.4.3.1 组件介绍:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-component

#### 1.4.3.2 构建布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-layout

##### 1.4.3.2.1 布局说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-intro

##### 1.4.3.2.2 添加标题行和文本区域:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-text

##### 1.4.3.2.3 添加图片区域:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-image

##### 1.4.3.2.4 添加留言区域:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-comment

##### 1.4.3.2.5 添加容器:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-layout-external-container

#### 1.4.3.3 添加交互:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-interactions

#### 1.4.3.4 动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-animation

#### 1.4.3.5 手势事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-event

#### 1.4.3.6 页面路由:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-routes

### 1.4.4 常见组件开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components

#### 1.4.4.1 容器组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-container-components

##### 1.4.4.1.1 list开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-list

##### 1.4.4.1.2 dialog开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-dialog

##### 1.4.4.1.3 form开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-form

##### 1.4.4.1.4 stepper开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-stepper

##### 1.4.4.1.5 tabs开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-component-tabs

##### 1.4.4.1.6 swiper开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-swiper

#### 1.4.4.2 基础组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-basic-components

##### 1.4.4.2.1 text开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-text

##### 1.4.4.2.2 input开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-input

##### 1.4.4.2.3 button开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-button

##### 1.4.4.2.4 picker开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-picker

##### 1.4.4.2.5 image开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-images

##### 1.4.4.2.6 image-animator开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-image-animator

##### 1.4.4.2.7 rating开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-rating

##### 1.4.4.2.8 slider开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-slider

##### 1.4.4.2.9 chart开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-chart

##### 1.4.4.2.10 switch开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-switch

##### 1.4.4.2.11 toolbar开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-toolbar

##### 1.4.4.2.12 menu开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-menu

##### 1.4.4.2.13 marquee开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-marquee

##### 1.4.4.2.14 qrcode开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-qrcode

##### 1.4.4.2.15 search开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-search

#### 1.4.4.3 Canvas开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-canvas

##### 1.4.4.3.1 Canvas对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvas

##### 1.4.4.3.2 CanvasRenderingContext2D对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-canvasrenderingcontext2d

##### 1.4.4.3.3 Path2D对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-path2d

##### 1.4.4.3.4 OffscreenCanvasRenderingContext2D对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-offscreencanvas

#### 1.4.4.4 栅格布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-grid

#### 1.4.4.5 svg开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-svg

##### 1.4.4.5.1 基础知识:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-overview

##### 1.4.4.5.2 绘制图形:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-graphics

##### 1.4.4.5.3 绘制路径:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-path

##### 1.4.4.5.4 绘制文本:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-components-svg-text

### 1.4.5 动效开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animation

#### 1.4.5.1 CSS动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animation-css

##### 1.4.5.1.1 属性样式动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-attribute-style

##### 1.4.5.1.2 transform样式动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-transform

##### 1.4.5.1.3 background-position样式动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-background-position-style

##### 1.4.5.1.4 svg动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-svg

#### 1.4.5.2 JS动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animation-js

##### 1.4.5.2.1 组件动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-component

##### 1.4.5.2.2 插值器动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-interpolator-animation

###### 1.4.5.2.2.1 动画动效:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-dynamic-effects

###### 1.4.5.2.2.2 动画帧:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-animate-frame

### 1.4.6 自定义组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-custom-components

### 1.4.7 WebGL:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-webgl

#### 1.4.7.1 使用WebGL绘制图形:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/webgl-2d-guidelines

## 1.5 UI开发调试调优:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-debug-optimize

### 1.5.1 UI稳定性故障调试:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-stability

#### 1.5.1.1 UI稳定性故障分析概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-stability-guide

#### 1.5.1.2 UI相关应用崩溃常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-stability-crash-issues

#### 1.5.1.3 UI相关应用无响应常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-stability-freeze-issues

### 1.5.2 UI显示异常调试:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-debug

### 1.5.3 UI上下文异常调试:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrong-uicontext-debug

### 1.5.4 UI预览:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-ide-previewer

### 1.5.5 UI调优:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-inspector-profiler

### 1.5.6 UI高性能开发:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-performance-overview

### 1.5.7 UI开发常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-development-faq

#### 1.5.7.1 自定义节点常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-node-faq

#### 1.5.7.2 按钮与选择组件常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-select-component-faq

#### 1.5.7.3 使用文本常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-text-faq

#### 1.5.7.4 动态属性设置常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-attribute-modifier-faq

#### 1.5.7.5 命令式节点常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-arkui-framenode-faq

#### 1.5.7.6 UI并行化常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-ui-build-faq

## 1.6 窗口管理:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-manager

### 1.6.1 窗口开发概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-overview

### 1.6.2 管理应用窗口（Stage模型）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-stage

### 1.6.3 管理应用窗口（FA模型）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-fa

### 1.6.4 窗口旋转:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-rotation

### 1.6.5 窗口元数据配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-config-m

### 1.6.6 使用WindowManager管理多模输入事件（C/C++）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-window-event-filter

### 1.6.7 在应用程序中使用画中画功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-pipwindow

#### 1.6.7.1 画中画开发概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-overview

#### 1.6.7.2 使用XComponent实现画中画功能开发（ArkTS）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-xcomponent

#### 1.6.7.3 使用typeNode实现画中画功能开发（ArkTS）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-typenode

#### 1.6.7.4 使用NDK接口实现画中画功能开发（C/C++）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-native

#### 1.6.7.5 画中画常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pip-faqs

### 1.6.8 全局闪控球开发指导:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/floatingball-guide

### 1.6.9 智慧多窗应用开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-guide

#### 1.6.9.1 智慧多窗简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-intro

#### 1.6.9.2 应用适配智慧多窗:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-adapt

##### 1.6.9.2.1 应用声明支持智慧多窗:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-support

##### 1.6.9.2.2 应用布局适配智慧多窗:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-layout-adapt

##### 1.6.9.2.3 顶部窗口控制条避让适配智慧多窗:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-controlbar-adapt

### 1.6.10 应用启动页的配置与使用:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/launch-page

#### 1.6.10.1 应用启动页简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/launch-page-overview

#### 1.6.10.2 配置应用启动页:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/launch-page-config

#### 1.6.10.3 启动页资源分类配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/launch-page-resource-config

### 1.6.11 窗口开发术语:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology

### 1.6.12 窗口开发常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-faqs

## 1.7 屏幕管理:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/display-manager

### 1.7.1 屏幕管理简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaymanager-overview

### 1.7.2 使用OH_DisplayManager实现屏幕基础信息查询和状态监听 (C/C++):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-display-manager

### 1.7.3 使用Display实现屏幕属性查询及状态监听 (ArkTS):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/screenproperty-guideline

### 1.7.4 屏幕管理开发术语:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/display-terminology

### 1.7.5 屏幕开发常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaymanager-faqs

## 1.8 ArkUI术语:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-glossary

---

# 2 ArkUI（方舟UI框架）API参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-api

## 2.1 ArkTS API:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-arkts

### 2.1.1 UI界面:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui

#### 2.1.1.1 @ohos.animator (动画):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-animator

#### 2.1.1.2 @ohos.arkui.componentSnapshot (组件截图):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentsnapshot

#### 2.1.1.3 @ohos.arkui.componentUtils (componentUtils):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentutils

#### 2.1.1.4 @ohos.arkui.dragController (DragController):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-dragcontroller

#### 2.1.1.5 @ohos.arkui.drawableDescriptor (DrawableDescriptor):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-drawabledescriptor

#### 2.1.1.6 @ohos.arkui.inspector (布局回调):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-inspector

#### 2.1.1.7 @ohos.arkui.node:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-node

#### 2.1.1.8 @ohos.arkui.observer (无感监听):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer

#### 2.1.1.9 @ohos.arkui.Prefetcher (Prefetching):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-prefetcher

#### 2.1.1.10 @ohos.arkui.shape (形状):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape

#### 2.1.1.11 @ohos.arkui.theme(主题换肤):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme

#### 2.1.1.12 @ohos.arkui.UIContext (UIContext):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uicontext

##### 2.1.1.12.1 模块描述:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext

##### 2.1.1.12.2 Class (ComponentSnapshot):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-componentsnapshot

##### 2.1.1.12.3 Class (ComponentUtils):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-componentutils

##### 2.1.1.12.4 Class (ContextMenuController):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-contextmenucontroller

##### 2.1.1.12.5 Class (CursorController):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-cursorcontroller

##### 2.1.1.12.6 Class (DragController):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dragcontroller

##### 2.1.1.12.7 Class (DynamicSyncScene):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dynamicsyncscene

##### 2.1.1.12.8 Class (FocusController):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-focuscontroller

##### 2.1.1.12.9 Class (Font):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-font

##### 2.1.1.12.10 Class (FrameCallback):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-framecallback

##### 2.1.1.12.11 Class (Magnifier):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-magnifier

##### 2.1.1.12.12 Class (MarqueeDynamicSyncScene):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-marqueedynamicsyncscene

##### 2.1.1.12.13 Class (MeasureUtils):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-measureutils

##### 2.1.1.12.14 Class (MediaQuery):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery

##### 2.1.1.12.15 Class (OverlayManager):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-overlaymanager

##### 2.1.1.12.16 Class (PromptAction):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-promptaction

##### 2.1.1.12.17 Class (Router):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router

##### 2.1.1.12.18 Class (SwiperDynamicSyncScene):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-swiperdynamicsyncscene

##### 2.1.1.12.19 Class (TextMenuController):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-textmenucontroller

##### 2.1.1.12.20 Class (UIContext):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext

##### 2.1.1.12.21 Class (ResolvedUIContext):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-resolveduicontext

##### 2.1.1.12.22 Class (UIInspector):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiinspector

##### 2.1.1.12.23 Class (UIObserver):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiobserver

##### 2.1.1.12.24 Interface (AtomicServiceBar):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-atomicservicebar

##### 2.1.1.12.25 Interfaces (其他):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-i

##### 2.1.1.12.26 Enums:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e

##### 2.1.1.12.27 Types:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-t

#### 2.1.1.13 @ohos.arkui.uiExtension (uiExtension):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uiextension

#### 2.1.1.14 @ohos.arkui.StateManagement (状态管理):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement

#### 2.1.1.15 @ohos.curves (插值计算):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-curve

#### 2.1.1.16 @ohos.font (注册自定义字体):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-font

#### 2.1.1.17 @ohos.matrix4 (矩阵变换):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-matrix4

#### 2.1.1.18 @ohos.measure (文本计算):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-measure

#### 2.1.1.19 @ohos.mediaquery (媒体查询):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery

#### 2.1.1.20 @ohos.pluginComponent (PluginComponentManager):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-plugincomponent

#### 2.1.1.21 @ohos.promptAction (弹窗):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction

#### 2.1.1.22 @ohos.router (页面路由)(不推荐):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-router

#### 2.1.1.23 @ohos.uiAppearance (用户界面外观):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uiappearance

#### 2.1.1.24 getContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-getcontext

#### 2.1.1.25 postCardAction:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-postcardaction

#### 2.1.1.26 arkui:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-interface-arkui

##### 2.1.1.26.1 BuilderNode:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-buildernode

##### 2.1.1.26.2 ComponentContent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentcontent

##### 2.1.1.26.3 FrameNode:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode

##### 2.1.1.26.4 Graphics:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics

##### 2.1.1.26.5 NodeController:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontroller

##### 2.1.1.26.6 RenderNode:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-rendernode

##### 2.1.1.26.7 AttributeUpdater:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-attributeupdater

##### 2.1.1.26.8 Content:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-content

##### 2.1.1.26.9 NodeContent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontent

##### 2.1.1.26.10 Resource:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-resource

### 2.1.2 窗口管理:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/window-manager-api

#### 2.1.2.1 @ohos.PiPWindow (画中画窗口):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pipwindow

#### 2.1.2.2 @ohos.window.floatingBall (闪控球窗口):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-floatingball

#### 2.1.2.3 @ohos.window (窗口):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-window

##### 2.1.2.3.1 模块描述:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window

##### 2.1.2.3.2 Functions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-f

##### 2.1.2.3.3 Interface (Window):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window

##### 2.1.2.3.4 Interface (WindowStage):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-windowstage

##### 2.1.2.3.5 Interfaces (其他):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-i

##### 2.1.2.3.6 Enums:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-e

##### 2.1.2.3.7 Types:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-t

### 2.1.3 屏幕管理:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/display-manager-api

#### 2.1.3.1 @ohos.display (屏幕属性):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display

#### 2.1.3.2 @ohos.screenshot (屏幕截图):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-screenshot

### 2.1.4 已停止维护的接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-arkts-dep

#### 2.1.4.1 @ohos.prompt (弹窗):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-prompt

#### 2.1.4.2 @system.app (应用上下文):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-app

#### 2.1.4.3 @system.configuration (应用配置):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-configuration

#### 2.1.4.4 @system.mediaquery (媒体查询):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-mediaquery

#### 2.1.4.5 @system.prompt (弹窗):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-prompt

#### 2.1.4.6 @system.router (页面路由):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-router

#### 2.1.4.7 XComponentNode:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-xcomponentnode

## 2.2 ArkTS组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-declarative-comp

### 2.2.1 通用事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events

#### 2.2.1.1 基础输入事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/basic-raw-input-event

##### 2.2.1.1.1 触摸事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch

##### 2.2.1.1.2 鼠标事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mouse-key

##### 2.2.1.1.3 轴事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-axis

##### 2.2.1.1.4 按键事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-key

##### 2.2.1.1.5 表冠事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-crown

##### 2.2.1.1.6 焦点轴事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-focus_axis

#### 2.2.1.2 交互响应事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/interaction-events

##### 2.2.1.2.1 点击事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-click

##### 2.2.1.2.2 拖拽事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-drag-drop

##### 2.2.1.2.3 焦点事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-focus-event

##### 2.2.1.2.4 悬浮事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-hover

##### 2.2.1.2.5 组件快捷键事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-keyboardshortcut

#### 2.2.1.3 交互事件分发控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/event-dispatch-control

##### 2.2.1.3.1 自定义事件拦截:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-touch-intercept

##### 2.2.1.3.2 自定义事件分发:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-on-child-touch-test

#### 2.2.1.4 无障碍相关:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/accessibility-related

##### 2.2.1.4.1 无障碍控制操作:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-accessibility-event

##### 2.2.1.4.2 无障碍悬浮事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-accessibility-hover-event

#### 2.2.1.5 组件变化事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/component-change

##### 2.2.1.5.1 挂载卸载事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-show-hide

##### 2.2.1.5.2 组件区域变化事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-area-change-event

##### 2.2.1.5.3 组件尺寸变化事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-size-change-event

##### 2.2.1.5.4 组件可见区域变化事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-visible-area-change-event

### 2.2.2 通用属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes

#### 2.2.2.1 基础属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/basic-property

##### 2.2.2.1.1 组件标识:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id

##### 2.2.2.1.2 分布式迁移标识:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-restoreid

##### 2.2.2.1.3 显隐控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility

##### 2.2.2.1.4 背景设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background

##### 2.2.2.1.5 浮层:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-overlay

##### 2.2.2.1.6 Z序控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-z-order

##### 2.2.2.1.7 隐私遮罩:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-obscured

##### 2.2.2.1.8 禁用反色能力:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-allow-force-dark

#### 2.2.2.2 布局与边框:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/layout-property

##### 2.2.2.2.1 尺寸设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size

##### 2.2.2.2.2 位置设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-location

##### 2.2.2.2.3 布局约束:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-layout-constraints

##### 2.2.2.2.4 Flex布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout

##### 2.2.2.2.5 安全区域:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area

##### 2.2.2.2.6 组件级像素取整:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-pixelroundforcomponent

##### 2.2.2.2.7 页面级像素取整:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-pixelroundforpage

##### 2.2.2.2.8 边框设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border

##### 2.2.2.2.9 图片边框设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border-image

#### 2.2.2.3 视效与模糊:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/visual-effect-property

##### 2.2.2.3.1 透明度设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-opacity

##### 2.2.2.3.2 图形变换:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation

##### 2.2.2.3.3 图像效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect

##### 2.2.2.3.4 形状裁剪:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping

##### 2.2.2.3.5 颜色渐变:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gradient-color

##### 2.2.2.3.6 前景色设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-color

##### 2.2.2.3.7 前景属性设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-effect

##### 2.2.2.3.8 外描边设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-outline

##### 2.2.2.3.9 视效设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-filter-effect

##### 2.2.2.3.10 组件内容模糊:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-blur-style

##### 2.2.2.3.11 运动模糊:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-motionblur

##### 2.2.2.3.12 点击回弹效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click-effect

##### 2.2.2.3.13 特效绘制合并:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-use-effect

##### 2.2.2.3.14 组件内容填充方式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-renderfit

#### 2.2.2.4 交互属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/interaction-property

##### 2.2.2.4.1 禁用控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-enable

##### 2.2.2.4.2 焦点控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-focus

##### 2.2.2.4.3 拖拽控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-drop

##### 2.2.2.4.4 拖拽排序:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-drag-sorting

##### 2.2.2.4.5 悬浮态效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hover-effect

##### 2.2.2.4.6 触摸交互控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/touch-interactions

###### 2.2.2.4.6.1 触摸热区设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-touch-target

###### 2.2.2.4.6.2 触摸测试控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior

###### 2.2.2.4.6.3 事件独占控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-monopolize-events

##### 2.2.2.4.7 鼠标光标控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-cursor

#### 2.2.2.5 多态样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style

#### 2.2.2.6 弹窗控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/popup-property

##### 2.2.2.6.1 Popup控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-popup

##### 2.2.2.6.2 Tips控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-tips

##### 2.2.2.6.3 菜单控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-menu

#### 2.2.2.7 无障碍属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility

#### 2.2.2.8 模态转场设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/transition

##### 2.2.2.8.1 全屏模态转场:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-modal-transition

##### 2.2.2.8.2 半模态转场:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition

#### 2.2.2.9 动态属性与自定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/attribute-modifier-property

##### 2.2.2.9.1 动态属性设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier

##### 2.2.2.9.2 动态手势设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-gesture-modifier

##### 2.2.2.9.3 自定义绘制设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-draw-modifier

##### 2.2.2.9.4 自定义内容:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-content-modifier

##### 2.2.2.9.5 自定义属性设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-custom-property

##### 2.2.2.9.6 动态SymbolGlyphModifier属性设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/universal-attributes-attribute-symbolglyphmodifier

#### 2.2.2.10 其他:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/other-property

##### 2.2.2.10.1 复用标识:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-reuse-id

##### 2.2.2.10.2 复用选项:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-reuse

##### 2.2.2.10.3 工具栏设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-toolbar

### 2.2.3 手势处理:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gesture-handling

#### 2.2.3.1 绑定手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gesture-binding

##### 2.2.3.1.1 绑定手势方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-settings

##### 2.2.3.1.2 设置组件绑定的手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-uigestureevent

##### 2.2.3.1.3 手势处理器:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesturehandler

#### 2.2.3.2 基础手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/basic-gestures

##### 2.2.3.2.1 TapGesture:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-tapgesture

##### 2.2.3.2.2 LongPressGesture:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-longpressgesture

##### 2.2.3.2.3 PanGesture:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture

##### 2.2.3.2.4 PinchGesture:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pinchgesture

##### 2.2.3.2.5 RotationGesture:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-rotationgesture

##### 2.2.3.2.6 SwipeGesture:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-swipegesture

#### 2.2.3.3 组合手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-combined-gestures

#### 2.2.3.4 手势控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/gesture-control

##### 2.2.3.4.1 自定义手势判定:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-customize-judge

##### 2.2.3.4.2 手势拦截增强:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-blocking-enhancement

#### 2.2.3.5 手势公共接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-common

### 2.2.4 行列与堆叠:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rows-columns-and-stacking

#### 2.2.4.1 Flex:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex

#### 2.2.4.2 Column:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column

#### 2.2.4.3 Row:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row

#### 2.2.4.4 Stack:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack

#### 2.2.4.5 RelativeContainer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-relativecontainer

### 2.2.5 栅格与分栏:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/grid-and-column-layout

#### 2.2.5.1 GridRow:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridrow

#### 2.2.5.2 GridCol:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcol

#### 2.2.5.3 ColumnSplit:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-columnsplit

#### 2.2.5.4 RowSplit:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-rowsplit

#### 2.2.5.5 SideBarContainer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-sidebarcontainer

### 2.2.6 滚动与滑动:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/scroll-and-swipe

#### 2.2.6.1 List:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list

#### 2.2.6.2 ListItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitem

#### 2.2.6.3 ListItemGroup:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-listitemgroup

#### 2.2.6.4 ArcList:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist

#### 2.2.6.5 ArcListItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclistitem

#### 2.2.6.6 Grid:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid

#### 2.2.6.7 GridItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-griditem

#### 2.2.6.8 Scroll:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scroll

#### 2.2.6.9 Swiper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper

#### 2.2.6.10 ArcSwiper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arcswiper

#### 2.2.6.11 WaterFlow:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow

#### 2.2.6.12 FlowItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flowitem

#### 2.2.6.13 LazyVGridLayout:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-lazyvgridlayout

#### 2.2.6.14 ScrollBar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-scrollbar

#### 2.2.6.15 Refresh:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh

#### 2.2.6.16 ArcScrollBar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-arcscrollbar

#### 2.2.6.17 滚动组件通用接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-scrollable-common

### 2.2.7 导航与切换:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/navigation-and-switching

#### 2.2.7.1 Indicator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-swiper-components-indicator

#### 2.2.7.2 Navigation:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation

#### 2.2.7.3 NavDestination:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination

#### 2.2.7.4 MultiNavigation:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-multinavigation

#### 2.2.7.5 Tabs:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs

#### 2.2.7.6 TabContent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent

#### 2.2.7.7 ToolBarItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toolbaritem

### 2.2.8 按钮与选择:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/buttons-and-selections

#### 2.2.8.1 Button:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button

#### 2.2.8.2 Toggle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-toggle

#### 2.2.8.3 Checkbox:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkbox

#### 2.2.8.4 CheckboxGroup:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-checkboxgroup

#### 2.2.8.5 UIPickerComponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-ui-picker-component

#### 2.2.8.6 CalendarPicker:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-calendarpicker

#### 2.2.8.7 DatePicker:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datepicker

#### 2.2.8.8 TextPicker:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textpicker

#### 2.2.8.9 TimePicker:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-timepicker

#### 2.2.8.10 Radio:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-radio

#### 2.2.8.11 Rating:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-rating

#### 2.2.8.12 Select:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-select

#### 2.2.8.13 Slider:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider

#### 2.2.8.14 ArcButton:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcbutton

#### 2.2.8.15 ArcSlider:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-arcslider

#### 2.2.8.16 选择器（Picker）公共接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-picker-common

### 2.2.9 文本与输入:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/text-and-input

#### 2.2.9.1 Text:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text

#### 2.2.9.2 TextArea:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textarea

#### 2.2.9.3 TextInput:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput

#### 2.2.9.4 RichEditor:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor

#### 2.2.9.5 Search:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-search

#### 2.2.9.6 Span:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span

#### 2.2.9.7 ImageSpan:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imagespan

#### 2.2.9.8 ContainerSpan:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-containerspan

#### 2.2.9.9 SymbolSpan:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan

#### 2.2.9.10 SymbolGlyph:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolglyph

#### 2.2.9.11 Hyperlink:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-hyperlink

#### 2.2.9.12 RichText:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richtext

#### 2.2.9.13 属性字符串:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-styled-string

#### 2.2.9.14 输入框类组件通用接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-text-style

#### 2.2.9.15 文本组件公共接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-text-common

### 2.2.10 图片与视频:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/images-and-videos

#### 2.2.10.1 Image:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image

#### 2.2.10.2 ImageAnimator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-imageanimator

#### 2.2.10.3 Video:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video

#### 2.2.10.4 图像类型定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-common

#### 2.2.10.5 SVG标签说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-svg

#### 2.2.10.6 SVG标签解析能力增强:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-image-svg2-capabilities

### 2.2.11 信息展示:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/information-display

#### 2.2.11.1 AlphabetIndexer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-alphabet-indexer

#### 2.2.11.2 ArcAlphabetIndexer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer

#### 2.2.11.3 Badge:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge

#### 2.2.11.4 Counter:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-counter

#### 2.2.11.5 DataPanel:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel

#### 2.2.11.6 Gauge:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-gauge

#### 2.2.11.7 LoadingProgress:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress

#### 2.2.11.8 Marquee:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-marquee

#### 2.2.11.9 PatternLock:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-patternlock

#### 2.2.11.10 Progress:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress

#### 2.2.11.11 QRCode:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-qrcode

#### 2.2.11.12 TextClock:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textclock

#### 2.2.11.13 TextTimer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-texttimer

#### 2.2.11.14 信息展示公共接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-information-display-common

### 2.2.12 空白与分隔:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/blank-and-divider

#### 2.2.12.1 Blank:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-blank

#### 2.2.12.2 Divider:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-divider

### 2.2.13 画布绘制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/canvas-drawing

#### 2.2.13.1 Canvas:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas

#### 2.2.13.2 CanvasGradient:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvasgradient

#### 2.2.13.3 CanvasPattern:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvaspattern

#### 2.2.13.4 CanvasRenderingContext2D:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d

#### 2.2.13.5 DrawingRenderingContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawingrenderingcontext

#### 2.2.13.6 ImageBitmap:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagebitmap

#### 2.2.13.7 ImageData:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagedata

#### 2.2.13.8 Matrix2D:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-matrix2d

#### 2.2.13.9 OffscreenCanvas:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-offscreencanvas

#### 2.2.13.10 OffscreenCanvasRenderingContext2D:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d

#### 2.2.13.11 Path2D:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-path2d

### 2.2.14 图形绘制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphic-drawing

#### 2.2.14.1 Circle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-circle

#### 2.2.14.2 Ellipse:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-ellipse

#### 2.2.14.3 Line:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-line

#### 2.2.14.4 Polyline:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polyline

#### 2.2.14.5 Polygon:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polygon

#### 2.2.14.6 Path:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-path

#### 2.2.14.7 Rect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-rect

#### 2.2.14.8 Shape:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-shape

### 2.2.15 渲染绘制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rendering-drawing

#### 2.2.15.1 XComponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent

#### 2.2.15.2 Component3D:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-component3d

#### 2.2.15.3 EmbeddedComponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-embedded-component

### 2.2.16 菜单:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/menus

#### 2.2.16.1 Menu:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menu

#### 2.2.16.2 MenuItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menuitem

#### 2.2.16.3 MenuItemGroup:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-menuitemgroup

#### 2.2.16.4 ContextMenu:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-menu

### 2.2.17 动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/animation

#### 2.2.17.1 属性动画 (animation):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatorproperty

#### 2.2.17.2 显式动画 (animateTo):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation

#### 2.2.17.3 关键帧动画 (keyframeAnimateTo):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-keyframeanimateto

#### 2.2.17.4 页面间转场 (pageTransition):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-page-transition-animation

#### 2.2.17.5 组件内转场 (transition):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-component

#### 2.2.17.6 共享元素转场 (sharedTransition):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-shared-elements

#### 2.2.17.7 组件内隐式共享元素转场 (geometryTransition):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-transition-animation-geometrytransition

#### 2.2.17.8 路径动画 (motionPath):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-motion-path-animation

#### 2.2.17.9 粒子动画 (Particle):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-particle-animation

#### 2.2.17.10 显式动画立即下发 (animateToImmediately):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animatetoimmediately

### 2.2.18 弹窗:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dialog-boxes

#### 2.2.18.1 警告弹窗 (AlertDialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-alert-dialog-box

#### 2.2.18.2 列表选择弹窗 (ActionSheet):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-action-sheet

#### 2.2.18.3 自定义弹窗 (CustomDialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-custom-dialog-box

#### 2.2.18.4 日历选择器弹窗 (CalendarPickerDialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-calendarpicker-dialog

#### 2.2.18.5 日期滑动选择器弹窗 (DatePickerDialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-datepicker-dialog

#### 2.2.18.6 时间滑动选择器弹窗 (TimePickerDialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-timepicker-dialog

#### 2.2.18.7 文本滑动选择器弹窗 (TextPickerDialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-methods-textpicker-dialog

#### 2.2.18.8 弹出框 (Dialog):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialog

### 2.2.19 卡片:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/service-widgets

#### 2.2.19.1 FormLink:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-formlink

### 2.2.20 安全:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-security

#### 2.2.20.1 安全控件通用属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-securitycomponent-attributes

#### 2.2.20.2 PasteButton:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-security-components-pastebutton

#### 2.2.20.3 SaveButton:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-security-components-savebutton

### 2.2.21 主题:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/themes

#### 2.2.21.1 WithTheme:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-with-theme

### 2.2.22 AtomicService:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/atomic-services

#### 2.2.22.1 AtomicServiceNavigation:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicenavigation

#### 2.2.22.2 AtomicServiceSearch:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicesearch

#### 2.2.22.3 AtomicServiceTabs:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicservicetabs

#### 2.2.22.4 AtomicServiceWeb:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-atomicserviceweb

#### 2.2.22.5 InterstitialDialogAction:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-interstitialdialogaction

#### 2.2.22.6 HalfScreenLaunchComponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-halfscreenlaunchcomponent

#### 2.2.22.7 NavPushPathHelper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-atomicservice-navpushpathhelper

### 2.2.23 自定义占位组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/custom-placeholder-comp

#### 2.2.23.1 NodeContainer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-nodecontainer

#### 2.2.23.2 ContentSlot:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-contentslot

### 2.2.24 自定义组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/custom-comp

#### 2.2.24.1 自定义组件的生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-lifecycle

#### 2.2.24.2 自定义组件的自定义布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-layout

#### 2.2.24.3 自定义组件内置方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-api

#### 2.2.24.4 自定义组件参数:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-parameter

#### 2.2.24.5 组件扩展装饰器:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-extend-component-decorator

##### 2.2.24.5.1 定义可动画属性 (@AnimatableExtend):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatable-extend

##### 2.2.24.5.2 @Entry：页面入口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-entry

##### 2.2.24.5.3 wrapBuilder:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-wrapbuilder

##### 2.2.24.5.4 mutableBuilder:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-mutablebuilder

### 2.2.25 组件预览:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/component-preview

#### 2.2.25.1 组件预览:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-previewer

### 2.2.26 系统预置UI组件库:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/system-preset-ui-component-library

#### 2.2.26.1 Chip:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chip

#### 2.2.26.2 ChipGroup:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-chipgroup

#### 2.2.26.3 ComposeListItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-composelistitem

#### 2.2.26.4 ComposeTitleBar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-composetitlebar

#### 2.2.26.5 DownloadFileButton:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-downloadfilebutton

#### 2.2.26.6 DialogV2:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-dialogv2

#### 2.2.26.7 EditableTitleBar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-editabletitlebar

#### 2.2.26.8 ExceptionPrompt:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-exceptionprompt

#### 2.2.26.9 Filter:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-filter

#### 2.2.26.10 FolderStack:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-folderstack

#### 2.2.26.11 FoldSplitContainer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-foldsplitcontainer

#### 2.2.26.12 FormMenu:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-formmenu

#### 2.2.26.13 FullScreenLaunchComponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-fullscreenlaunchcomponent

#### 2.2.26.14 GridObjectSortComponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-gridobjectsortcomponent

#### 2.2.26.15 Popup:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-popup

#### 2.2.26.16 ProgressButton:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-progressbutton

#### 2.2.26.17 ProgressButtonV2:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-progressbuttonv2

#### 2.2.26.18 SegmentButton:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbutton

#### 2.2.26.19 SegmentButtonV2:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-segmentbuttonv2

#### 2.2.26.20 SelectTitleBar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selecttitlebar

#### 2.2.26.21 SelectionMenu:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-selectionmenu

#### 2.2.26.22 SplitLayout:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-splitlayout

#### 2.2.26.23 SubHeader:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheader

#### 2.2.26.24 SubHeaderV2:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-subheaderv2

#### 2.2.26.25 SwipeRefresher:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-swiperefresher

#### 2.2.26.26 TabTitleBar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-tabtitlebar

#### 2.2.26.27 ToolBar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-toolbar

#### 2.2.26.28 ToolBarV2:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-toolbarv2

#### 2.2.26.29 TreeView:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-treeview

#### 2.2.26.30 advanced.Counter:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-counter

### 2.2.27 状态管理与渲染控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/state-management-and-rendering-control

#### 2.2.27.1 应用级变量的状态管理:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management

#### 2.2.27.2 状态管理V1装饰器参数:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-v1-parameter

#### 2.2.27.3 状态变量变化监听:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-watch-monitor

#### 2.2.27.4 内置环境变量说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management-environment-variables

#### 2.2.27.5 ForEach:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-foreach

#### 2.2.27.6 LazyForEach:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach

#### 2.2.27.7 Repeat:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-repeat

### 2.2.28 响应式环境变量:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/responsive-env-system-property

#### 2.2.28.1 @Env：环境变量:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property

### 2.2.29 公共定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/common-definitions

#### 2.2.29.1 基础类型定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types

#### 2.2.29.2 像素单位:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-pixel-units

#### 2.2.29.3 枚举说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums

#### 2.2.29.4 设置事件回调:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-uicommonevent

### 2.2.30 已停止维护的组件与接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-declarative-comp-dep

#### 2.2.30.1 GridContainer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-gridcontainer

#### 2.2.30.2 Panel:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-panel

#### 2.2.30.3 NavRouter:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navrouter

#### 2.2.30.4 Navigator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-navigator

#### 2.2.30.5 点击控制:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-click

#### 2.2.30.6 栅格设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-grid

#### 2.2.30.7 Stepper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper

#### 2.2.30.8 StepperItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepperitem

## 2.3 JS组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-js-comp

### 2.3.1 兼容JS的类Web开发范式（ArkUI.Full）:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-js-full-comp

#### 2.3.1.1 组件通用信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-full-universal-comp-inform

##### 2.3.1.1.1 通用属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-attributes

##### 2.3.1.1.2 通用样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-styles

##### 2.3.1.1.3 通用事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-events

##### 2.3.1.1.4 通用方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-methods

##### 2.3.1.1.5 动画样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-animation

##### 2.3.1.1.6 渐变样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-gradient

##### 2.3.1.1.7 转场样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-transition

##### 2.3.1.1.8 媒体查询:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-mediaquery

##### 2.3.1.1.9 自定义字体样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-customizing-font

##### 2.3.1.1.10 原子布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-common-atomic-layout

#### 2.3.1.2 容器组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-full-container-comp

##### 2.3.1.2.1 badge:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-badge

##### 2.3.1.2.2 dialog:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-dialog

##### 2.3.1.2.3 div:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-div

##### 2.3.1.2.4 form:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-form

##### 2.3.1.2.5 list:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-list

##### 2.3.1.2.6 list-item:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-list-item

##### 2.3.1.2.7 list-item-group:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-list-item-group

##### 2.3.1.2.8 panel:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-panel

##### 2.3.1.2.9 popup:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-popup

##### 2.3.1.2.10 refresh:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-refresh

##### 2.3.1.2.11 stack:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stack

##### 2.3.1.2.12 stepper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stepper

##### 2.3.1.2.13 stepper-item:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-stepper-item

##### 2.3.1.2.14 swiper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-swiper

##### 2.3.1.2.15 tabs:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tabs

##### 2.3.1.2.16 tab-bar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tab-bar

##### 2.3.1.2.17 tab-content:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-container-tab-content

#### 2.3.1.3 基础组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-full-basic-comp

##### 2.3.1.3.1 button:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-button

##### 2.3.1.3.2 chart:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-chart

##### 2.3.1.3.3 divider:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-divider

##### 2.3.1.3.4 image:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-image

##### 2.3.1.3.5 image-animator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-image-animator

##### 2.3.1.3.6 input:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-input

##### 2.3.1.3.7 label:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-label

##### 2.3.1.3.8 marquee:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-marquee

##### 2.3.1.3.9 menu:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-menu

##### 2.3.1.3.10 option:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-option

##### 2.3.1.3.11 picker:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-picker

##### 2.3.1.3.12 picker-view:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-picker-view

##### 2.3.1.3.13 piece:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-piece

##### 2.3.1.3.14 progress:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-progress

##### 2.3.1.3.15 qrcode:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-qrcode

##### 2.3.1.3.16 rating:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-rating

##### 2.3.1.3.17 richtext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-richtext

##### 2.3.1.3.18 search:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-search

##### 2.3.1.3.19 select:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-select

##### 2.3.1.3.20 slider:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-slider

##### 2.3.1.3.21 span:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-span

##### 2.3.1.3.22 switch:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-switch

##### 2.3.1.3.23 text:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-text

##### 2.3.1.3.24 textarea:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-textarea

##### 2.3.1.3.25 toolbar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toolbar

##### 2.3.1.3.26 toolbar-item:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toolbar-item

##### 2.3.1.3.27 toggle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-toggle

##### 2.3.1.3.28 web:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-web

##### 2.3.1.3.29 xcomponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-basic-xcomponent

#### 2.3.1.4 媒体组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-full-media-comp

##### 2.3.1.4.1 video:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-media-video

#### 2.3.1.5 画布组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-full-canvas-comp

##### 2.3.1.5.1 canvas组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvas

##### 2.3.1.5.2 CanvasRenderingContext2D对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasrenderingcontext2d

##### 2.3.1.5.3 Image对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-image

##### 2.3.1.5.4 CanvasGradient对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-canvasgradient

##### 2.3.1.5.5 ImageData对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagedata

##### 2.3.1.5.6 Path2D对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-path2d

##### 2.3.1.5.7 ImageBitmap对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-imagebitmap

##### 2.3.1.5.8 OffscreenCanvas对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-canvas-offscreencanvas

##### 2.3.1.5.9 OffscreenCanvasRenderingContext2D对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-offscreencanvasrenderingcontext2d

#### 2.3.1.6 栅格组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-full-grid-comp

##### 2.3.1.6.1 基本概念:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-basic-concepts

##### 2.3.1.6.2 grid-container:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-container

##### 2.3.1.6.3 grid-row:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-row

##### 2.3.1.6.4 grid-col:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-grid-col

#### 2.3.1.7 svg组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-full-svg-comp

##### 2.3.1.7.1 通用属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-common-attributes

##### 2.3.1.7.2 svg:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg

##### 2.3.1.7.3 rect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-rect

##### 2.3.1.7.4 circle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-circle

##### 2.3.1.7.5 ellipse:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-ellipse

##### 2.3.1.7.6 path:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-path

##### 2.3.1.7.7 line:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-line

##### 2.3.1.7.8 polyline:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polyline

##### 2.3.1.7.9 polygon:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-polygon

##### 2.3.1.7.10 text:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-text

##### 2.3.1.7.11 tspan:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-tspan

##### 2.3.1.7.12 textPath:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-textpath

##### 2.3.1.7.13 animate:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animate

##### 2.3.1.7.14 animateMotion:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatemotion

##### 2.3.1.7.15 animateTransform:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-svg-animatetransform

#### 2.3.1.8 自定义组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-full-custom-comp

##### 2.3.1.8.1 自定义组件的基本用法:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-basic-usage

##### 2.3.1.8.2 数据传递与处理:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-props

##### 2.3.1.8.3 继承样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-style

##### 2.3.1.8.4 slot插槽:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-slot

##### 2.3.1.8.5 生命周期定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-custom-lifecycle

#### 2.3.1.9 动态创建组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-components-create-elements

#### 2.3.1.10 数据类型说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-appendix-types

### 2.3.2 兼容JS的类Web开发范式（ArkUI.Lite）:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-js-lite-comp

#### 2.3.2.1 框架说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-overview

##### 2.3.2.1.1 文件组织:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-file

##### 2.3.2.1.2 js标签配置:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-js-tag

##### 2.3.2.1.3 app.js:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-js-file

##### 2.3.2.1.4 生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-lifecycle

##### 2.3.2.1.5 多语言支持:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-localization

##### 2.3.2.1.6 语法:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-syntax

###### 2.3.2.1.6.1 HML语法参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-hml

###### 2.3.2.1.6.2 CSS语法参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-css

###### 2.3.2.1.6.3 JS语法参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-framework-syntax-js

#### 2.3.2.2 组件通用信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-universal-comp-inform

##### 2.3.2.2.1 通用事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-events

##### 2.3.2.2.2 通用属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-attributes

##### 2.3.2.2.3 通用样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-common-styles

##### 2.3.2.2.4 动画样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-common-animation

##### 2.3.2.2.5 媒体查询:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-common-mediaquery

#### 2.3.2.3 容器组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-container-comp

##### 2.3.2.3.1 div:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-div

##### 2.3.2.3.2 list:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-list

##### 2.3.2.3.3 list-item:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-list-item

##### 2.3.2.3.4 stack:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-stack

##### 2.3.2.3.5 swiper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-container-swiper

#### 2.3.2.4 基础组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-basic-comp

##### 2.3.2.4.1 chart:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-chart

##### 2.3.2.4.2 image:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-image

##### 2.3.2.4.3 image-animator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-image-animator

##### 2.3.2.4.4 input:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-input

##### 2.3.2.4.5 marquee:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-marquee

##### 2.3.2.4.6 picker-view:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-picker-view

##### 2.3.2.4.7 progress:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-progress

##### 2.3.2.4.8 qrcode:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-qrcode

##### 2.3.2.4.9 slider:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-slider

##### 2.3.2.4.10 switch:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-switch

##### 2.3.2.4.11 text:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-basic-text

#### 2.3.2.5 画布组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-canvas-comp

##### 2.3.2.5.1 canvas组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvas

##### 2.3.2.5.2 CanvasRenderingContext2D对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-lite-components-canvas-canvasrenderingcontext2d

### 2.3.3 JS服务卡片UI组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-card-comp

#### 2.3.3.1 框架说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/card-comp-framework-overview

##### 2.3.3.1.1 文件组织:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-file

##### 2.3.3.1.2 语法:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/card-comp-syntax

###### 2.3.3.1.2.1 HML语法参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-syntax-hml

###### 2.3.3.1.2.2 CSS语法参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-syntax-css

##### 2.3.3.1.3 多语言支持:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-multiple-languages

##### 2.3.3.1.4 版本兼容适配:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-version-compatibility

##### 2.3.3.1.5 设置主题样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-theme

#### 2.3.3.2 组件通用信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/card-comp-universal-comp-inform

##### 2.3.3.2.1 通用属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-attributes

##### 2.3.3.2.2 通用样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-styles

##### 2.3.3.2.3 通用事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-events

##### 2.3.3.2.4 渐变样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-gradient

##### 2.3.3.2.5 媒体查询:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-mediaquery

##### 2.3.3.2.6 自定义字体样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-customizing-font

##### 2.3.3.2.7 无障碍:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-accessibility

##### 2.3.3.2.8 原子布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-common-atomic-layout

#### 2.3.3.3 容器组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/card-comp-container-comp

##### 2.3.3.3.1 badge:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-badge

##### 2.3.3.3.2 div:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-div

##### 2.3.3.3.3 list:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-list

##### 2.3.3.3.4 list-item:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-list-item

##### 2.3.3.3.5 stack:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-stack

##### 2.3.3.3.6 swiper:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-container-swiper

#### 2.3.3.4 基础组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/card-comp-basic-comp

##### 2.3.3.4.1 button:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-button

##### 2.3.3.4.2 calendar:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-calendar

##### 2.3.3.4.3 chart:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-chart

##### 2.3.3.4.4 clock:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-clock

##### 2.3.3.4.5 divider:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-divider

##### 2.3.3.4.6 image:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-image

##### 2.3.3.4.7 input:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-input

##### 2.3.3.4.8 progress:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-progress

##### 2.3.3.4.9 span:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-span

##### 2.3.3.4.10 text:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-basic-text

#### 2.3.3.5 自定义组件使用说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-custom-basic-usage

#### 2.3.3.6 数据类型说明:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-service-widget-appendix-types

## 2.4 C API:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-c

### 2.4.1 模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-module

#### 2.4.1.1 ArkUI_NativeModule:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule

#### 2.4.1.2 ArkUI_Accessibility:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility

#### 2.4.1.3 OH_NativeXComponent Native XComponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent

#### 2.4.1.4 ArkUI_EventModule:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-eventmodule

#### 2.4.1.5 WindowManager:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager

#### 2.4.1.6 OH_DisplayManager:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-displaymanager

#### 2.4.1.7 ArkUI_RenderNodeUtils:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-rendernodeutils

### 2.4.2 头文件:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-headerfile

#### 2.4.2.1 drag_and_drop.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drag-and-drop-h

#### 2.4.2.2 drawable_descriptor.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawable-descriptor-h

#### 2.4.2.3 native_animate.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-animate-h

#### 2.4.2.4 native_dialog.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-dialog-h

#### 2.4.2.5 native_gesture.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-gesture-h

#### 2.4.2.6 native_interface.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-h

#### 2.4.2.7 native_interface_accessibility.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-accessibility-h

#### 2.4.2.8 native_interface_focus.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-focus-h

#### 2.4.2.9 native_interface_xcomponent.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-xcomponent-h

#### 2.4.2.10 native_key_event.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-key-event-h

#### 2.4.2.11 native_node.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-h

#### 2.4.2.12 native_node_napi.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-node-napi-h

#### 2.4.2.13 native_render.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-render-h

#### 2.4.2.14 native_type.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h

#### 2.4.2.15 native_xcomponent_key_event.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-xcomponent-key-event-h

#### 2.4.2.16 styled_string.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-styled-string-h

#### 2.4.2.17 ui_input_event.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ui-input-event-h

#### 2.4.2.18 oh_window.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-h

#### 2.4.2.19 oh_window_comm.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-comm-h

#### 2.4.2.20 oh_window_event_filter.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-event-filter-h

#### 2.4.2.21 oh_window_pip.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-window-pip-h

#### 2.4.2.22 oh_display_capture.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-capture-h

#### 2.4.2.23 oh_display_info.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-info-h

#### 2.4.2.24 oh_display_manager.h:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-display-manager-h

### 2.4.3 结构体:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-struct

#### 2.4.3.1 ArkUI_NodeEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeevent

#### 2.4.3.2 ArkUI_Context:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-context

#### 2.4.3.3 ArkUI_Context*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-context8h

#### 2.4.3.4 ArkUI_DragEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragevent

#### 2.4.3.5 ArkUI_DragPreviewOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragpreviewoption

#### 2.4.3.6 ArkUI_DragAction:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragaction

#### 2.4.3.7 ArkUI_DragAndDropInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-draganddropinfo

#### 2.4.3.8 ArkUI_DrawableDescriptor:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-drawabledescriptor

#### 2.4.3.9 ArkUI_DrawableDescriptor_AnimationController:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/module-arkui-drawabledescriptoranimationcontroller

#### 2.4.3.10 OH_PixelmapNative*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-pixelmapnative8h

#### 2.4.3.11 ArkUI_ExpectedFrameRateRange:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-expectedframeraterange

#### 2.4.3.12 ArkUI_AnimateCompleteCallback:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-animatecompletecallback

#### 2.4.3.13 ArkUI_NativeAnimateAPI_1:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativeanimateapi-1

#### 2.4.3.14 ArkUI_AnimateOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animateoption

#### 2.4.3.15 ArkUI_Curve:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve

#### 2.4.3.16 ArkUI_Curve*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-curve8h

#### 2.4.3.17 ArkUI_KeyframeAnimateOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-keyframeanimateoption

#### 2.4.3.18 ArkUI_AnimatorOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoroption

#### 2.4.3.19 ArkUI_Animator*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animator8h

#### 2.4.3.20 ArkUI_AnimatorEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatorevent

#### 2.4.3.21 ArkUI_AnimatorOnFrameEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-animatoronframeevent

#### 2.4.3.22 ArkUI_TransitionEffect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-transitioneffect

#### 2.4.3.23 ArkUI_NativeDialogAPI_1:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-1

#### 2.4.3.24 ArkUI_NativeDialogAPI_2:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-2

#### 2.4.3.25 ArkUI_NativeDialogAPI_3:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialogapi-3

#### 2.4.3.26 ArkUI_DialogDismissEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dialogdismissevent

#### 2.4.3.27 ArkUI_CustomDialogOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customdialogoptions

#### 2.4.3.28 ArkUI_NativeGestureAPI_1:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-1

#### 2.4.3.29 ArkUI_NativeGestureAPI_2:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativegestureapi-2

#### 2.4.3.30 ArkUI_GestureRecognizer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gesturerecognizer

#### 2.4.3.31 ArkUI_GestureInterruptInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gestureinterruptinfo

#### 2.4.3.32 ArkUI_GestureEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gestureevent

#### 2.4.3.33 ArkUI_GestureEventTargetInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-gestureeventtargetinfo

#### 2.4.3.34 ArkUI_ParallelInnerGestureEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-nativemodule-arkui-parallelinnergestureevent

#### 2.4.3.35 ArkUI_TouchRecognizer:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchrecognizer

#### 2.4.3.36 ArkUI_TouchRecognizer*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-touchrecognizerhandle

#### 2.4.3.37 ArkUI_TouchRecognizerHandle*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rkui-nativemodule-arkui-touchrecognizerhandlearray

#### 2.4.3.38 ArkUI_GestureRecognizer*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-gesturerecognizerhandle

#### 2.4.3.39 ArkUI_GestureRecognizerHandle*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-nativemodule-arkui-gesturerecognizerhandlearray

#### 2.4.3.40 ArkUI_AccessibleAction:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibleaction

#### 2.4.3.41 ArkUI_AccessibleRect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblerect

#### 2.4.3.42 ArkUI_AccessibleRangeInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblerangeinfo

#### 2.4.3.43 ArkUI_AccessibleGridInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegridinfo

#### 2.4.3.44 ArkUI_AccessibleGridItemInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-accessibility-arkui-accessiblegriditeminfo

#### 2.4.3.45 ArkUI_AccessibilityProviderCallbacks:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/accessibility-arkui-accessibilityprovidercallbacks

#### 2.4.3.46 ArkUI_AccessibilityProviderCallbacksWithInstance:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/y-arkui-accessibilityprovidercallbackswithinstance

#### 2.4.3.47 ArkUI_AccessibilityElementInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-accessibility-arkui-accessibilityelementinfo

#### 2.4.3.48 ArkUI_AccessibilityEventInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-accessibility-arkui-accessibilityeventinfo

#### 2.4.3.49 ArkUI_AccessibilityProvider:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-accessibility-arkui-accessibilityprovider

#### 2.4.3.50 ArkUI_AccessibilityActionArguments:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-accessibility-arkui-accessibilityactionarguments

#### 2.4.3.51 ArkUI_AccessibilityElementInfoList:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-accessibility-arkui-accessibilityelementinfolist

#### 2.4.3.52 OH_NativeXComponent_HistoricalPoint:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ive-xcomponent-oh-nativexcomponent-historicalpoint

#### 2.4.3.53 OH_NativeXComponent_TouchPoint:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/t-native-xcomponent-oh-nativexcomponent-touchpoint

#### 2.4.3.54 OH_NativeXComponent_TouchEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/t-native-xcomponent-oh-nativexcomponent-touchevent

#### 2.4.3.55 OH_NativeXComponent_MouseEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/t-native-xcomponent-oh-nativexcomponent-mouseevent

#### 2.4.3.56 OH_NativeXComponent_Callback:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-callback

#### 2.4.3.57 OH_NativeXComponent_MouseEvent_Callback:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xcomponent-oh-nativexcomponent-mouseevent-callback

#### 2.4.3.58 OH_NativeXComponent_ExpectedRateRange:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/e-xcomponent-oh-nativexcomponent-expectedraterange

#### 2.4.3.59 OH_NativeXComponent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/vexcomponent-native-xcomponent-oh-nativexcomponent

#### 2.4.3.60 OH_NativeXComponent_KeyEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ent-native-xcomponent-oh-nativexcomponent-keyevent

#### 2.4.3.61 OH_NativeXComponent_ExtraMouseEventInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xcomponent-oh-nativexcomponent-extramouseeventinfo

#### 2.4.3.62 OH_ArkUI_SurfaceHolder:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/component-native-xcomponent-oh-arkui-surfaceholder

#### 2.4.3.63 OH_ArkUI_SurfaceCallback:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/mponent-native-xcomponent-oh-arkui-surfacecallback

#### 2.4.3.64 NativeWindow:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/oh-nativexcomponent-native-xcomponent-nativewindow

#### 2.4.3.65 ArkUI_XComponentSurfaceConfig:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nt-native-xcomponent-arkui-xcomponentsurfaceconfig

#### 2.4.3.66 ArkUI_AttributeItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-attributeitem

#### 2.4.3.67 ArkUI_NodeComponentEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecomponentevent

#### 2.4.3.68 ArkUI_StringAsyncEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-stringasyncevent

#### 2.4.3.69 ArkUI_TextChangeEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textchangeevent

#### 2.4.3.70 ArkUI_NativeNodeAPI_1:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1

#### 2.4.3.71 ArkUI_NodeCustomEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecustomevent

#### 2.4.3.72 ArkUI_NodeAdapter*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeadapter8h

#### 2.4.3.73 ArkUI_NodeAdapterEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeadapterevent

#### 2.4.3.74 ArkUI_NodeContentEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecontentevent

#### 2.4.3.75 ArkUI_ContextCallback:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-contextcallback

#### 2.4.3.76 ArkUI_NumberValue:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-numbervalue

#### 2.4.3.77 ARKUI_TextPickerRangeContent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-textpickerrangecontent

#### 2.4.3.78 ARKUI_TextPickerCascadeRangeContent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-nativemodule-arkui-textpickercascaderangecontent

#### 2.4.3.79 ArkUI_ColorStop:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-colorstop

#### 2.4.3.80 ArkUI_Rect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rect

#### 2.4.3.81 ArkUI_IntSize:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-intsize

#### 2.4.3.82 ArkUI_IntOffset:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-intoffset

#### 2.4.3.83 ArkUI_Margin:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-margin

#### 2.4.3.84 ArkUI_TranslationOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-translationoptions

#### 2.4.3.85 ArkUI_ScaleOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-scaleoptions

#### 2.4.3.86 ArkUI_RotationOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rotationoptions

#### 2.4.3.87 ArkUI_NativeDialog:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog

#### 2.4.3.88 ArkUI_LayoutConstraint:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-layoutconstraint

#### 2.4.3.89 ArkUI_DrawContext:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-drawcontext

#### 2.4.3.90 ArkUI_Node:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node-descriptor

#### 2.4.3.91 ArkUI_Node*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-node8h

#### 2.4.3.92 ArkUI_NativeDialog*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nativedialog8h

#### 2.4.3.93 ArkUI_WaterFlowSectionOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-waterflowsectionoption

#### 2.4.3.94 ArkUI_ListItemSwipeActionItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-listitemswipeactionitem

#### 2.4.3.95 ArkUI_ListItemSwipeActionOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-nativemodule-arkui-listitemswipeactionoption

#### 2.4.3.96 ArkUI_NodeContent*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodecontent8h

#### 2.4.3.97 ArkUI_AlignmentRuleOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-alignmentruleoption

#### 2.4.3.98 ArkUI_GuidelineOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-guidelineoption

#### 2.4.3.99 ArkUI_BarrierOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-barrieroption

#### 2.4.3.100 ArkUI_ImageAnimatorFrameInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-imageanimatorframeinfo

#### 2.4.3.101 ArkUI_ListChildrenMainSize:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-listchildrenmainsize

#### 2.4.3.102 ArkUI_ProgressLinearStyleOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-nativemodule-arkui-progresslinearstyleoption

#### 2.4.3.103 ArkUI_CustomProperty:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customproperty

#### 2.4.3.104 ArkUI_HostWindowInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-hostwindowinfo

#### 2.4.3.105 ArkUI_ActiveChildrenInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-activechildreninfo

#### 2.4.3.106 ArkUI_CrossLanguageOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-crosslanguageoption

#### 2.4.3.107 AbilityBase_Want:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-abilitybase-want

#### 2.4.3.108 ArkUI_EmbeddedComponentOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-embeddedcomponentoption

#### 2.4.3.109 ArkUI_AccessibilityState:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-accessibilitystate

#### 2.4.3.110 ArkUI_AccessibilityValue:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-accessibilityvalue

#### 2.4.3.111 ArkUI_SystemFontStyleEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-systemfontstyleevent

#### 2.4.3.112 ArkUI_CustomSpanMeasureInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-customspanmeasureinfo

#### 2.4.3.113 ArkUI_CustomSpanMetrics:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customspanmetrics

#### 2.4.3.114 ArkUI_CustomSpanDrawInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-customspandrawinfo

#### 2.4.3.115 ArkUI_SwiperIndicator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-swiperindicator

#### 2.4.3.116 ArkUI_SwiperDigitIndicator:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-swiperdigitindicator

#### 2.4.3.117 ArkUI_SwiperArrowStyle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-swiperarrowstyle

#### 2.4.3.118 ArkUI_StyledString_Descriptor:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-styledstring-descriptor

#### 2.4.3.119 ArkUI_SnapshotOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-snapshotoptions

#### 2.4.3.120 ArkUI_TextPickerRangeContentArray:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kui-nativemodule-arkui-textpickerrangecontentarray

#### 2.4.3.121 ArkUI_TextCascadePickerRangeContentArray:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ivemodule-arkui-textcascadepickerrangecontentarray

#### 2.4.3.122 ArkUI_VisibleAreaEventOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-visibleareaeventoptions

#### 2.4.3.123 ArkUI_PositionEdges:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-positionedges

#### 2.4.3.124 ArkUI_PixelRoundPolicy:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-pixelroundpolicy

#### 2.4.3.125 ArkUI_StyledString:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-styledstring

#### 2.4.3.126 ArkUI_TextLayoutManager:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textlayoutmanager

#### 2.4.3.127 ArkUI_UIInputEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-eventmodule-arkui-uiinputevent

#### 2.4.3.128 ArkUI_ShowCounterConfig:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-textshowcounterconfig

#### 2.4.3.129 PictureInPicture_PipConfig:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pictureinpicture-pipconfig

#### 2.4.3.130 WindowManager_Rect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-rect

#### 2.4.3.131 OH_PixelmapNative:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-struct

#### 2.4.3.132 WindowManager_WindowProperties:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowproperties

#### 2.4.3.133 WindowManager_AvoidArea:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-avoidarea

#### 2.4.3.134 WindowManager_MainWindowInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-windowmanager-windowmanager-mainwindowinfo

#### 2.4.3.135 WindowManager_WindowSnapshotConfig:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-windowmanager-windowmanager-windowsnapshotconfig

#### 2.4.3.136 NativeDisplayManager_Rect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-rect

#### 2.4.3.137 NativeDisplayManager_WaterfallDisplayAreaRects:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-nativedisplaymanager-waterfalldisplayarearects

#### 2.4.3.138 NativeDisplayManager_CutoutInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-cutoutinfo

#### 2.4.3.139 NativeDisplayManager_DisplayHdrFormat:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayhdrformat

#### 2.4.3.140 NativeDisplayManager_DisplayColorSpace:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaycolorspace

#### 2.4.3.141 NativeDisplayManager_DisplayInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displayinfo

#### 2.4.3.142 NativeDisplayManager_DisplaysInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-nativedisplaymanager-displaysinfo

#### 2.4.3.143 ArkUI_CircleShapeOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-circleshapeoption

#### 2.4.3.144 ArkUI_ColorAnimatablePropertyHandle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-nativemodule-arkui-coloranimatablepropertyhandle

#### 2.4.3.145 ArkUI_ColorPropertyHandle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-colorpropertyhandle

#### 2.4.3.146 ArkUI_CommandPathOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-commandpathoption

#### 2.4.3.147 ArkUI_FloatAnimatablePropertyHandle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-nativemodule-arkui-floatanimatablepropertyhandle

#### 2.4.3.148 ArkUI_FloatPropertyHandle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-floatpropertyhandle

#### 2.4.3.149 ArkUI_NodeBorderColorOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-nodebordercoloroption

#### 2.4.3.150 ArkUI_NodeBorderRadiusOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-nodeborderradiusoption

#### 2.4.3.151 ArkUI_NodeBorderStyleOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-nodeborderstyleoption

#### 2.4.3.152 ArkUI_NodeBorderWidthOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-nodeborderwidthoption

#### 2.4.3.153 ArkUI_RectShapeOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rectshapeoption

#### 2.4.3.154 ArkUI_RenderContentModifierHandle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kui-nativemodule-arkui-rendercontentmodifierhandle

#### 2.4.3.155 ArkUI_RenderNodeClipOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rendernodeclipoption

#### 2.4.3.156 ArkUI_RenderNodeHandle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rendernodehandle

#### 2.4.3.157 ArkUI_RenderNodeMaskOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rendernodemaskoption

#### 2.4.3.158 ArkUI_RoundRectShapeOption:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-roundrectshapeoption

#### 2.4.3.159 ArkUI_Vector2AnimatablePropertyHandle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nativemodule-arkui-vector2animatablepropertyhandle

#### 2.4.3.160 ArkUI_Vector2PropertyHandle:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-arkui-nativemodule-arkui-vector2propertyhandle

#### 2.4.3.161 ArkUI_ContentTransitionEffect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-contenttransitioneffect

#### 2.4.3.162 ArkUI_CoastingAxisEvent:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-coastingaxisevent

#### 2.4.3.163 ArkUI_GridItemRect:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemrect

#### 2.4.3.164 ArkUI_GridItemSize:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-griditemsize

#### 2.4.3.165 ArkUI_GridLayoutOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gridlayoutoptions

#### 2.4.3.166 ArkUI_TouchTestInfo:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfo

#### 2.4.3.167 ArkUI_TouchTestInfoItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-touchtestinfoitem

#### 2.4.3.168 ArkUI_TouchTestInfoItem*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-arkui-nativemodule-arkui-touchtestinfoitemhandle

#### 2.4.3.169 ArkUI_TouchTestInfoItemHandle*:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-nativemodule-arkui-touchtestinfoitemhandlearray

#### 2.4.3.170 ArkUI_TextMenuItem:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textmenuitem

#### 2.4.3.171 ArkUI_TextMenuItemArray:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-textmenuitemarray

#### 2.4.3.172 ArkUI_TextEditMenuOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-texteditmenuoptions

#### 2.4.3.173 ArkUI_TextSelectionMenuOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-arkui-nativemodule-arkui-textselectionmenuoptions

## 2.5 错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-arkts-errcode

### 2.5.1 UI界面:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-ui-arkts-errcode

#### 2.5.1.1 接口调用异常错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-internal

#### 2.5.1.2 弹窗错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-promptaction

#### 2.5.1.3 页面路由错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-router

#### 2.5.1.4 拖拽事件错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drag-event

#### 2.5.1.5 图像AI分析错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image-analyzer

#### 2.5.1.6 焦点错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-focus

#### 2.5.1.7 系统资源错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-system-resource

#### 2.5.1.8 附属节点错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-adopt

#### 2.5.1.9 半模态错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-bindsheet

#### 2.5.1.10 滚动类组件错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-scroll

#### 2.5.1.11 截图错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-snapshot

#### 2.5.1.12 属性字符串错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-styled-string

#### 2.5.1.13 UI上下文错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uicontext

#### 2.5.1.14 注册节点渲染状态监听错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node-render-monitor

#### 2.5.1.15 交互事件错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-event

#### 2.5.1.16 Canvas组件错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-canvas

#### 2.5.1.17 自定义节点错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node

#### 2.5.1.18 UIExtension错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uiextension

#### 2.5.1.19 用户界面外观服务错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uiappearance

#### 2.5.1.20 NodeAdapter错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-nodeadapter

#### 2.5.1.21 XComponent组件错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-xcomponent

#### 2.5.1.22 Video组件错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-video

#### 2.5.1.23 状态管理错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-statemanagement

#### 2.5.1.24 渲染节点错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node-render

#### 2.5.1.25 DrawableDescriptor错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-drawable-descriptor

#### 2.5.1.26 环境变量错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-env

#### 2.5.1.27 反色能力错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-force-dark

### 2.5.2 图形图像:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-graphics-images-arkts-errcode

#### 2.5.2.1 屏幕错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-display

#### 2.5.2.2 窗口错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-window

### 2.5.3 UI编译:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-compile-arkts-errcode

#### 2.5.3.1 编译错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_ark_ui_compile

---

# 3 最佳实践-组件封装与复用

## 3.1 组件封装与复用:

### 3.1.1 组件动态创建:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ui-dynamic-operations

### 3.1.2 组件封装:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ui-component-encapsulation

### 3.1.3 组件复用:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-reuse

### 3.1.4 组件复用问题诊断分析:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-reuse-issue-diagnosis-and-analysis

---

# 4 最佳实践-布局与弹窗

## 4.1 布局与弹窗:

### 4.1.1 文本展开折叠:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-text-expand-collapse

### 4.1.2 布局优化指导:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance

### 4.1.3 常见列表流:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-common-list-flows

### 4.1.4 Grid网格元素拖拽交换:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-grid-drag-swap

### 4.1.5 使用Swiper组件实现轮播图:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-carousel-graphic-works

### 4.1.6 图片预览器:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-picture-preview

### 4.1.7 自定义弹窗选型与开发:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-customdialog-selection-and-development

### 4.1.8 评论回复弹窗:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-comment-reply-pop-up-window

### 4.1.9 基于DialogHub的通用弹窗:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hadss_dialoghub

### 4.1.10 基于ScrollComponents实现瀑布流:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-waterflow-based-on-scrollcomponents

### 4.1.11 常见瀑布流操作:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-waterflow-operations

### 4.1.12 基于ScrollComponents实现网格:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-grid-based-on-scrollcomponents

### 4.1.13 基于ScrollComponents实现长列表:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-list-based-on-scrollcomponents

### 4.1.14 Tabs选项卡常见开发场景:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-development-scenarios-for-tabs

### 4.1.15 常见列表操作:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-common-list-operations

### 4.1.16 弹窗组件封装:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dialog-encapsulation

### 4.1.17 富文本显示的选型与开发:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-rich-text-display

### 4.1.18 实现富文本编辑器:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-rich-text-editor

---

# 5 最佳实践-声明式语法

## 5.1 声明式语法:

### 5.1.1 状态管理最佳实践:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-status-management

### 5.1.2 组件冗余刷新解决方案:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-redundancy-refresh-guide

### 5.1.3 基于StateStore的全局状态管理:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-global-state-management-state-store

---

# 6 最佳实践-手势与导航

## 6.1 手势与导航:

### 6.1.1 常见导航样式案例:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-tab-practice

### 6.1.2 基于HMRouter的页面跳转:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hmrouter

### 6.1.3 手势事件冲突解决方案:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-gestures-practice

---

# 7 最佳实践-动画与转场

## 7.1 动画与转场:

### 7.1.1 动画使用指导:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fair-use-animation

### 7.1.2 页面间转场:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-page-transition

### 7.1.3 一镜到底动效:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-one-shot-to-the-end

---

# 8 最佳实践-主题与样式

## 8.1 主题与样式:

### 8.1.1 深色模式适配:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dark-mode-adaptation

### 8.1.2 页面亮度设置:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-page-brightness-settings

### 8.1.3 自定义字体设置:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-custom-font-settings

### 8.1.4 基于colorFilter实现图片滤镜效果:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-implementing-image-filters

### 8.1.5 基于resizable实现图片拉伸效果:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-implementing-image-resizable

---

# 9 ArkUI（方舟UI框架）FAQ:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-kit

## 9.1 Image组件加载的图片，如何缓解图片在缩放时的锯齿问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1

## 9.2 如何对手势事件进行限流防止连续识别，例如500ms内不允许点击事件重复触发？如何对多个手势进行统一限流:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-394

## 9.3 如何实现防截屏功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-3

## 9.4 如何在长按手势回调方法里获取手指触摸点的坐标:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-4

## 9.5 如何自定义Tabs页签导航栏及其对齐方式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-5

## 9.6 如何在可滚动的容器组件中实现曝光埋点:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-7

## 9.7 如何给UI组件设置不同情况下的属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-8

## 9.8 如何在Navigation跳转页面时返回传参:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-12

## 9.9 TextInput组件获取焦点的几种场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-13

## 9.10 RichEditor组件如何设置光标的起始位置位于左上角:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-14

## 9.11 如何实现软键盘弹出后，整体布局不变:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-16

## 9.12 如何实现Tabs页签导航栏切换时，下划线也随之滑动:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-17

## 9.13 如何解决Web与List的嵌套滑动冲突:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-18

## 9.14 如何解决两层Tabs出现滑动冲突的情况:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-19

## 9.15 如何主动清除控件的焦点:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-20

## 9.16 如何加载和使用自定义字体:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-21

## 9.17 如何选择图文混排的实现方案:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-23

## 9.18 如何实现分组列表的吸顶/吸底效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-25

## 9.19 如何解决List组件在不设置高度的情况下滑动不到底的问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-26

## 9.20 List组件如何实现多列效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-27

## 9.21 如何设置分组列表的圆角和间距:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-28

## 9.22 如何获取UI组件的显示或隐藏状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-30

## 9.23 如何实现类似插槽的功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-31

## 9.24 如何解决子组件全屏后margin不会生效的问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-32

## 9.25 如何通过PanGesture手势或者SwipeGesture手势实现自定义组件的惯性滚动效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-33

## 9.26 如何监听当前屏幕的横竖屏状态？如何实现页面跟随屏幕横竖屏自动旋转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-34

## 9.27 如何处理父子组件间的事件传递，例如，如何解决滑动冲突:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-40

## 9.28 使用ForEach&LazyForEach循环渲染时，会出现更改数据源时，界面不刷新的情况。如何解决:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-41

## 9.29 在使用Canvas的场景中，如何主动控制组件刷新UI:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-42

## 9.30 如何在键盘弹出时仅调整指定UI组件的位置，而不影响整体布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-43

## 9.31 组件支持的参数类型及参数单位类型：PX、 VP、 FP 、LPX、Percentage、Resource 详细区别是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-45

## 9.32 Text组件如何加载Unicode字符:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-46

## 9.33 自定义字体的注册方式是什么，如何从资源存放路径中取出字体资源:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-47

## 9.34 AppStorage是否支持线程间共享对象，如果不支持，推荐替代方案是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-49

## 9.35 如何在自定义组件的构建流程里跟踪组件数据或者状态，如在build里增加日志跟踪状态变量等:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-50

## 9.36 如何在键盘弹出时，让内容上移，而不是整个页面上移:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-53

## 9.37 输入框拉起键盘时，如何将底部布局弹起到键盘顶部:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-54

## 9.38 图片如何添加渐变模糊:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-55

## 9.39 如何去除Tabs组件两侧的蒙层:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-56

## 9.40 如何获取Text组件中文字的宽度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-57

## 9.41 如何设置自定义组件height缺省:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-58

## 9.42 弹窗组件无法进入onPageShow方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-59

## 9.43 Navigation的toolbar中设置大图标时被切断:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-60

## 9.44 Image无法使用bindContextMenu:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-61

## 9.45 SideBarContainer如何设置controlButton属性:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-65

## 9.46 如何监听屏幕旋转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-66

## 9.47 如何设置窗口旋转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-67

## 9.48 父组件如何与孙子组件进行状态同步:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-69

## 9.49 如何一键清空TextInput、TextArea组件内容:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-80

## 9.50 如何设置自定义弹窗位置:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-81

## 9.51 如何理解自定义弹窗（CustomDialog）中的gridCount参数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-84

## 9.52 TextInput组件密码模式下，右边的眼睛图标能否支持自定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-86

## 9.53 TextInput的onSubmit事件如何使用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-87

## 9.54 TextInput在聚焦时如何使光标回到起点:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-88

## 9.55 如何获取组件的属性信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-89

## 9.56 如何获取可滚动组件的当前滚动偏移量:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-90

## 9.57 如何实现文本竖向排列:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-91

## 9.58 TimePicker组件中文本的颜色和大小是否可以自定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-94

## 9.59 ConstraintSize尺寸设置不生效:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-95

## 9.60 如何将背景颜色设置为透明:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-96

## 9.61 如何自定义Video组件控制栏样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-97

## 9.62 如何设置组件不同状态下的样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-98

## 9.63 如何主动拉起软键盘:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-100

## 9.64 如何在List组件中分组展示不同种类的数据:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-101

## 9.65 通过$r访问应用资源是否支持嵌套形式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-102

## 9.66 Button组件如何设置渐变背景色:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-103

## 9.67 滑动的页面软键盘挡住内容不能向上滑动:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-105

## 9.68 TextInput如何限制输入字符为某些字符:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-106

## 9.69 如何根据组件内容大小修改浮动窗口:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-107

## 9.70 List组件如何设置多列:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-109

## 9.71 如何设置区分TabBar和TabContent的分割线样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-111

## 9.72 为何RichText组件中内容可以滚动:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-112

## 9.73 如何设置List组件滑动到边缘无回弹效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-113

## 9.74 ArkUI中icon资源锯齿感严重:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-114

## 9.75 如何实现多行输入:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-116

## 9.76 文本组件是否支持分段设置字体样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-117

## 9.77 如何修改状态栏字体颜色:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-118

## 9.78 弹窗弹出时，输入框如何用代码设置全选:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-119

## 9.79 文字空行高度与字体高度不一致:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-121

## 9.80 TextInput组件包含英文和汉字时，如何设置全选:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-122

## 9.81 Color支持哪些格式，使用color: 'rgba(0, 0, 255, .5)'格式不生效:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-123

## 9.82 TextInput按压态背景色如何修改:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-124

## 9.83 组件最大和最小宽度和高度如何设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-125

## 9.84 XComponent组件如何设置背景颜色:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-126

## 9.85 组件如何设置模糊效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-128

## 9.86 UI布局默认是多少vp为基准，以达到不同机器自适应:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-129

## 9.87 如何获取与设置屏幕亮度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-132

## 9.88 TextInput是否能自定义hover效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-133

## 9.89 如何去除tabbar滑动到边缘时的蒙层效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-134

## 9.90 如何实现两层Tab嵌套滑动的效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-135

## 9.91 Grid组件的scrollBar是否支持自定义:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-136

## 9.92 List组件如何设置两端的渐变效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-137

## 9.93 过长文字如何滚动显示:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-138

## 9.94 XComponent 怎么设置成透明:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-139

## 9.95 半模态转场如何控制固定高度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-142

## 9.96 如何实现拖拽时列表项占位动画的效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-143

## 9.97 ArkUI组件的字符串中如何实现字符串变量拼接:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-144

## 9.98 控制中心的下拉背景实时模糊是如何实现的:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-145

## 9.99 如何获取图片的宽高:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-146

## 9.100 如何解决Web页面输入框拉起键盘后，页面头部被截断的问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-148

## 9.101 Navigation如何隐藏导航栏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-149

## 9.102 如何设置子组件宽度使其不超过父组件的大小:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-152

## 9.103 Image或者ImageSpan传入一个string类型的路径时无法加载图片:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-153

## 9.104 Image组件如何读入沙箱内的图片:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-154

## 9.105 如何实现事件透传:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-155

## 9.106 Text组件设置maxLines后如何确定文本是否被隐藏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-156

## 9.107 如何实现类似keyframes的效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-157

## 9.108 外部容器Stack能否满足适应内部容器组件的圆角等样式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-159

## 9.109 Stack布局设置Alignment.Bottom没有生效:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160

## 9.110 布局是否支持css里的calc(100vh - 100px)类似能力:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-161

## 9.111 如何获取router.back传递的参数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-164

## 9.112 焦点事件onBlur/onFocus回调无法触发:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-165

## 9.113 Scroll里面套一个grid，如何禁用grid的滑动事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-166

## 9.114 如何实现一个组件不停地旋转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-167

## 9.115 键盘拉起时列表无法上下滑动:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-168

## 9.116 键盘移动焦点对象按下enter，为什么不会触发点击事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-169

## 9.117 多层组件嵌套Button，如何阻止事件传递:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-170

## 9.118 在容器组件嵌套的场景下，如何解决手势拖拽事件出现错乱的问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-172

## 9.119 当父组件绑定了onTouch，其子组件Button绑定了onClick，如何做到点击Button只响应Button的onClick，而不用响应父组件的onTouch:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-174

## 9.120 点击文本输入框，如何屏蔽系统默认键盘弹起行为:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-176

## 9.121 如何阻止组件的鼠标事件冒泡到父组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-177

## 9.122 如何实现上下切换的页面间跳转动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-178

## 9.123 自定义组件间如何实现从底部滑入滑出的效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-179

## 9.124 子组件事件能否传递到父组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-180

## 9.125 文档中提到键鼠事件可以设置冒泡阻断，其他事件是否支持:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-181

## 9.126 组件被隐藏后 onVisibleAreaChange 事件触发了两次:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-183

## 9.127 @Watch是否有粘性的概念:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-184

## 9.128 使用@Watch监听并在回调函数中调用其他异步接口时UI响应慢:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-185

## 9.129 如何移除页面上Video组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-187

## 9.130 触摸事件的TouchEvent调用stopPropagation时无法阻止事件分发:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-188

## 9.131 如何获取窗口的宽高信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-190

## 9.132 通用属性width是否支持设置变量:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-191

## 9.133 如何判断JS对象中是否存在某个值:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-192

## 9.134 应用如何设置隐藏顶部的状态栏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-193

## 9.135 如何锁定设备竖屏，使得窗口不随屏幕旋转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-194

## 9.136 调用window实例的setWindowSystemBarProperties接口设置窗口状态栏和导航栏的高亮属性时不生效:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-195

## 9.137 如何保持屏幕常亮:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-196

## 9.138 如何监听窗口大小的变化:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-197

## 9.139 如何获取屏幕的宽度、高度、分辨率和横竖屏等信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-198

## 9.140 如何设置沉浸式窗口:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-199

## 9.141 如何获取窗口的宽度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-200

## 9.142 如何解决window创建的模态窗口默认焦点不在界面上，导致不响应返回事件的问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-201

## 9.143 如何获取状态栏和导航栏高度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-202

## 9.144 如何实现Tabs组件的TabBar居左对齐:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-205

## 9.145 如何进行页面横竖屏切换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-206

## 9.146 是否有处理"9图"（又称"draw9patch"、".9图"、"点9图"等）的平替方案:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-208

## 9.147 ArkUI有没有在组件刷新后的回调事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-209

## 9.148 如何在自定义弹窗中再次弹窗:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-210

## 9.149 Grid如何实现拖拽功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-211

## 9.150 如何设置沉浸式状态栏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-214

## 9.151 如何动态控制键盘绑定在不同的TextInput上:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-215

## 9.152 如何使用iconfont:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-216

## 9.153 Image组件是否有缓存机制:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-217

## 9.154 ForEach键值生成规则是怎样的:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-219

## 9.155 Flex布局与w3c中的Flex是否有差异:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-220

## 9.156 ArkUI组件能否支持继承:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-221

## 9.157 @Style 和 @Extend 是否支持export导出:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-222

## 9.158 Canvas绘制内容如何动态更新:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-225

## 9.159 组件是否支持泛型:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-226

## 9.160 自定义组件是否能通过容器保存:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-228

## 9.161 使用BuilderParam在父组件调用this的方法报错：Error message: undefined is not callable:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-229

## 9.162 Component如何监听应用前后台切换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-230

## 9.163 自定义组件如何实现类似系统组件的链式调用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-231

## 9.164 自定义组件在外部设置属性方法和在build方法内部设置有什么区别:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-232

## 9.165 如何实现页面加载的loading效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-233

## 9.166 如何实现下拉刷新和上滑加载的效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-235

## 9.167 如何正确获取刘海区域的高度，topRect中的取值是height、top还是height+top:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-236

## 9.168 应用开启禁止截屏之后，系统将如何处理用户的截屏和录屏操作:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-237

## 9.169 在屏幕底部的组件的响应区域是否存在遮挡:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-238

## 9.170 如何获取设备屏幕横竖屏状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-239

## 9.171 创建subwindow默认是否铺满全屏，铺满全屏时如何隐藏状态栏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-240

## 9.172 如何让Grid组件在高度不确定的情况下，实现自适应高度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-241

## 9.173 如何获取手机屏幕信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-242

## 9.174 如何解决点击子组件模块区域会触发父组件的点击事件问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-243

## 9.175 当子组件触发触摸事件时，如果父组件也设置了触摸事件，如何解决父组件同时被触发的问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-244

## 9.176 使用0x八位颜色设置渐变透明度为什么与#八位资源颜色值不同:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-245

## 9.177 如何实现背景跟随文字大小改变:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-246

## 9.178 ListItemGroup和LazyForEach如何结合使用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-247

## 9.179 如何设置Text的字体，可以不受系统设置里显示大小缩放的影响:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-248

## 9.180 如何获取底部手势横条的高度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-249

## 9.181 如何实现列表既可以左右滑、又可以上下滑动:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-250

## 9.182 如何使用Swiper组件实现下拉刷新:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-251

## 9.183 为什么vp2px、px2vp返回的结果不正确:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-259

## 9.184 是否navigation有最大页面数量限制？router栈的栈最大是32个，超过32个是无响应还是报错:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-260

## 9.185 如何使用Navigation的navPathStack参数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-262

## 9.186 Navigation容器中，如何设置子组件的高度为100%，撑满父容器:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-263

## 9.187 Navigation中pushPathByName与pushDestinationByName的区别:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-264

## 9.188 如何实现点击输入框时会拉起软键盘，点击Button时软键盘关闭:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-265

## 9.189 如何获取屏幕顶部状态栏、底部导航栏和导航条的高度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-266

## 9.190 如何实现文本展开收起功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-267

## 9.191 List的下拉加载如何回滚到当前展示位置:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-268

## 9.192 TextInput的visibility属性设置为Hidden或者None之后是否可获焦:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-269

## 9.193 使用Navigation导航时，NavDestination页如何获取路由参数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-270

## 9.194 如何实现跨文件样式复用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-271

## 9.195 如何实现跨文件组件复用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-272

## 9.196 如何在Navigation页面中实现侧滑事件拦截:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-273

## 9.197 如何完成挖孔屏的适配:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-274

## 9.198 如何实现窗口、页面和组件的一键置灰功能（灰色模式）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-275

## 9.199 如何实现List内拖拽交换子组件位置:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-276

## 9.200 如何将ListItem的swipeAction滑动效果恢复到初始状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-277

## 9.201 如何实现List/Swiper/Grid嵌套滚动的下拉刷新和上拉加载更多:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-278

## 9.202 如何在代码中触发应用后台运行:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-279

## 9.203 禁用Tab组件边缘滑动回弹效果的方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-280

## 9.204 自定义键盘和系统键盘如何切换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-281

## 9.205 struct和class的区别是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-284

## 9.206 跳转页面如何实现页面级别的透明效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-285

## 9.207 如何实现二维数组的懒加载:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-292

## 9.208 如何实现带图片的二维码效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-294

## 9.209 Scroll中嵌套List，可否设置事件响应顺序，让List不响应滚动事件，让外层的Scroll滚动整个布局:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-295

## 9.210 如何清除输入框焦点:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-296

## 9.211 如何进行截屏并获取截屏内容:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-297

## 9.212 如何在Page中获取WindowStage实例:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-298

## 9.213 如何获取组件渲染完成时间:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-302

## 9.214 Toggle组件设置拖动的同时如何屏蔽其本身的点击手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-303

## 9.215 如何通过路由的方式打开半屏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-305

## 9.216 如何识别双击手势时忽视单击手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-306

## 9.217 如何查看触摸热区范围:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-307

## 9.218 如何将内容直接复制到剪贴板:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-308

## 9.219 在长按拖拽排序的场景下，如何实现自定义长按拖拽onItemDragStart的开始触发时长:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-310

## 9.220 绑定类型的组件和ForEach的正确连用方式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-311

## 9.221 如何使用canvas绘制圆角矩形:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-313

## 9.222 如何设置镜像语言的左右间距:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-314

## 9.223 如何实现Scroll、List单边回弹效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-316

## 9.224 如何合并两个列表并支持懒加载:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-317

## 9.225 RelativeContainer组件height设置为auto，子组件以容器作为锚点，为什么auto不生效:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-318

## 9.226 如何设置禁止分屏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-319

## 9.227 如何解决滚动类容器的滚动事件和手势之间的冲突:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-320

## 9.228 如何使用ListItemGroup和LazyForEach结合并实现组件复用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-321

## 9.229 如何在Text组件关闭bindSelection自定义菜单时，取消文本的选中状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-323

## 9.230 WaterFlow、Grid、List这些容器的使用区别是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-324

## 9.231 如何控制CustomDialog显示层级:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-325

## 9.232 如何处理ForEach第三个参数键值生成耗时久导致的卡顿问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-327

## 9.233 Tab组件页面切换时，如何不显示中间过渡的tab页:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-328

## 9.234 LocalStorage频繁读写复杂对象时性能变差的原因是什么？:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-329

## 9.235 如何给不同输入框绑定不同的自定义键盘:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-331

## 9.236 一个自定义组件内某一时机批量刷新多个@State修饰的状态变量，是否会影响性能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-333

## 9.237 List控件加载的数据如何判断是否超过一屏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-334

## 9.238 常用可以设置'auto'的属性的组件及其含义的介绍:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-335

## 9.239 双层嵌套list，如何使用LazyForEach起作用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-337

## 9.240 Marquee组件的文字滚动，第一次滚动出现大量空白，如何避免空白出现:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-338

## 9.241 如何解决Web页上下滑动时会误触发tab页翻页手势及tab页切换时Web组件还可以上下滚动问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-339

## 9.242 如何判断当前设备是手机还是折叠屏手机:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-340

## 9.243 如何在使用子窗口时保持键盘获焦:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-341

## 9.244 如何实现直播评论场景中顶部渐变遮罩效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-343

## 9.245 如何在Tabs的tabBar中添加其他组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-344

## 9.246 使用Canvas如何实现部分区域镂空的效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-346

## 9.247 如何解决Text组件文本为中文、数字、英文混合时显示省略号截断异常的问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-347

## 9.248 如何实现List的折叠动画效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-348

## 9.249 如何修改bindPopup绑定的弹窗圆角大小和箭头颜色:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-349

## 9.250 bindPopup适配Web组件长按菜单功能，设置offset控制弹窗的偏移:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-350

## 9.251 如何避免Badge在数量显示切换时的Image闪烁问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-352

## 9.252 Toggle组件响应点击后会立即渲染并回调，如何实现点击后延迟改变状态:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-353

## 9.253 如何在系统深色模式下使用getColorSync(resource)返回深色颜色值:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-354

## 9.254 汉字转拼音如何去掉声调符号:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-355

## 9.255 如何更改TextInput密码输入模式下passwordIcon的大小、颜色、位置:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-356

## 9.256 状态栏与页面内容发生重叠，如何解决:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-357

## 9.257 如何实现状态栏背景颜色沉浸:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-358

## 9.258 在深色模式切换下如何适配状态栏颜色:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-359

## 9.259 进入全屏模式后隐藏状态栏，退出全屏模式如何显示状态栏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-360

## 9.260 Button组件无法设置字体最大、最小值:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-361

## 9.261 如何实现折叠屏折叠态不适配旋转，展示态适配旋转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-362

## 9.262 如何实现组件动态上下树:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-364

## 9.263 Image组件长按和拖拽的系统手势和自定义手势冲突:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-365

## 9.264 如何实现通过侧滑手势关闭打开的悬浮框:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-366

## 9.265 如何获取ArkTS状态管理框架代理前的原始对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-367

## 9.266 在display.on('change')监听回调中，无法使用Window实例获取更新后的窗口大小:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-368

## 9.267 如何同时获取屏幕方向orientation和系统规避区avoidAreaChange信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-369

## 9.268 如何实现沉浸式页面（包括沉浸式状态栏、沉浸式导航条）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-370

## 9.269 如何理解AspectRatio对布局的影响:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-371

## 9.270 如何设置customspan不同位置的点击事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-372

## 9.271 窗口Orientation枚举值8~10或12和枚举值13~16的区别:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-373

## 9.272 如何实现应用的屏幕自动旋转:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-374

## 9.273 自定义构建函数Builder与自定义组件component的使用区别以及限制是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-375

## 9.274 如何实现ArkUI组件字符串变量拼接:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-376

## 9.275 如何打开键鼠穿越功能开关:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-377

## 9.276 是否支持对页面等ArkUI组件相关元素进行插桩:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-378

## 9.277 如何模拟点击事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-379

## 9.278 应用冷启动时，trace中dlopen：libace_compatible.z.so耗时长的可能原因:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-380

## 9.279 onAreaChange回调事件和windowStatusChange回调事件两者有什么关系，时序是怎样的:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-381

## 9.280 给组件设置responseRegion属性向上下扩展热区，为什么上半部分可以响应点击，下半部分不能响应点击:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-382

## 9.281 Surface模式下的XComponent组件在设置renderFit后如果出现显示异常，该如何调整以获得正确的显示效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-383

## 9.282 如何解决组件消失动画偏移闪烁:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-384

## 9.283 如何实现字体渐变效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-385

## 9.284 如何禁用Refresh组件的下拉刷新:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-386

## 9.285 使用Text嵌套Span或者使用属性字符串渲染文本，部分文本颜色显示异常:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-387

## 9.286 使用Router跳转导致闪退，可能是什么原因，如何排查:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-388

## 9.287 Router路由跳转页面失败，可能有哪些原因:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-389

## 9.288 Navigation跳转页面白屏，可能原因是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-390

## 9.289 如何实现弹窗动画和遮罩动画分开设置:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-391

## 9.290 如何实现加载svga动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-392

## 9.291 Swiper如何自定义导航点高度位置:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-393

## 9.292 当一个组件同时绑定了点击事件（onClick）和并行手势（.parallelGesture），为什么当操作为长按时，两个手势都会响应:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-457

## 9.293 如何实现在图片进行绘制马赛克的效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-396

## 9.294 如何实现swiper根据内容高度随滑动距离变动的效果:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-397

## 9.295 Navigation自定义标题栏不生效，可能是什么原因:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-399

## 9.296 如何监听Navigation页面的生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-401

## 9.297 Navigation页面级弹窗，下层页面如何监听是否被Dialog覆盖:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-402

## 9.298 Navigation管理的页面生命周期是什么，需要什么回调监听页面生命周期:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-403

## 9.299 Navigation组件中，NavDestination页面是否可以缓存，下次入栈可以复用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-404

## 9.300 Navigation路由，如何快速实现RouterMap注册转为wrapBuilder注册:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-405

## 9.301 Navigation组件，打开页面耗时，是否有优化建议:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-406

## 9.302 Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-407

## 9.303 Navigation组件，调用queryNavDestinationInfo返回undefined，如何正确调用这个接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-408

## 9.304 Navigation如何设置默认页:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-409

## 9.305 Navigation组件，如何监听页面切换后系统动画的结束时机:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-410

## 9.306 Navigation组件，内部页面是否可以预加载:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-411

## 9.307 Navigation如何取消单双栏切换动效:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-412

## 9.308 在Tabs组件中，哪些方式可以实现内容页的切换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-413

## 9.309 如何监听Navigation页面栈变化:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-414

## 9.310 Navigation通过pushPathByName跳转页面为什么显示空白:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-415

## 9.311 Watch开发，ArcSwiper实现右滑退出:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-416

## 9.312 NavDestinationMode.DIALOG模式下，如何针对弹窗内容或者背景遮罩做转场动效:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-417

## 9.313 使用Navigation，页面从A->B->C->D，D直接调用popToName到A，不会触发B、C的onPop是什么原因:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-418

## 9.314 Navigation页面接收参数一般推荐在什么生命周期接收:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-419

## 9.315 Navigation页面参数如何管理？如：传递参数、参数返回、参数获取:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-420

## 9.316 Navigation如何在自定义组件之间传递NavPathStack实例:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-422

## 9.317 Navigation跨模块跳转报错:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-423

## 9.318 Tabs如何实现TabBar左对齐:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-427

## 9.319 如何区分onPageHide的两种场景：应用退到后台，以及有新的页面打开:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-429

## 9.320 NavPathStack清空页面栈或者按返回键，为什么显示的是导航栏，如何实现退出Navigation所在的页面:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-430

## 9.321 Tabs是否支持懒加载:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-431

## 9.322 Navigation组件，使用customNavContentTransition自定义转场动效，如何实现动效逻辑跟组件解耦:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-432

## 9.323 手表设备，熄屏2分钟才能收到onHidden回调:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-433

## 9.324 Swiper怎么实现Item部分可见的效果？有没有示例展示:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-436

## 9.325 有没有Navigation实现跨模块跳转的demo工程，包括系统路由表以及自定义路由表的实践:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-437

## 9.326 Navigation组件NavPathStack removeByName默认会有底部滑入滑出的动画，如何关闭动画:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-438

## 9.327 ArcSwiper如何适配表冠:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-439

## 9.328 如何给Swiper组件添加节流，控制Swiper的切换频率:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-440

## 9.329 Tabs如何设置页面margin，使得边距空白跟随页面滑动:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-442

## 9.330 Scroll内容区的高度小于组件高度，是否无法滑动:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-443

## 9.331 Scroll嵌套外层滚动容器滚动，如何设置nestedScroll，实现Scroll组件先滚动，滚动边缘后触发外层滚动容器滚动:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-444

## 9.332 如何让弹窗显示层级不在下一个页面上:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-445

## 9.333 pc上，bindPopup设置了showInSubWindow:true时，气泡无法再弹出菜单:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-446

## 9.334 组件A通过bindContextMenu配置了长按菜单，点击菜单外区域，组件A响应了点击事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-447

## 9.335 如何针对UI组件属性做API版本兼容性判断:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-449

## 9.336 TextInput、TextArea等组件如何禁止提示拍摄输入:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-450

## 9.337 Tabs组件，自定义tabBar切换动画有延迟，Tabs页面切换完才触发tabBar切换，如何修改:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-451

## 9.338 Tabs组件，TabContent页面加载耗时，预加载未生效，怎么解决:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-452

## 9.339 全屏模态转场和半模态转场中是否可以实现避让软键盘:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-453

## 9.340 如何监听Tabs里面TabContent页面显示:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-454

## 9.341 如何控制Tabs内容页单向滑动切换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-455

## 9.342 页面存在透明的部分，使用组件截图保存为jpg图片，为什么变成了黑色:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-456

## 9.343 FrameNode的性能为什么不如声明式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-458

## 9.344 FrameNode的isAttached接口是否可以判断FrameNode节点出现在屏幕上:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-459

## 9.345 AppStorage里面存储数据，如何保证不会有内存泄漏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-461

## 9.346 AppStorage存了对象之后里面的值取不出来，什么原因:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-462

## 9.347 customDialog里面页面跳转后，页面显示在弹窗下面，怎么调整:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-463

## 9.348 半模态打开的页面被半模态覆盖了，怎么解决:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-464

## 9.349 Navigation组件，页面切换时，两个页面的生命周期时序关系是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-465

## 9.350 Swiper左滑为什么会显示空白:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-467

## 9.351 如何实现Tabs切换页签，强制重新刷新页面数据:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-468

## 9.352 Tabs组件，使用tab键循环走焦，会在最后一个页面和最后一个页签之间循环，怎么解决:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-469

## 9.353 如何去掉Tabs组件自定义tabBar的自带无障碍朗读:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-470

## 9.354 在子容器的onTouch中调用stopPropagation，为什么无法阻止外层容器的onClick事件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-471

## 9.355 Tabs如何禁止点击切换，以及禁止滑动内容页切换TabContent:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-472

## 9.356 Tabs如何实现预加载特定的TabContent页:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-473

## 9.357 Tabs导航页签栏如何根据Tabbar数均匀设置宽度:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-474

## 9.358 如何实现Tabs高度自适应内容:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-475

## 9.359 aboutToReuse使用入参params刷新UI崩溃:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-476

## 9.360 组件内转场(transition)新增内容动画生效，但删除内容动画不生效的可能原因是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-477

## 9.361 Tabs组件子组件包含if节点，if条件变更后, tabBar页签联动异常，有没有解决方案:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-478

## 9.362 Navigation页面底部空白是什么，如何取消:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-479

## 9.363 如何实现护眼模式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-480

## 9.364 组件截图（ComponentSnapshot）返回错误码100001，可能原因为截图尺寸过大，文档说明其与具体硬件限制有关，如何查看具体限制是多少:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-481

## 9.365 Text组件设置opacity后，文字颜色在整体透明度基础上叠加了一个透明，应该如何处理:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-482

## 9.366 设置了动态的visibility属性，切换组件的显示隐藏，使用requestFocus让组件获取焦点报错150003：the component is not on tree or does not exist.:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-483

## 9.367 如何实现当长按触发成功后，移出组件取消当前长按手势:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-484

## 9.368 如何判断组件遮挡情况，并主动隐藏被遮挡的组件:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-485

## 9.369 自定义组件内定义方法报错，出现异常的原因:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-486

## 9.370 如何解决应用键盘出现遮挡，输入框被拦截一半:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ffaqs-arkui-489

## 9.371 鸿蒙电脑拖拽悬浮窗至扩展显示器时，如何保证悬浮窗布局不出现异常:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-487

## 9.372 自定义键盘如何设置可与输入框贴边:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-490

## 9.373 如何实现三键导航的监听与避让:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-491

## 9.374 如何设置仅文字输入的键盘，即屏蔽键盘中AI功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-492
