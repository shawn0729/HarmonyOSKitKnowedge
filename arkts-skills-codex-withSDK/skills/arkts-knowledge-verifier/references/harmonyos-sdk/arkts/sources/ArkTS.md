# 1 ArkTS（方舟编程语言）开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts

## 1.1 ArkTS简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-overview

## 1.2 ArkTS基础类库:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-utils

### 1.2.1 ArkTS基础类库概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-utils-overview

### 1.2.2 XML生成、解析与转换:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-generation-parsing-conversion

#### 1.2.2.1 XML概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-overview

#### 1.2.2.2 XML生成:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-generation

#### 1.2.2.3 XML解析:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-parsing

#### 1.2.2.4 XML转换:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/xml-conversion

### 1.2.3 Buffer与FastBuffer:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/buffer

### 1.2.4 JSON扩展库:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-json

### 1.2.5 ArkTS容器类库:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/containers

#### 1.2.5.1 容器类库概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/container-overview

#### 1.2.5.2 线性容器:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/linear-container

#### 1.2.5.3 非线性容器:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nonlinear-container

### 1.2.6 基础库常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/commonlibrary-faq

## 1.3 ArkTS并发:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-concurrency

### 1.3.1 并发概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/concurrency-overview

### 1.3.2 异步并发 (Promise和async/await):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/async-concurrency-overview

### 1.3.3 多线程并发:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multithread-concurrency

#### 1.3.3.1 多线程并发概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-concurrency-overview

#### 1.3.3.2 TaskPool简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction

#### 1.3.3.3 Worker简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-introduction

#### 1.3.3.4 TaskPool和Worker的对比 (TaskPool和Worker):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-vs-worker

### 1.3.4 并发线程间通信:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/interthread-communication

#### 1.3.4.1 ArkTS线程间通信概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/interthread-communication-overview

#### 1.3.4.2 线程间通信对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/interthread-communication-object

##### 1.3.4.2.1 线程间通信对象概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/serializable-overview

##### 1.3.4.2.2 普通对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/normal-object

##### 1.3.4.2.3 ArrayBuffer对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arraybuffer-object

##### 1.3.4.2.4 SharedArrayBuffer对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/shared-arraybuffer-object

##### 1.3.4.2.5 Transferable对象（NativeBinding对象）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/transferabled-object

##### 1.3.4.2.6 Sendable对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-object

###### 1.3.4.2.6.1 Sendable对象简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable

###### 1.3.4.2.6.2 Sendable使用规则与约束:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-constraints

###### 1.3.4.2.6.3 异步锁:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-async-lock-introduction

###### 1.3.4.2.6.4 异步等待:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-condition-variable-introduction

###### 1.3.4.2.6.5 ASON解析与生成:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ason-parsing-generation

###### 1.3.4.2.6.6 共享容器:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-collections-introduction

###### 1.3.4.2.6.7 共享模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable-module

###### 1.3.4.2.6.8 Sendable对象冻结:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-freeze

###### 1.3.4.2.6.9 Sendable使用场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide

#### 1.3.4.3 线程间通信场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/interthread-communication-guide

##### 1.3.4.3.1 使用TaskPool执行独立的耗时任务:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/independent-time-consuming-task

##### 1.3.4.3.2 使用TaskPool执行多个耗时任务:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-time-consuming-tasks

##### 1.3.4.3.3 TaskPool任务与宿主线程通信:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-communicates-with-mainthread

##### 1.3.4.3.4 Worker和宿主线程的即时消息通信:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-communicates-with-mainthread

##### 1.3.4.3.5 Worker同步调用宿主线程的接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-invoke-mainthread-interface

##### 1.3.4.3.6 多级Worker间高性能消息通信:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-postmessage-sendable

### 1.3.5 应用多线程开发实践:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multithread-develop-guide

#### 1.3.5.1 应用多线程开发概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multithread-develop-overview

#### 1.3.5.2 耗时任务并发场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task

##### 1.3.5.2.1 耗时任务并发场景简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/time-consuming-task-overview

