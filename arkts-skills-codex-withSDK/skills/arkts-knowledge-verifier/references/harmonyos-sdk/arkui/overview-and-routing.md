# ArkUI 总览与主题路由

## 使用方式

- 当用户问题主题不明确时，优先按下面的主题索引定位主主题，再读取对应 reference。

## 主题索引

### 基础语法与组件定义

- ArkUI（方舟UI框架）开发指南：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui
- ArkUI简介：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui-overview
- UI开发（ArkTS声明式开发范式）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-development
- UI开发（ArkTS声明式开发范式）概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-development-overview
- 学习UI范式基本语法：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-paradigm-basic-syntax
- 基本语法概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-basic-syntax-overview
- UI装饰器总览：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-decorator-overview
- 声明式UI描述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-declarative-ui-description
- 自定义组件：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components
- 创建自定义组件：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components
- 自定义组件生命周期：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-custom-components-lifecycle
- 自定义组件的自定义布局：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-page-custom-components-layout
- 自定义组件成员属性访问限定符使用限制：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-access-restrictions
- 自定义组件复用：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-component-reusable
- 自定义组件冻结：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-component-freeze
- 自定义组件冻结功能（V1）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-freeze
- 自定义组件冻结功能（V2）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-freezev2
- 组件扩展：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend-components
- 组件扩展概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend-components-overview
- `@Builder`装饰器：自定义构建函数：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder
- `@LocalBuilder`装饰器：维持组件关系：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localbuilder
- `@BuilderParam`装饰器：引用@Builder函数：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builderparam
- `wrapBuilder`：封装全局@Builder：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-wrapbuilder
- `mutableBuilder`：实现全局@Builder动态更新：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mutablebuilder
- `@Styles`装饰器：定义组件重用样式：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style
- `@Extend`装饰器：定义扩展组件样式：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend
- `stateStyles`：多态样式：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-statestyles
- `@AnimatableExtend`装饰器：定义可动画属性：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animatable-extend
- `@Require`装饰器：校验构造传参：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-require

### 状态管理

- 学习UI范式状态管理：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management
- 状态管理概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview
- 状态管理术语：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-glossary
- 状态管理原理介绍：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-introduce
- 状态管理V1和V2更新机制差异：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-update-difference
- MVVM模式（V1）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mvvm
- MVVM模式（V2）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mvvm-v2
- 状态管理（V1）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v1
- 状态管理（V2）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v2
- 辅助接口：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-uiutils
- 语法糖：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-syntactic-sugar
- 状态管理V1-V2迁移指导：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-guide
- 状态管理常见问题：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq

### 渲染控制与列表

- 学习UI范式渲染控制：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control
- 渲染控制概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-overview
- if/else：条件渲染：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-ifelse
- ForEach：循环渲染：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-foreach
- LazyForEach：数据懒加载：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach
- Repeat：可复用的循环渲染：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-rendering-control-repeat
- LazyForEach迁移Repeat指南：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-lazyforeach-repeat-migration-guide
- ContentSlot：混合开发：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-contentslot
- 列表与网格：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-list-and-grid
- 列表与网格概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-list-grid-development-overview
- 创建列表 (List)：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-list
- 弧形列表 (ArcList)（圆形屏幕推荐使用）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-arclist
- 创建网格 (Grid/GridItem)：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-grid
- 创建瀑布流（WaterFlow）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-create-waterflow

### 导航与页面路由

- 设置组件导航和页面路由：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-set-navigation-routing
- 组件导航和页面路由概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-introduction
- 组件导航(Navigation) (推荐)：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-navigation
- 页面路由 (@ohos.router)(不推荐)：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing
- Router切换Navigation：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-router-to-navigation

### 样式、布局、动画与主题

- 学习响应式环境变量：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-property
- @Env：环境变量：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-env-system-property
- 组件布局：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development
- 布局概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-overview
- 构建布局：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-build-layout
- 开发应用沉浸式效果：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects
- 使用动画：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-animation
- 动画概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation
- 属性动画：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-attribute
- 转场动画：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-transition
- 粒子动画：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-particle-animation
- 组件动画：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-component-animation
- 动画曲线：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-curve
- 动画衔接：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-smoothing
- 动画效果：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-effects
- 帧动画（ohos.animator）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animator
- 主题设置：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-theme
- 应用深浅色适配：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-dark-light-color-adaptation
- 设置应用内主题换肤：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning

### 其他 UI 能力

- 使用文本：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-text
- 媒体展示：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-media-display
- 表单选择：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-form-selection
- 添加组件：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-add-component
- 使用弹窗：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-dialog
- 几何图形绘制：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-draw-graphics
- 添加交互响应：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-overview
- 使用自定义能力：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-capabilities
- UI国际化：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-internationalization
- 无障碍与适老化：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-support-accessibility-friendliness
- UI系统场景化能力：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-system-scenarization-capability
- UI开发（基于NDK构建UI）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-ndk

## 路由提示

- 问声明式 UI、组件定义、Builder、样式复用时，转到 `component-composition.md`
- 问 `@State`、`@Link`、`@Local`、`@Param`、状态不刷新、V1/V2 时，转到 `state-management.md`
- 问 `ForEach`、`LazyForEach`、`Repeat`、条件渲染、页面跳转、`Navigation` 时，转到 `rendering-navigation.md`
- 问样式、布局、动画、主题时，转到 `styling-animation.md`
- 问最佳实践、常见错误、FAQ、排障时，转到 `best-practices-and-faq.md`
- 问 API 条目、参数、装饰器、方法对照时，转到 `api-map.md`
