# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 Core File Kit API 参考入口时，读取本文件。

## API 总入口

- 2 Core File Kit（文件基础服务）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-file-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-file-arkts
- 2.2 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-file-c

## 主题到 API 的映射规则

### 备份恢复扩展能力 相关接口

- ArkTS API
  - 2.1.1 @ohos.application.BackupExtensionAbility (备份恢复扩展能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-backupextensionability
  - 2.1.13 @ohos.file.BackupExtensionContext (备份恢复扩展能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-backupextensioncontext

### 端云同步能力 相关接口

- ArkTS API
  - 2.1.2 @ohos.file.cloudSync (端云同步能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-cloudsync

### 端云同步管理能力 相关接口

- ArkTS API
  - 2.1.3 @ohos.file.cloudSyncManager (端云同步管理能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-cloudsyncmanager

### 目录环境能力 相关接口

- ArkTS API
  - 2.1.4 @ohos.file.environment (目录环境能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-environment

### 文件URI 相关接口

- ArkTS API
  - 2.1.5 @ohos.file.fileuri (文件URI)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri

### 文件管理 相关接口

- ArkTS API
  - 2.1.6 @ohos.file.fs (文件管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs
  - 2.1.14.2 @ohos.fileio (文件管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileio

### 文件哈希处理 相关接口

- ArkTS API
  - 2.1.7 @ohos.file.hash (文件哈希处理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-hash

### 选择器 相关接口

- ArkTS API
  - 2.1.8 @ohos.file.picker (选择器)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker

### 数据标签 相关接口

- ArkTS API
  - 2.1.9 @ohos.file.securityLabel (数据标签)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-securitylabel

### 文件系统空间统计 相关接口

- ArkTS API
  - 2.1.10 @ohos.file.statvfs (文件系统空间统计)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-statvfs

### 应用空间统计 相关接口

- ArkTS API
  - 2.1.11 @ohos.file.storageStatistics (应用空间统计)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-storage-statistics

### 文件分享 相关接口

- ArkTS API
  - 2.1.12 @ohos.fileshare (文件分享)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileshare

### 已停止维护的接口 相关接口

- 通用入口
  - 2.1.14 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-file-arkts-dep

### 文件交互 相关接口

- ArkTS API
  - 2.1.14.1 @ohos.document (文件交互)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-document

### statfs 相关接口

- ArkTS API
  - 2.1.14.3 @ohos.statfs (statfs)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-statfs

### 文件存储 相关接口

- ArkTS API
  - 2.1.14.4 @system.file (文件存储)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-file

### Environment 相关接口

- C API
  - 2.2.1.1 Environment：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-environment

### FileIO 相关接口

- C API
  - 2.2.1.2 FileIO：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileio

### fileShare 相关接口

- C API
  - 2.2.1.3 fileShare：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileshare

### fileUri 相关接口

- C API
  - 2.2.1.4 fileUri：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-fileuri

### CloudDisk 相关接口

- C API
  - 2.2.1.5 CloudDisk：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-clouddisk

### 错误码与异常定位

- 通用入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/core-file-arkts-errcode
  - 2.3.1 文件管理错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-filemanagement

## 直接映射

- `备份恢复扩展能力`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-backupextensionability
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-backupextensioncontext
- `端云同步能力`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-cloudsync
- `端云同步管理能力`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-cloudsyncmanager
- `目录环境能力`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-environment
- `文件URI`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fileuri
- `文件管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileio
- `文件哈希处理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-hash
- `选择器`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker
- `数据标签`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-securitylabel
- `文件系统空间统计`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-statvfs
- `应用空间统计`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-storage-statistics
- `文件分享`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-fileshare

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 Core File Kit（文件基础服务）、备份恢复扩展能力、@ohos.file.cloudSync、端云同步能力、端云同步管理能力 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
