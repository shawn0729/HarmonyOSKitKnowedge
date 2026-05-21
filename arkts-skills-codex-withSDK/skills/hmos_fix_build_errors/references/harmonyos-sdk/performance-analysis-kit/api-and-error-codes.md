# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 Performance Analysis Kit API 参考入口时，读取本文件。

## API 总入口

- 2 Performance Analysis Kit API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-arkts
- 2.2 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-c

## 主题到 API 的映射规则

### 检测模式 相关接口

- ArkTS API
  - 2.1.1 @ohos.hichecker (检测模式)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hichecker

### Debug调试 相关接口

- ArkTS API
  - 2.1.2 @ohos.hidebug (Debug调试)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug

### HiLog日志打印 相关接口

- ArkTS API
  - 2.1.3 @ohos.hilog (HiLog日志打印)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog

### 分布式跟踪 相关接口

- ArkTS API
  - 2.1.4 @ohos.hiTraceChain (分布式跟踪)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracechain

### 性能打点 相关接口

- ArkTS API
  - 2.1.5 @ohos.hiTraceMeter (性能打点)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracemeter
  - 2.1.10.1 @ohos.bytrace (性能打点)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bytrace

### 故障延迟通知 相关接口

- ArkTS API
  - 2.1.6 @ohos.hiviewdfx.FaultLogExtensionAbility (故障延迟通知)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability

### 故障延迟通知上下文 相关接口

- ArkTS API
  - 2.1.7 @ohos.hiviewdfx.FaultLogExtensionContext (故障延迟通知上下文)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext

### 应用事件打点 相关接口

- ArkTS API
  - 2.1.8 @ohos.hiviewdfx.hiAppEvent (应用事件打点)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent

### js泄漏检测 相关接口

- ArkTS API
  - 2.1.9 @ohos.hiviewdfx.jsLeakWatcher (js泄漏检测)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-jsleakwatcher

### 已停止维护的接口 相关接口

- 通用入口
  - 2.1.10 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-arkts-dep

### 应用打点 相关接口

- ArkTS API
  - 2.1.10.2 @ohos.hiAppEvent (应用打点)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiappevent

### 故障日志获取 相关接口

- ArkTS API
  - 2.1.10.3 @ohos.faultLogger (故障日志获取)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger

### HiAppEvent 相关接口

- C API
  - 2.2.1.1 HiAppEvent：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent

### HiCollie 相关接口

- C API
  - 2.2.1.2 HiCollie：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie

### HiDebug 相关接口

- C API
  - 2.2.1.3 HiDebug：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug

### HiLog 相关接口

- C API
  - 2.2.1.4 HiLog：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hilog

### HiTrace 相关接口

- C API
  - 2.2.1.5 HiTrace：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace

### ParamListNode* 相关接口

- C API
  - 2.2.3.3 ParamListNode*：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hiappevent-paramlistnode8h

### HiDebug_Backtrace_Object__* 相关接口

- C API
  - 2.2.3.17 HiDebug_Backtrace_Object__*：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-backtrace-object--8h

### HiTraceId 相关接口

- C API
  - 2.2.3.20 HiTraceId：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hitrace-hitraceid

### 错误码与异常定位

- 通用入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-errcode
  - 2.3.1 Faultlogger 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-faultlogger
  - 2.3.2 应用事件打点错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiappevent
  - 2.3.3 HiDebug错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug
  - 2.3.4 HiDebug CpuUsage错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-cpuusage
  - 2.3.5 HiDebug Trace错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hidebug-trace
  - 2.3.6 HiCollie错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-hiviewdfx-hicollie
  - 2.3.7 JsLeakWatcher错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-jsleakwatcher

## 直接映射

- `检测模式`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hichecker
- `Debug调试`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hidebug
- `HiLog日志打印`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hilog
- `分布式跟踪`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracechain
- `性能打点`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hitracemeter
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bytrace
- `故障延迟通知`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensionability
- `故障延迟通知上下文`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-faultlogextensioncontext
- `应用事件打点`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiviewdfx-hiappevent
- `js泄漏检测`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-jsleakwatcher
- `已停止维护的接口`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-arkts-dep
- `应用打点`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hiappevent
- `故障日志获取`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-faultlogger

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 Performance Analysis Kit、@ohos.hichecker、检测模式、@ohos.hidebug、Debug调试 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