##### 1.3.5.2.2 CPU密集型任务开发指导 (TaskPool和Worker):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cpu-intensive-task-development

##### 1.3.5.2.3 I/O密集型任务开发指导 (TaskPool):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/io-intensive-task-development

##### 1.3.5.2.4 同步任务开发指导 (TaskPool和Worker):https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sync-task-development

#### 1.3.5.3 长时任务并发场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/long-time-task

##### 1.3.5.3.1 长时任务并发场景简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/long-time-task-overview

##### 1.3.5.3.2 长时任务开发指导（TaskPool）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/long-time-task-guide

#### 1.3.5.4 常驻任务并发场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resident-task

##### 1.3.5.4.1 常驻任务并发场景简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resident-task-overview

##### 1.3.5.4.2 常驻任务开发指导（Worker）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resident-task-guide

#### 1.3.5.5 应用多线程开发实践案例:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multithread-develop-case

##### 1.3.5.5.1 批量数据写数据库场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/batch-database-operations-guide

##### 1.3.5.5.2 业务模块并发加载场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/concurrent-loading-modules-guide

##### 1.3.5.5.3 全局配置项功能场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/global-configuration-guide

##### 1.3.5.5.4 ArkUI数据更新场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/makeobserved-sendable

##### 1.3.5.5.5 C++线程间数据共享场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-interthread-shared

##### 1.3.5.5.6 TaskPool指定任务并发度场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-async-task-guide

##### 1.3.5.5.7 ArkUI瀑布流渲染场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-waterflow

##### 1.3.5.5.8 获取最近访问列表场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendablelrucache-recent-list

##### 1.3.5.5.9 多线程取消TaskPool任务场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-cancel-task

##### 1.3.5.5.10 自定义Native Transferable对象的多线程操作场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-coerce-to-native-binding-object

##### 1.3.5.5.11 自定义Native Sendable对象的多线程操作场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/napi-define-sendable-object

##### 1.3.5.5.12 Worker常驻线程通过TaskPool进行多任务并发处理:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-and-taskpool

### 1.3.6 并发常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/concurrency-faq

## 1.4 ArkTS跨语言交互:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-cross-language-interaction

## 1.5 ArkTS运行时:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-runtime

### 1.5.1 ArkTS运行时概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-runtime-overview

### 1.5.2 GC垃圾回收:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gc-introduction

### 1.5.3 ArkTS模块化:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-runtime-module

#### 1.5.3.1 模块化运行简介:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-principle

#### 1.5.3.2 动态加载:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dynamic-import

#### 1.5.3.3 延迟加载（lazy import）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-lazy-import

#### 1.5.3.4 同步方式动态加载Native模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/js-apis-load-native-module

#### 1.5.3.5 静态方式加载Native模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-import-native-module

#### 1.5.3.6 基于Node-API加载模块:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/load-module-base-nodeapi

#### 1.5.3.7 模块加载副作用及优化:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-module-side-effects

### 1.5.4 ArkTS运行时常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-runtime-faq

## 1.6 ArkTS编译工具链:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-compilation-tool-chain

### 1.6.1 ArkTS编译工具链概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/compilation-tool-chain-overview

### 1.6.2 方舟字节码:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bytecode

#### 1.6.2.1 方舟字节码概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bytecode-overview

#### 1.6.2.2 方舟字节码文件格式:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bytecode-file-format

#### 1.6.2.3 方舟字节码基本原理:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bytecode-fundamentals

#### 1.6.2.4 方舟字节码函数命名规则:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-bytecode-function-name

#### 1.6.2.5 编译期自定义修改方舟字节码:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/customize-bytecode-during-compilation

#### 1.6.2.6 方舟字节码生成常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/es2abc-faq

### 1.6.3 Disassembler反汇编工具:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/tool-disassembler

### 1.6.4 ArkGuard源码混淆工具:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-arkguard

#### 1.6.4.1 ArkGuard源码混淆工具概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-overview

