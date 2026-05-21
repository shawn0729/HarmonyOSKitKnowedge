# Performance Analysis Kit 总览与主题路由

## 使用方式

- 当用户问题主题不明确时，先根据下面的主题索引定位主主题，再读取对应 reference。
- 默认先看开发指南；需要接口细节时再看 API；需要避坑和排障时再补最佳实践或 FAQ。

## 主题索引

### Performance Analysis Kit

#### 主题入口

- 开发指南入口
  - 1 Performance Analysis Kit开发指南：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-analysis-kit
    - 关键词：Performance Analysis Kit
  - 1.1 Performance Analysis Kit简介：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-analysis-kit-overview
    - 关键词：Performance Analysis Kit

### 故障检测

#### 主题入口

- 开发指南入口
  - 1.2 故障检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fault-analysis
    - 关键词：故障检测
  - 1.2.1 简介：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fault-detection-overview
  - 1.2.2 崩溃检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crash-detection
    - 关键词：崩溃检测
  - 1.2.3 AddrSanitizer（地址越界）检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/address-sanitizer-guidelines
    - 关键词：AddrSanitizer（地址越界）检测
  - 1.2.4 AppFreeze（应用冻屏）检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines
    - 关键词：AppFreeze（应用冻屏）检测
  - 1.2.5 Resource Leak（资源泄漏）检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-leak-guidelines
    - 关键词：Resource Leak（资源泄漏）检测
  - 1.2.6 任务超时检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/apptask-timeout-guidelines
    - 关键词：任务超时检测
  - 1.2.7 App Killed（应用终止）检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appkilled-guidelines
    - 关键词：App Killed（应用终止）检测

### 崩溃检测

#### 主题入口

- 开发指南入口
  - 1.2.2.1 JS Crash（进程崩溃）检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/jscrash-guidelines
    - 关键词：JS Crash（进程崩溃）检测
  - 1.2.2.2 Cpp Crash（进程崩溃）检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cppcrash-guidelines
    - 关键词：Cpp Crash（进程崩溃）检测

### 功耗检测

#### 主题入口

- 开发指南入口
  - 1.3 功耗检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/power-detection
    - 关键词：功耗检测

### 性能检测

#### 主题入口

- 开发指南入口
  - 1.4 性能检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/perf-detection
    - 关键词：性能检测

### 日志打印

#### 主题入口

- 开发指南入口
  - 1.5 日志打印：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog-dev
    - 关键词：日志打印
  - 1.5.1 使用HiLog打印日志（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog-guidelines-arkts
    - 关键词：HiLog打印日志（ArkTS）
  - 1.5.2 使用HiLog打印日志（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog-guidelines-ndk
    - 关键词：HiLog打印日志（C / C++）

### 事件订阅

#### 主题入口

- 开发指南入口
  - 1.6 事件订阅：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent
    - 关键词：事件订阅
  - 1.6.1 HiAppEvent介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-intro
    - 关键词：HiAppEvent介绍
  - 1.6.2 使用HiAppEvent订阅事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/event-subscription
    - 关键词：HiAppEvent订阅事件

### 使用HiAppEvent订阅事件

#### 主题入口

- 开发指南入口
  - 1.6.2.1 事件订阅简介：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/event-subscription-overview
    - 关键词：事件订阅
  - 1.6.2.2 事件订阅（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-events-arkts
    - 关键词：事件订阅（ArkTS）
  - 1.6.2.3 事件订阅（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-events-ndk
    - 关键词：事件订阅（C / C++）
  - 1.6.2.4 系统事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-events
    - 关键词：系统事件

