# 状态管理

## 总览

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

## V1 状态管理

- 状态管理（V1）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v1

### 管理组件拥有的状态

- `@State`装饰器：组件内状态：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state
- `@Prop`装饰器：父子单向同步：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-prop
- `@Link`装饰器：父子双向同步：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-link
- `@Provide`装饰器和`@Consume`装饰器：与后代组件双向同步：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-provide-and-consume
- `@Observed`装饰器和`@ObjectLink`装饰器：嵌套类对象属性变化：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink
- `@Watch`装饰器：状态变量更改通知：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-watch

### 管理数据对象的状态

- `@Track`装饰器：class对象属性级更新：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-track

### 管理应用拥有的状态

- 管理应用拥有的状态概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-application-state-management-overview
- `LocalStorage`：页面级UI状态存储：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage
- `AppStorage`：应用全局的UI状态存储：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-appstorage
- `PersistentStorage`：持久化存储UI状态：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-persiststorage
- `Environment`：设备环境查询：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-environment

## V2 状态管理

- 状态管理（V2）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v2

### 管理组件拥有的状态

- `@Local`装饰器：组件内部状态：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-local
- `@Param`：组件外部输入：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-param
- `@Once`：初始化同步一次：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-once
- `@Event`装饰器：规范组件输出：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-event
- `@Provider`装饰器和`@Consumer`装饰器：跨组件层级双向同步：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-provider-and-consumer

### 管理数据对象的状态

- `@ObservedV2`装饰器和`@Trace`装饰器：类属性变化观测：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace
- `@Monitor`装饰器：状态变量修改监听：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor
- `@Computed`装饰器：计算属性：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-computed
- `@Type`装饰器：标记类属性的类型：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-type

### 管理应用拥有的状态

- `AppStorageV2`：应用全局UI状态存储：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-appstoragev2
- `PersistenceV2`：持久化存储UI状态：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-persistencev2

## 辅助接口

- `getTarget`接口：获取状态管理框架代理前的原始对象：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-gettarget
- `makeObserved`接口：将非观察数据变为可观察数据：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-makeobserved
- `addMonitor`/`clearMonitor`接口：动态添加/取消监听：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-addmonitor-clearmonitor
- `applySync`/`flushUpdates`/`flushUIUpdates`接口：同步刷新：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates

## 语法糖

- `$$`语法：系统组件双向同步：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-two-way-sync
- `!!`语法：双向绑定：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding

## 迁移、混用与 FAQ

- 状态管理V1-V2迁移指导：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-guide
- V1-V2迁移概述：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration
- 状态管理V1向V2迁移场景：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-v1-v2-migration-guide
- 组件内状态变量迁移：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-component
- 数据对象状态变量迁移：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-class
- 应用内状态变量迁移：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-application
- 组件复用迁移：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-reusable
- 循环渲染迁移：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-rendering-control-repeat
- 内置对象的迁移：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-object
- AnimateTo使用迁移：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-animateto
- 状态管理V1和V2混用场景：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/v1v2-mixing
- 状态管理V1和V2混用指导（API version 19前）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage-before-api-version
- 状态管理V1和V2混用指导（API version 19及之后）：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage
- 状态管理常见问题：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq
- 组件内状态管理常见问题：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-inner-component
- 数据对象状态管理常见问题：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-inner-class
- 应用内状态管理和其他常见问题：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-application-and-others
- 状态变量改变不触发组件刷新问题常用定位方法：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/troubleshooting-state-manage