#### 1.6.4.2 ArkGuard混淆原理及功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation

#### 1.6.4.3 ArkGuard混淆开启指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-guide

#### 1.6.4.4 不同包类型的源码混淆建议:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-practice

#### 1.6.4.5 ArkGuard混淆常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-questions

### 1.6.5 ArkGuard字节码混淆工具:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-arkguard-bytecode

#### 1.6.5.1 ArkGuard字节码混淆工具概述:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bytecode-obfuscation-overview

#### 1.6.5.2 ArkGuard字节码混淆原理及功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bytecode-obfuscation

#### 1.6.5.3 ArkGuard字节码混淆开启指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bytecode-obfuscation-guide

#### 1.6.5.4 不同包类型的字节码混淆建议:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bytecode-obfuscation-practice

#### 1.6.5.5 ArkGuard字节码混淆常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bytecode-obfuscation-questions

### 1.6.6 在build-profile.json5中配置arkOptions:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkoptions-guide

---

# 2 ArkTS（方舟编程语言）API参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-api

## 2.1 ArkTS API:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-arkts

### 2.1.1 @arkts.collections (ArkTS容器集):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-collections

#### 2.1.1.1 模块描述:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections

#### 2.1.1.2 Class (Array):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-array

#### 2.1.1.3 Class (Map):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-map

#### 2.1.1.4 Class (Set):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-set

#### 2.1.1.5 Class (ArrayBuffer):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-arraybuffer

#### 2.1.1.6 Class (Int8Array):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-int8array

#### 2.1.1.7 Class (Uint8Array):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint8array

#### 2.1.1.8 Class (Int16Array):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-int16array

#### 2.1.1.9 Class (Uint16Array):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint16array

#### 2.1.1.10 Class (Int32Array):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-int32array

#### 2.1.1.11 Class (Uint32Array):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint32array

#### 2.1.1.12 Class (Uint8ClampedArray):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-uint8clampedarray

#### 2.1.1.13 Class (Float32Array):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-float32array

#### 2.1.1.14 Class (BitVector):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-bitvector

#### 2.1.1.15 Interface (ConcatArray):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-concatarray

#### 2.1.1.16 Types:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-collections-types

### 2.1.2 @arkts.lang (ArkTS语言基础能力):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-lang

### 2.1.3 @arkts.math.Decimal (高精度数学库Decimal):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-decimal

### 2.1.4 @arkts.utils (ArkTS工具库):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkts-utils

#### 2.1.4.1 模块描述:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils

#### 2.1.4.2 Functions:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-f

#### 2.1.4.3 ArkTSUtils.locks:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-locks

#### 2.1.4.4 ArkTSUtils.ASON:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-ason

#### 2.1.4.5 SendableLruCache<K, V>:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-arkts-utils-sendablelrucache

### 2.1.5 @ohos.buffer (Buffer):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-buffer

### 2.1.6 @ohos.convertxml (xml转换JavaScript):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-convertxml

### 2.1.7 @ohos.fastbuffer (FastBuffer):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fastbuffer

### 2.1.8 @ohos.process (获取进程相关的信息):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-process

### 2.1.9 @ohos.taskpool (启动任务池):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool

### 2.1.10 @ohos.uri (URI字符串解析):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uri

### 2.1.11 @ohos.url (URL字符串解析):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-url

### 2.1.12 @ohos.util (util工具函数):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util

### 2.1.13 @ohos.util.ArrayList (线性容器ArrayList):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arraylist

### 2.1.14 @ohos.util.Deque (线性容器Deque):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-deque

### 2.1.15 @ohos.util.HashMap (非线性容器HashMap):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hashmap

### 2.1.16 @ohos.util.HashSet (非线性容器HashSet):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-hashset

### 2.1.17 @ohos.util.json (JSON解析与生成):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json

### 2.1.18 @ohos.util.LightWeightMap (非线性容器LightWeightMap):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-lightweightmap

### 2.1.19 @ohos.util.LightWeightSet (非线性容器LightWeightSet):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-lightweightset