### 系统事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.1 崩溃事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crash-events
    - 关键词：崩溃事件
  - 1.6.2.4.2 应用冻屏事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/freeze-events
    - 关键词：应用冻屏事件
  - 1.6.2.4.3 资源泄漏事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resource-leak-events
    - 关键词：资源泄漏事件
  - 1.6.2.4.4 地址越界事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/address-sanitizer-events
    - 关键词：地址越界事件
  - 1.6.2.4.5 主线程超时事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/main-thread-jank-events
    - 关键词：主线程超时事件
  - 1.6.2.4.6 任务执行超时事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-hicollie-events
    - 关键词：任务执行超时事件
  - 1.6.2.4.7 应用终止事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-killed-events
    - 关键词：应用终止事件
  - 1.6.2.4.8 启动耗时事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/startup-duration-events
    - 关键词：耗时事件
  - 1.6.2.4.9 滑动丢帧事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/frame-drops-event-during-scrolling
    - 关键词：滑动丢帧事件
  - 1.6.2.4.10 CPU高负载事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/high-cpu-load-event
    - 关键词：CPU高负载事件
  - 1.6.2.4.11 24h功耗器件分解统计事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/24-hour-battery-usage-event
    - 关键词：24h功耗器件分解统计事件
  - 1.6.2.4.12 音频卡顿事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-audio-jank-event
    - 关键词：音频卡顿事件

### 崩溃事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.1.1 崩溃事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events
    - 关键词：崩溃事件介绍
  - 1.6.2.4.1.2 订阅崩溃事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events-arkts
    - 关键词：订阅崩溃事件（ArkTS）
  - 1.6.2.4.1.3 订阅崩溃事件（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events-ndk
    - 关键词：订阅崩溃事件（C / C++）

### 应用冻屏事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.2.1 应用冻屏事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events
    - 关键词：应用冻屏事件介绍
  - 1.6.2.4.2.2 订阅应用冻屏事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-arkts
    - 关键词：订阅应用冻屏事件（ArkTS）
  - 1.6.2.4.2.3 订阅应用冻屏事件（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-ndk
    - 关键词：订阅应用冻屏事件（C / C++）

### 资源泄漏事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.3.1 资源泄漏事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events
    - 关键词：资源泄漏事件介绍
  - 1.6.2.4.3.2 订阅资源泄漏事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-arkts
    - 关键词：订阅资源泄漏事件（ArkTS）
  - 1.6.2.4.3.3 订阅资源泄漏事件（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-resourceleak-events-ndk
    - 关键词：订阅资源泄漏事件（C / C++）

### 地址越界事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.4.1 地址越界事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events
    - 关键词：地址越界事件介绍
  - 1.6.2.4.4.2 订阅地址越界事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events-arkts
    - 关键词：订阅地址越界事件（ArkTS）
  - 1.6.2.4.4.3 订阅地址越界事件（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events-ndk
    - 关键词：订阅地址越界事件（C / C++）

### 主线程超时事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.5.1 主线程超时事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events
    - 关键词：主线程超时事件介绍
  - 1.6.2.4.5.2 订阅主线程超时事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events-arkts
    - 关键词：订阅主线程超时事件（ArkTS）
  - 1.6.2.4.5.3 订阅主线程超时事件（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events-ndk
    - 关键词：订阅主线程超时事件（C / C++）

### 任务执行超时事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.6.1 任务执行超时事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-apphicollie-events
    - 关键词：任务执行超时事件介绍
  - 1.6.2.4.6.2 订阅任务执行超时事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-apphicollie-events-arkts
    - 关键词：订阅任务执行超时事件（ArkTS）
  - 1.6.2.4.6.3 订阅任务执行超时事件（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-apphicollie-events-ndk
    - 关键词：订阅任务执行超时事件（C / C++）

### 应用终止事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.7.1 应用终止事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-killed-events
    - 关键词：应用终止事件介绍
  - 1.6.2.4.7.2 订阅应用终止事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-killed-events-arkts
    - 关键词：订阅应用终止事件（ArkTS）
  - 1.6.2.4.7.3 订阅应用终止事件（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-killed-events-ndk
    - 关键词：订阅应用终止事件（C / C++）

### 启动耗时事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.8.1 启动耗时事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-launch-event
    - 关键词：耗时事件介绍
  - 1.6.2.4.8.2 订阅启动耗时事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-launch-arkts
    - 关键词：订阅启动耗时事件（ArkTS）

### 滑动丢帧事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.9.1 滑动丢帧事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-scroll-jank-event
    - 关键词：滑动丢帧事件介绍
  - 1.6.2.4.9.2 订阅滑动丢帧事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-scroll-jank-arkts
    - 关键词：订阅滑动丢帧事件（ArkTS）

### CPU高负载事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.10.1 CPU高负载事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-cpu-usage-high-event
    - 关键词：CPU高负载事件介绍
  - 1.6.2.4.10.2 订阅CPU高负载事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-cpu-usage-high-arkts
    - 关键词：订阅CPU高负载事件（ArkTS）

