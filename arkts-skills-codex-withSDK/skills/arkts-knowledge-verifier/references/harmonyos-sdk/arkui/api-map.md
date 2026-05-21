# ArkUI API 映射

## 使用方式

当回答已经确定主主题，但需要补充 ArkUI API 参考入口时，读取本文件。

## API 总入口

- ArkUI（方舟UI框架）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkui-api

## 主题到 API 的映射规则

- 基础语法与组件定义：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uicontext
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-node
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-componentutils
- 状态管理：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/state-management-and-rendering-control
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement
- 渲染控制与列表：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/state-management-and-rendering-control
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-foreach
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-repeat
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow
- 导航与页面路由：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/navigation-and-switching
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-arkui-advanced-multinavigation
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-router
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-router
- 样式、布局、动画与主题：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/layout-property
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-layout-constraints
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-flex-layout
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatable-extend
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/animation
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/themes
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme

## 直接映射

- `@Styles`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style
- `@Extend`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style
- `stateStyles`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style
- `@AnimatableExtend`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-animatable-extend
- `ContentSlot`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-contentslot
- `@Env`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-env-system-property
- `ArcList`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arclist
- `GridItem`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-griditem
- `ForEach`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-foreach
- `LazyForEach`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-lazyforeach
- `Repeat`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-rendering-control-repeat
- `@ohos.router`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-router
- `Navigation`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation
- `NavDestination`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navdestination
- `Tabs`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs
- `List` / `Grid` / `WaterFlow`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-grid
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-waterflow
- 动画：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/animation
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-animator
- 主题：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/themes
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-theme
- 状态管理：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-state-management
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statemanagement

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南
- 当开发指南已经能回答“推荐怎么做”时，API 参考只作为补充
