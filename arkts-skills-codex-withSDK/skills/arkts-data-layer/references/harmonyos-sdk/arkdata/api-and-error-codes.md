# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 ArkData API 参考入口时，读取本文件。

## API 总入口

- 2 ArkData（方舟数据管理）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkdata-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkdata-arkts
- 2.3 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkdata-c

## 主题到 API 的映射规则

### 数据通用类型 相关接口

- ArkTS API
  - 2.1.1 @ohos.data.commonType (数据通用类型)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-commontype

### DataAbility谓词 相关接口

- ArkTS API
  - 2.1.2 @ohos.data.dataAbility (DataAbility谓词)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-ability

### 数据共享 相关接口

- ArkTS API
  - 2.1.3 @ohos.data.dataShare (数据共享)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-datashare

### 数据共享谓词 相关接口

- ArkTS API
  - 2.1.4 @ohos.data.dataSharePredicates (数据共享谓词)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-datasharepredicates

### 分布式数据对象 相关接口

- ArkTS API
  - 2.1.5 @ohos.data.distributedDataObject (分布式数据对象)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-distributedobject

### 分布式键值数据库 相关接口

- ArkTS API
  - 2.1.6 @ohos.data.distributedKVStore (分布式键值数据库)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedkvstore

### 用户首选项 相关接口

- ArkTS API
  - 2.1.7 @ohos.data.preferences (用户首选项)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-preferences

### 共享用户首选项 相关接口

- ArkTS API
  - 2.1.8 @ohos.data.sendablePreferences (共享用户首选项)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablepreferences

### 关系型数据库 相关接口

- ArkTS API
  - 2.1.9 @ohos.data.relationalStore (关系型数据库)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-relationalstore
  - 2.1.17.2 @ohos.data.rdb (关系型数据库)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-rdb

### RdbStore 相关接口

- ArkTS API
  - 2.1.9.3 Interface (RdbStore)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore

### ResultSet 相关接口

- ArkTS API
  - 2.1.9.4 Interface (ResultSet)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-resultset

### Transaction 相关接口

- ArkTS API
  - 2.1.9.5 Interface (Transaction)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-transaction

### RdbPredicates 相关接口

- ArkTS API
  - 2.1.9.7 Class (RdbPredicates)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbpredicates

### 共享关系型数据库 相关接口

- ArkTS API
  - 2.1.10 @ohos.data.sendableRelationalStore (共享关系型数据库)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablerelationalstore

### 标准化数据通路 相关接口

- ArkTS API
  - 2.1.11 @ohos.data.unifiedDataChannel (标准化数据通路)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-unifieddatachannel

### 标准化数据结构 相关接口

- ArkTS API
  - 2.1.12 @ohos.data.uniformDataStruct (标准化数据结构)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformdatastruct

### 标准化数据定义与描述 相关接口

- ArkTS API
  - 2.1.13 @ohos.data.uniformTypeDescriptor (标准化数据定义与描述)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-uniformtypedescriptor

### 数据集 相关接口

- ArkTS API
  - 2.1.14 @ohos.data.ValuesBucket (数据集)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-valuesbucket

### 智慧数据平台 相关接口

- ArkTS API
  - 2.1.15 @ohos.data.intelligence (智慧数据平台)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-intelligence

### 端云服务 相关接口

- ArkTS API
  - 2.1.16 @ohos.data.cloudData (端云服务)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-clouddata

### 已停止维护的接口 相关接口

- 通用入口
  - 2.1.17 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkdata-arkts-dep

### 分布式数据管理 相关接口

- ArkTS API
  - 2.1.17.1 @ohos.data.distributedData (分布式数据管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributed-data

### 轻量级存储 相关接口

- ArkTS API
  - 2.1.17.3 @ohos.data.storage (轻量级存储)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-storage

### 数据存储 相关接口

- ArkTS API
  - 2.1.17.4 @system.storage (数据存储)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-storage

### data 相关接口

- 通用入口
  - 2.1.17.5 data/rdb：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/data-rdb

### 结果集 相关接口

- ArkTS API
  - 2.1.17.5.1 resultSet (结果集)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-resultset

### ArkTS 组件 相关接口

- 通用入口
  - 2.2 ArkTS 组件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkdata-comp

### 内容卡片 相关接口

- ArkTS API
  - 2.2.1 @ohos.data.UdmfComponents (内容卡片)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-udmfcomponents

### Preferences 相关接口

- C API
  - 2.3.1.1 Preferences：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-preferences

### RDB 相关接口

- C API
  - 2.3.1.2 RDB：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb

### UDMF 相关接口

- C API
  - 2.3.1.3 UDMF：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-udmf

### 错误码与异常定位

- 通用入口
  - 2.4 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkdata-arkts-errcode
  - 2.4.1 关系型数据库错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-data-rdb
  - 2.4.2 数据共享错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-datashare
  - 2.4.3 分布式数据对象错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributed-dataobject
  - 2.4.4 分布式键值数据库错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-distributedkvstore
  - 2.4.5 用户首选项错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-preferences
  - 2.4.6 统一数据管理框架错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-udmf
  - 2.4.7 智慧数据平台错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-intelligence

## 直接映射

- `数据通用类型`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-commontype
- `DataAbility谓词`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-ability
- `数据共享`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-datashare
- `数据共享谓词`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-datasharepredicates
- `分布式数据对象`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-distributedobject
- `分布式键值数据库`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-distributedkvstore
- `用户首选项`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-preferences
- `共享用户首选项`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-sendablepreferences
- `关系型数据库`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-relationalstore
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-data-rdb
- `RdbStore`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore
- `ResultSet`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-resultset
- `Transaction`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-transaction

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 ArkData（方舟数据管理）、@ohos.data.commonType、数据通用类型、@ohos.data.dataAbility、DataAbility谓词 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