### 24h功耗器件分解统计事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.11.1 24h功耗器件分解统计事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-battery-usage-event
    - 关键词：24h功耗器件分解统计事件介绍
  - 1.6.2.4.11.2 订阅24h功耗器件分解统计事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-battery-usage-arkts
    - 关键词：订阅24h功耗器件分解统计事件（ArkTS）

### 音频卡顿事件

#### 主题入口

- 开发指南入口
  - 1.6.2.4.12.1 音频卡顿事件介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-audio-jank-event
    - 关键词：音频卡顿事件介绍
  - 1.6.2.4.12.2 订阅音频卡顿事件（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-audio-jank-event-arkts
    - 关键词：订阅音频卡顿事件（ArkTS）
  - 1.6.2.4.12.3 订阅音频卡顿事件（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-audio-jank-event-c
    - 关键词：订阅音频卡顿事件（C / C++）

### 最佳实践与FAQ

#### 最佳实践

- 最佳实践入口
  - 3.1.1 性能概览：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-guide-reading
    - 关键词：性能概览
  - 3.1.2 性能体验设计：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-smooth-application-design
    - 关键词：性能体验设计
  - 3.1.3 性能检测：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-detection
    - 关键词：性能检测
  - 3.1.3.1 开发态性能检测：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-detection
    - 关键词：开发态性能检测
  - 3.1.3.2 运行态性能检测：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-runtime-detection
    - 关键词：运行态性能检测
  - 3.1.3.2.1 启动耗时类问题检测方法：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-startup-time-detection
    - 关键词：耗时类问题检测方法
  - 3.1.3.2.2 主线程超时类问题检测方法：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-mainthread-consumption-detection
    - 关键词：主线程超时类问题检测方法
  - 3.1.3.2.3 滑动丢帧类问题检测方法：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-sliding-frame-drop-detection
    - 关键词：滑动丢帧类问题检测方法
  - 3.1.4 性能分析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-optimization-tool-practice
    - 关键词：性能分析
  - 3.1.4.1 性能分析简介：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-optimization-overview
    - 关键词：性能分析
  - 3.1.4.2 点击响应时延分析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-click-response-optimization
    - 关键词：点击响应时延分析
  - 3.1.4.3 点击完成时延分析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-complete-delay-analysis
    - 关键词：点击完成时延分析
  - 3.1.4.4 帧率问题分析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-zhenlv
    - 关键词：帧率问题分析
  - 3.1.4.5 Web点击响应时延分析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-click-response-delay-analysis
    - 关键词：Web点击响应时延分析
  - 3.1.4.6 Web加载完成时延分析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-completion-delay-analysis
    - 关键词：Web加载完成时延分析
  - 3.1.4.7 跨线程序列化耗时问题分析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-threads-serialization-timeout-analysis
    - 关键词：跨线程序列化耗时问题分析
  - 3.1.4.8 分析内存占用问题：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-analyze-memory-problem
    - 关键词：分析内存占用问题
  - 3.1.4.8.1 内存基础知识：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-memory-basic-knowledge
    - 关键词：内存基础知识
  - 3.1.4.8.2 获取进程内存信息：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-retrieve-process-memory-info
    - 关键词：获取进程内存信息
  - 3.1.4.8.3 分析ArkTS/JS内存：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-js-memory-analysis
    - 关键词：分析ArkTS / JS内存
  - 3.1.4.8.4 分析native内存：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-native-memory-analysis
    - 关键词：分析native内存
  - 3.1.4.8.5 分析内核态内存：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-kernel-memory-analysis
    - 关键词：分析内核态内存
  - 3.1.4.9 分析任务执行超时问题：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-permission-timeout-analysis
    - 关键词：分析任务执行超时问题
  - 3.1.5 性能优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-optimization
    - 关键词：性能优化
  - 3.1.5.1 感知流畅优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-perceived-smoothness
    - 关键词：感知流畅优化
  - 3.1.5.2 渲染范围控制：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-control-rendering-range
    - 关键词：渲染范围控制
  - 3.1.5.3 布局节点减少：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reduce-layout-nodes
    - 关键词：布局节点减少
  - 3.1.5.4 组件绘制优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-pptimized-component-drawing
    - 关键词：组件绘制优化
  - 3.1.5.5 状态刷新控制：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-state-refresh
    - 关键词：状态刷新控制
  - 3.1.5.6 动画帧率优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-animation-frame
    - 关键词：动画帧率优化
  - 3.1.5.7 并发能力使用：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-concurrency-capability
    - 关键词：并发能力使用
  - 3.1.5.8 资源提前加载：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-preloading-resources
    - 关键词：资源提前加载
  - 3.1.5.9 运行效率提高：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-running-efficiency
    - 关键词：运行效率提高
  - 3.1.5.10 耗时操作减少：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reduce-time-consuming
    - 关键词：耗时操作减少
  - 3.1.5.11 操作延时触发：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-delayed-trigger-operation
    - 关键词：操作延时触发
  - 3.1.6 性能场景优化案例：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-scenario-performance-optimization
    - 关键词：性能场景优化案例
  - 3.1.6.1 界面渲染性能优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-developing-high-performance-ui
    - 关键词：界面渲染性能优化
  - 3.1.6.1.1 组件嵌套优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-nesting-optimization
    - 关键词：组件嵌套优化
  - 3.1.6.1.2 懒加载优化性能：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-lazyforeach-optimization
    - 关键词：懒加载优化性能
  - 3.1.6.1.3 UI组件性能优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ui-component-performance-optimization
    - 关键词：UI组件性能优化
  - 3.1.6.1.4 主线程耗时操作优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-time-optimization-of-the-main-thread
    - 关键词：主线程耗时操作优化
  - 3.1.6.1.5 高负载场景分帧渲染：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dispose-highly-loaded-component-render
    - 关键词：高负载场景分帧渲染
  - 3.1.6.1.6 长列表加载丢帧优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-best-practices-long-list
    - 关键词：长列表加载丢帧优化
  - 3.1.6.1.7 瀑布流加载丢帧优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-waterflow-performance-optimization
    - 关键词：瀑布流加载丢帧优化
  - 3.1.6.1.8 Grid组件加载丢帧优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve_grid_performance
    - 关键词：Grid组件加载丢帧优化
  - 3.1.6.1.9 Swiper组件加载丢帧优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-swiper_high_performance_development_guide
    - 关键词：Swiper组件加载丢帧优化
  - 3.1.6.2 应用启动与响应优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-startup-response-optimization
    - 关键词：应用启动与响应优化
  - 3.1.6.2.1 应用冷启动时延优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-cold-start-optimization
    - 关键词：应用冷启动时延优化
  - 3.1.6.2.2 应用时延优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-latency-optimization-cases
    - 关键词：应用时延优化
  - 3.1.6.3 资源与存储优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-resource-and-storage-optimization
    - 关键词：资源与存储优化
  - 3.1.6.3.1 应用包体积优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-decrease_pakage_size
    - 关键词：应用包体积优化
  - 3.1.6.3.2 应用内存占用优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-memory-optimization
    - 关键词：应用内存占用优化
  - 3.1.6.3.3 图片资源加载优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-texture-compression-improve-performance
    - 关键词：图片资源加载优化
  - 3.1.6.3.4 文件上传下载优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-file-upload-and-download-performance
    - 关键词：文件上传下载优化
  - 3.1.6.4 Web性能优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-performance-optimization
    - 关键词：Web性能优化
  - 3.1.6.4.1 Web加载性能优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-develop-optimization
    - 关键词：Web加载性能优化
  - 3.1.6.5 专项问题解决方案：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-solutions-to-special-issues
    - 关键词：专项问题解决方案
  - 3.1.6.5.1 应用闪屏解决方案：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-screen-flicker-solution
    - 关键词：应用闪屏解决方案
  - 3.1.6.5.2 Image白块解决方案：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-white-lump-solution
    - 关键词：Image白块解决方案
  - 3.1.6.6 对象序列化性能优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-object-serialization-performance
    - 关键词：对象序列化性能优化
  - 3.1.6.6.1 高性能JSON解析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-performance-json-parsing
    - 关键词：高性能JSON解析
  - 3.1.6.6.2 高性能Protobuf解析：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-performance-protobuf-parsing
    - 关键词：高性能Protobuf解析
  - 3.1.6.7 并行化性能优化：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-concurrent-optimization
    - 关键词：并行化性能优化