### 2.1.20 @ohos.util.LinkedList (线性容器LinkedList):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-linkedlist

### 2.1.21 @ohos.util.List (线性容器List):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-list

### 2.1.22 @ohos.util.PlainArray (非线性容器PlainArray):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-plainarray

### 2.1.23 @ohos.util.Queue (线性容器Queue):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-queue

### 2.1.24 @ohos.util.Stack (线性容器Stack):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stack

### 2.1.25 @ohos.util.stream (数据流基类stream):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stream

### 2.1.26 @ohos.util.TreeMap (非线性容器TreeMap):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-treemap

### 2.1.27 @ohos.util.TreeSet (非线性容器TreeSet):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-treeset

### 2.1.28 @ohos.worker (启动一个Worker):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-worker

### 2.1.29 @ohos.xml (XML解析与生成):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-xml

### 2.1.30 已停止维护的接口:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-arkts-dep

#### 2.1.30.1 @ohos.util.Vector (线性容器Vector):https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vector

## 2.2 错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-arkts-errcode

### 2.2.1 语言基础类库错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-utils

### 2.2.2 Typescript Compiler错误码介绍:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-tsc

### 2.2.3 编译工具链错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ets-loader

### 2.2.4 Es2abc编译器错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-es2abc

### 2.2.5 源码混淆错误码:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-source-obfuscation

---

# 3 最佳实践:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-language

## 3.1 ArkTS高性能编程:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-high-performance

## 3.2 应用并发设计:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-app-concurrency-design

## 3.3 TaskPool和Worker对比:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-comparative_practice_of_taskpool_and_worker

## 3.4 TaskPool使用规范:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-taskpool_usage_specifications_and_faqs

## 3.5 应用切面编程设计:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-aspect-programming-design

## 3.6 应用埋点:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-track-practice

## 3.7 基于Aspect插件库实现切面编程:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-aspect-implements-aop

---

# 4 FAQ:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts

## 4.1 方舟编程语言（ArkTS）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-kit

### 4.1.1 ArkTS语言与ArkUI框架、HarmonyOS SDK/API的关系:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-143

### 4.1.2 将rawfile中json格式的字符串转换成对应的object对象后，调用实例方法后程序崩溃:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-1

### 4.1.3 如何使用正则表达式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-3

### 4.1.4 如何生成随机的uuid:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-14

### 4.1.5 ArkTS中有类似Java中的System.arraycopy数组复制的方法吗:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-15

### 4.1.6 ArkTS文件后缀是否需要全部改成.ets:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-16

### 4.1.7 编译后生成的.abc文件存放路径在哪里:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-17

### 4.1.8 ArkTS文件和TS文件的区别:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-18

### 4.1.9 如何实现字符串编解码:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-19

### 4.1.10 如何生成UUID的字符串:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-20

### 4.1.11 使用NAPI扩展TS接口时，常用属性和实现接口的基本用法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-21

### 4.1.12 pthread创建的线程中如何读取rawfile:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-23

### 4.1.13 ArkTS的SendableClass对象内存共享的原理和限制是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-38

### 4.1.14 synchronized在Java中可以修饰方法，从而简单地实现方法的同步调用。在系统ets开发中，如何简单实现该功能:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-44

### 4.1.15 ArkTS类的方法是否支持重载:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-45

### 4.1.16 如何将类Java语言的线程模型（内存共享）的实现方式转换成在ArkTS的线程模型下（内存隔离）的实现方式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-46

### 4.1.17 以libstd为例，C++的标准库放在哪里了，有没有打到hap包中:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-48

### 4.1.18 AOT编译模式的产物及ap、an、ai文件是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-52

### 4.1.19 .ets文件和.ts文件的区别及如何互相调用文件中定义的方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-53

### 4.1.20 ArkTS中globalThis无法使用该如何替换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-54

### 4.1.21 ArkTS中this的常用场景及使用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-55

### 4.1.22 如何访问类的静态变量和方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-56

### 4.1.23 如何合并两个对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-61