#### 常见问题

- FAQ入口
  - 1.6.3 HiAppEvent常见问题：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-faq
    - 关键词：HiAppEvent

#### 场景排障

- FAQ入口
  - 1.6.4 使用FaultLogExtensionAbility订阅事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fault-log-extension-app-events-arkts
    - 关键词：FaultLogExtensionAbility订阅事件
  - 1.7 性能跟踪：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter
    - 关键词：性能跟踪
  - 1.7.1 HiTraceMeter介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-intro
    - 关键词：HiTraceMeter介绍
  - 1.7.2 使用HiTraceMeter跟踪性能（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-arkts
    - 关键词：HiTraceMeter跟踪性能（ArkTS）
  - 1.7.3 使用HiTraceMeter跟踪性能（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-guidelines-ndk
    - 关键词：HiTraceMeter跟踪性能（C / C++）
  - 1.7.4 查看HiTraceMeter日志：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracemeter-view
    - 关键词：查看HiTraceMeter日志
  - 1.8 分布式调用链跟踪：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain
    - 关键词：分布式调用链跟踪
  - 1.8.1 HiTraceChain介绍：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain-intro
    - 关键词：HiTraceChain介绍
  - 1.8.2 使用HiTraceChain打点（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain-guidelines-arkts
    - 关键词：HiTraceChain打点（ArkTS）
  - 1.8.3 使用HiTraceChain打点（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hitracechain-guidelines-ndk
    - 关键词：HiTraceChain打点（C / C++）
  - 1.9 检测模式：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hichecker
    - 关键词：检测模式
  - 1.9.1 使用HiChecker检测问题（ArkTS）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hichecker-guidelines-arkts
    - 关键词：HiChecker检测问题（ArkTS）
  - 1.10 系统调试信息获取：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug
    - 关键词：系统调试信息获取
  - 1.10.1 HiDebug能力概述：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug-guidelines
    - 关键词：HiDebug能力
  - 1.10.2 HiDebug接口使用示例(ArkTS)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug-guidelines-arkts
    - 关键词：HiDebug接口使用示例 / ArkTS
  - 1.10.3 HiDebug接口使用示例(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidebug-guidelines-ndk
    - 关键词：HiDebug接口使用示例 / C++
  - 1.11 业务线程超时检测：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hicollie
    - 关键词：业务线程超时检测
  - 1.11.1 使用HiCollie检测业务线程卡死卡顿问题（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hicollie-guidelines-ndk
    - 关键词：HiCollie检测业务线程卡死卡顿问题（C / C++）
  - 1.11.2 使用HiCollie监控函数执行时间超长问题（C/C++）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hicollie-settimer-guidelines-ndk
    - 关键词：HiCollie监控函数执行时间超长问题（C / C++）
  - 1.12 错误管理及应用恢复：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/error-manager
    - 关键词：错误管理及应用恢复
  - 1.12.1 错误管理开发指导：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/errormanager-guidelines
    - 关键词：错误管理
  - 1.12.2 应用恢复开发指导：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/apprecovery-guidelines
    - 关键词：应用恢复
  - 1.13 Performance Analysis Kit术语：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-analysis-kit-terminology
    - 关键词：Performance Analysis Kit术语

### API与错误码

#### 核心 API

- API入口
  - 2 Performance Analysis Kit API参考：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-api
    - 关键词：Performance Analysis Kit
  - 2.1 ArkTS API：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-arkts
    - 关键词：ArkTS
  - 2.1.1 @ohos.hichecker (检测模式)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hichecker
    - 关键词：@ohos.hichecker / 检测模式
  - 2.1.2 @ohos.hidebug (Debug调试)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug
    - 关键词：@ohos.hidebug / Debug调试
  - 2.1.3 @ohos.hilog (HiLog日志打印)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog
    - 关键词：@ohos.hilog / HiLog日志打印
  - 2.1.4 @ohos.hiTraceChain (分布式跟踪)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracechain
    - 关键词：@ohos.hiTraceChain / 分布式跟踪
  - 2.1.5 @ohos.hiTraceMeter (性能打点)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracemeter
    - 关键词：@ohos.hiTraceMeter / 性能打点
  - 2.1.6 @ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability
    - 关键词：@ohos.hiviewdfx.FaultLogExtensionAbility / 故障延迟通知
  - 2.1.7 @ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext
    - 关键词：@ohos.hiviewdfx.FaultLogExtensionContext / 故障延迟通知上下文
  - 2.1.8 @ohos.hiviewdfx.hiAppEvent (应用事件打点)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent
    - 关键词：@ohos.hiviewdfx.hiAppEvent / 应用事件打点
  - 2.1.9 @ohos.hiviewdfx.jsLeakWatcher (js泄漏检测)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-jsleakwatcher
    - 关键词：@ohos.hiviewdfx.jsLeakWatcher / js泄漏检测
  - 2.1.10.1 @ohos.bytrace (性能打点)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bytrace
    - 关键词：@ohos.bytrace / 性能打点
  - 2.1.10.2 @ohos.hiAppEvent (应用打点)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiappevent
    - 关键词：@ohos.hiAppEvent / 应用打点
  - 2.1.10.3 @ohos.faultLogger (故障日志获取)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger
    - 关键词：@ohos.faultLogger / 故障日志获取
  - 2.2 C API：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-c
  - 2.2.1 模块：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-module
  - 2.2.1.1 HiAppEvent：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent
    - 关键词：HiAppEvent
  - 2.2.1.2 HiCollie：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie
    - 关键词：HiCollie
  - 2.2.1.3 HiDebug：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug
    - 关键词：HiDebug
  - 2.2.1.4 HiLog：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hilog
    - 关键词：HiLog
  - 2.2.1.5 HiTrace：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace
    - 关键词：HiTrace
  - 2.2.2 头文件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-headerfile
  - 2.2.2.1 hiappevent.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-h
    - 关键词：hiappevent.h
  - 2.2.2.2 hiappevent_cfg.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-cfg-h
    - 关键词：hiappevent_cfg.h
  - 2.2.2.3 hiappevent_event.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-event-h
    - 关键词：hiappevent_event.h
  - 2.2.2.4 hiappevent_param.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-param-h
    - 关键词：hiappevent_param.h
  - 2.2.2.5 hicollie.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-h
    - 关键词：hicollie.h
  - 2.2.2.6 hidebug.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-h
    - 关键词：hidebug.h
  - 2.2.2.7 hidebug_type.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h
    - 关键词：hidebug_type.h
  - 2.2.2.8 log.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-log-h
    - 关键词：log.h
  - 2.2.2.9 trace.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trace-h
    - 关键词：trace.h
  - 2.2.3 结构体：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-struct
  - 2.2.3.1 HiAppEvent_AppEventInfo：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventinfo
    - 关键词：HiAppEvent_AppEventInfo
  - 2.2.3.2 HiAppEvent_AppEventGroup：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-appeventgroup
    - 关键词：HiAppEvent_AppEventGroup
  - 2.2.3.3 ParamListNode*：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-paramlistnode8h
    - 关键词：ParamListNode*
  - 2.2.3.4 HiAppEvent_Watcher：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-watcher
    - 关键词：HiAppEvent_Watcher
  - 2.2.3.5 HiAppEvent_Processor：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-processor
    - 关键词：HiAppEvent_Processor
  - 2.2.3.6 HiAppEvent_Config：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-hiappevent-config
    - 关键词：HiAppEvent_Config
  - 2.2.3.7 HiCollie_DetectionParam：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-hicollie-detectionparam
    - 关键词：HiCollie_DetectionParam
  - 2.2.3.8 HiCollie_SetTimerParam：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-hicollie-settimerparam
    - 关键词：HiCollie_SetTimerParam
  - 2.2.3.9 HiDebug_ThreadCpuUsage：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-threadcpuusage
    - 关键词：HiDebug_ThreadCpuUsage
  - 2.2.3.10 HiDebug_SystemMemInfo：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-systemmeminfo
    - 关键词：HiDebug_SystemMemInfo
  - 2.2.3.11 HiDebug_NativeMemInfo：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativememinfo
    - 关键词：HiDebug_NativeMemInfo
  - 2.2.3.12 HiDebug_MemoryLimit：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-memorylimit
    - 关键词：HiDebug_MemoryLimit
  - 2.2.3.13 HiDebug_JsStackFrame：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-jsstackframe
    - 关键词：HiDebug_JsStackFrame
  - 2.2.3.14 HiDebug_NativeStackFrame：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-nativestackframe
    - 关键词：HiDebug_NativeStackFrame
  - 2.2.3.15 HiDebug_StackFrame：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-stackframe
    - 关键词：HiDebug_StackFrame
  - 2.2.3.16 HiDebug_MallocDispatch：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-mallocdispatch
    - 关键词：HiDebug_MallocDispatch
  - 2.2.3.17 HiDebug_Backtrace_Object__*：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-backtrace-object--8h
    - 关键词：HiDebug_Backtrace_Object__*
  - 2.2.3.18 HiDebug_GraphicsMemorySummary：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-graphicsmemorysummary
    - 关键词：HiDebug_GraphicsMemorySummary
  - 2.2.3.19 HiDebug_ProcessSamplerConfig：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-processsamplerconfig
    - 关键词：HiDebug_ProcessSamplerConfig
  - 2.2.3.20 HiTraceId：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace-hitraceid
    - 关键词：HiTraceId

#### 已停止维护接口

- API入口
  - 2.1.10 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-arkts-dep
    - 关键词：已停止维护的接口

#### 错误码

- API入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-errcode
    - 关键词：错误码
  - 2.3.1 Faultlogger 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-faultlogger
    - 关键词：Faultlogger 错误码
  - 2.3.2 应用事件打点错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiappevent
    - 关键词：应用事件打点错误码
  - 2.3.3 HiDebug错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug
    - 关键词：HiDebug错误码
  - 2.3.4 HiDebug CpuUsage错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-cpuusage
    - 关键词：HiDebug CpuUsage错误码
  - 2.3.5 HiDebug Trace错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-trace
    - 关键词：HiDebug Trace错误码
  - 2.3.6 HiCollie错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hicollie
    - 关键词：HiCollie错误码
  - 2.3.7 JsLeakWatcher错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-jsleakwatcher
    - 关键词：JsLeakWatcher错误码

## 路由提示

- 问 Performance Analysis Kit 相关问题时，转到 `performance-analysis-kit.md`
- 问 故障检测 相关问题时，转到 `topic-e0395af1.md`
- 问 崩溃检测 相关问题时，转到 `topic-96bf6c74.md`
- 问 功耗检测 相关问题时，转到 `topic-d3e62d8d.md`
- 问 性能检测 相关问题时，转到 `topic-28fcba52.md`
- 问 日志打印 相关问题时，转到 `topic-561a0ea5.md`
- 问 事件订阅 相关问题时，转到 `topic-57a166bb.md`
- 问 使用HiAppEvent订阅事件 相关问题时，转到 `hiappevent.md`
- 问 系统事件 相关问题时，转到 `topic-b8c5beb2.md`
- 问 崩溃事件 相关问题时，转到 `topic-e2624e7c.md`
- 问 应用冻屏事件 相关问题时，转到 `topic-aefcce16.md`
- 问 资源泄漏事件 相关问题时，转到 `topic-24309fdd.md`
- 问 地址越界事件 相关问题时，转到 `topic-3826cc42.md`
- 问 主线程超时事件 相关问题时，转到 `topic-43e327a8.md`
- 问 任务执行超时事件 相关问题时，转到 `topic-4d3f926b.md`
- 问 应用终止事件 相关问题时，转到 `topic-027bf0ae.md`
- 问 启动耗时事件 相关问题时，转到 `topic-2833de46.md`
- 问 滑动丢帧事件 相关问题时，转到 `topic-89720f42.md`
- 问 CPU高负载事件 相关问题时，转到 `cpu.md`
- 问 24h功耗器件分解统计事件 相关问题时，转到 `24h.md`
- 问 音频卡顿事件 相关问题时，转到 `topic-57bfd10a.md`
- 问 HiAppEvent、性能跟踪、HiTraceMeter介绍、HiTraceMeter跟踪性能（ArkTS）、HiTraceMeter跟踪性能（C 时，转到 `best-practices-and-faq.md`
- 问 Performance Analysis Kit、@ohos.hichecker、检测模式、@ohos.hidebug、Debug调试 时，转到 `api-and-error-codes.md`