### 4.1.24 如何实现类似Java中的反射方法调用能力:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-62

### 4.1.25 系统使用了ArkTS作为开发语言，那这些代码在底层的解释运行的环境是自研的还是用的开源的，比如v8、jscore？另外系统也适配了React Native引擎，是不是也是复用的这个运行环境:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-64

### 4.1.26 ArkTS里有哪些转换数据类型的方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-65

### 4.1.27 是否支持开发者自行管理线程数量:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-69

### 4.1.28 是否支持模块的动态加载？如何实现:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-70

### 4.1.29 如何实现AOP（代码插桩）能力:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-71

### 4.1.30 如何使用AOP接口实现重复插桩或替换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-72

### 4.1.31 如何判断能否对接口进行插桩或替换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-74

### 4.1.32 如何解析JSON字符串为实例对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-75

### 4.1.33 如何在ArkTS中实现运行时注解的能力:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-77

### 4.1.34 如何在ArkTS中实现自定义装饰器能力:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-78

### 4.1.35 ArkTS是否支持解构:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-80

### 4.1.36 是否支持在TS文件中加载ArkTS文件，TS是否会被限制使用:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-82

### 4.1.37 ArkTS是否支持反射调用类的静态成员函数和实例成员函数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-83

### 4.1.38 如何通过Index获取ArrayList中的元素:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-85

### 4.1.39 如何将Map转换为JSON字符串:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-86

### 4.1.40 如何获取对象的类名:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-87

### 4.1.41 如何将JSON对象转换成HashMap:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-89

### 4.1.42 如何将ArrayBuffer转成string:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-90

### 4.1.43 Uint8Array类型和String以及hex如何互相转换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-91

### 4.1.44 如何进行base64编码:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-92

### 4.1.45 赋值和深拷贝与浅拷贝的区别:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-93

### 4.1.46 ArkTS是否支持多继承:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-95

### 4.1.47 ArkTS是否支持交叉类型:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-96

### 4.1.48 ArkTS是否支持匿名内部类:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-97

### 4.1.49 如何使用Record:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-98

### 4.1.50 如何通过AOP统计方法执行时间:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-99

### 4.1.51 如何快速生成class的setter和getter方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-101

### 4.1.52 如何实现Sendable类型和JSON数据的转换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-102

### 4.1.53 如何处理大整数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-104

### 4.1.54 如何通过判断函数入参类型实现不同代码逻辑:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-105

### 4.1.55 如何使用工具库对JSON进行解析与生成:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-106

### 4.1.56 A持有B，B引用A的场景会不会导致内存泄漏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-107

### 4.1.57 如何通过key获取对象值:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-108

### 4.1.58 ModuleManager模块加载流程是什么样的:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-109

### 4.1.59 如何查看编译的详细过程:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-110

### 4.1.60 如何遍历JSON对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-111

### 4.1.61 如何判断对象的类型:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-112

### 4.1.62 如何在ArkTS使用Reflect正确绑定this指针:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-113

### 4.1.63 混淆后的映射文件具体在哪个路径下:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-114

### 4.1.64 如何获取对象的所有方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-115

### 4.1.65 如何使用内置的js引擎？JIT支持策略如何:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-116

### 4.1.66 如何在ArkTS中使用闭包:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-117

### 4.1.67 是否支持通过动态import反射调用类的静态成员函数和实例成员函数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-118

### 4.1.68 如何获取环境变量信息:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-125

### 4.1.69 如何获取应用进程的CPU使用时间:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-127

### 4.1.70 如何指定对象某些属性参与序列化:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-128

### 4.1.71 对象反序列化时number类型丢失精度如何解决:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-129

### 4.1.72 Array的长度上限是多少:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-131

### 4.1.73 当前ArkTS是否采用类Node.js的异步I/O机制:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-132

### 4.1.74 对于网络请求这类I/O密集型任务是否需要使用多线程进行处理:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-133

### 4.1.75 对于@ohos.net.http模块是否需要使用TaskPool处理:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-134

### 4.1.76 模块间循环依赖导致运行时未初始化异常问题定位:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-135

### 4.1.77 编译异常，无具体错误日志，难以定位问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-136

### 4.1.78 gbk字符串TextEncoder编码结果属性buffer长度为何比编码结果长度略大:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-137

### 4.1.79 ArkTS如何定义callback函数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-138

### 4.1.80 对象中函数的this如何指向外层:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-139

### 4.1.81 如何实现匿名内部类:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-140

### 4.1.82 如何定义一个具有任意键的对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-141

### 4.1.83 如何在调用处实现接口中的方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-142

### 4.1.84 ArkTS类型转换方法，除了使用as是否有其他方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-144

### 4.1.85 如何在Index.ets中导出默认导出的对象:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-145

### 4.1.86 ArkTS是否支持调用js文件中的方法:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-146

### 4.1.87 是否支持获取编译阶段的ets文件的AST语法树:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-147

### 4.1.88 应用通过对象字面量初始化class实例导致编译失败的原因和修改方案:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-148

### 4.1.89 如何在URL编码时处理特殊字符:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-150

### 4.1.90 ArkTS自定义注解使用场景:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-151

## 4.2 ArkTS线程模型和并发:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model

### 4.2.1 有哪些创建线程的方式:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-2

### 4.2.2 应该如何设计大量线程并发方案:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-25

### 4.2.3 如何设置Task优先级:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-26

### 4.2.4 线程间JS对象通过序列化方式进行数据通信，是否存在性能问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-24

### 4.2.5 TaskPool和Worker的异同点:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-27

### 4.2.6 Worker和TaskPool的线程数量是否有限制:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-28

### 4.2.7 JS线程通过napi创建的C++线程的处理结果，如何返回JS线程:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-30

### 4.2.8 系统多线程模型是什么样的:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-32

### 4.2.9 是否支持Context跨线程传递:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-33

### 4.2.10 在多线程并发场景中，如何实现安全访问同一块共享内存:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-34

### 4.2.11 子线程和主线程的优先级及任务执行策略是什么:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-35

### 4.2.12 ArkTS中Worker线程、TaskPool线程如何与宿主线程通信:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-36

### 4.2.13 ArkTS是否支持类似Java的共享内存模型进行多线程开发:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-37

### 4.2.14 ArkTS的线程机制是怎么样的？每个线程是一个单独的JS引擎吗？如果每个线程开销较小的话，为什么要限制线程数量:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-39

### 4.2.15 TaskPool在任务执行过程中如何跟主线程进行通信？如何操作同一块内存变量:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-40

### 4.2.16 对于多线程操作首选项和数据库是不是线程安全的？还是每一个线程独立的:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-41

### 4.2.17 如果在ArkTS中大部分后台任务（计算、埋点、数据存储）都使用异步并发的方式，是否会使主线程响应变慢，引起卡顿掉帧问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-42

### 4.2.18 在ArkTS的主线程中使用await会阻塞主线程吗:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-43

### 4.2.19 是否可以在TaskPool中动态加载模块（HAR、HSP、SO）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-47

### 4.2.20 TaskPool线程内存如何共享:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-58

### 4.2.21 TaskPool后台I/O任务池，应用能否自行做管控？是否有方法开放管理机制:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-59

### 4.2.22 如何解决应用需要避免创建过多线程，并发处理任务数量受限，无法充分发挥设备性能的问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-60

### 4.2.23 Worker线程内存如何共享:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-66

### 4.2.24 如何判断是否为主线程:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-68

### 4.2.25 如何对异步方法进行插桩/替换:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-100

### 4.2.26 ArkTS实现多Worker实例:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-103

### 4.2.27 如何使用TaskPool在子线程调用对象成员函数:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-120

### 4.2.28 如何在Worker中开启多级子线程:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-121

### 4.2.29 如何在TaskPool和Worker获取上下文Context:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-122

### 4.2.30 是否支持#include <memory_resource>和std::pmr::vector:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-149
