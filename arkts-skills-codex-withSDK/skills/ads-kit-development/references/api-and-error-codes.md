# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 Ads Kit API 参考入口时，读取本文件。

## API 总入口

- 2 Ads Kit（广告服务）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ads-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ads-arkts

## 主题到 API 的映射规则

### 广告服务框架 相关接口

- ArkTS API
  - 2.1.1 @ohos.advertising (广告服务框架)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising

### 开放匿名设备标识服务 相关接口

- ArkTS API
  - 2.1.2 @ohos.identifier.oaid (开放匿名设备标识服务)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-oaid

### 广告扩展服务 相关接口

- ArkTS API
  - 2.1.3 @ohos.advertising.AdsServiceExtensionAbility(广告扩展服务)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adsserviceextensionability

### ArkTS组件 相关接口

- 通用入口
  - 2.2 ArkTS组件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ads-comp

### 广告展示组件 相关接口

- ArkTS API
  - 2.2.1 @ohos.advertising.AdComponent (广告展示组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adcomponent

### 轮播广告展示组件 相关接口

- ArkTS API
  - 2.2.2 @ohos.advertising.AutoAdComponent (轮播广告展示组件)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-autoadcomponent

### 错误码与异常定位

- 通用入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ads-arkts-errcode
  - 2.3.1 广告服务框架错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ads
  - 2.3.2 开放匿名设备标识服务错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-oaid

## 直接映射

- `广告服务框架`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising
- `开放匿名设备标识服务`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-oaid
- `广告扩展服务`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adsserviceextensionability
- `ArkTS组件`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ads-comp
- `广告展示组件`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adcomponent
- `轮播广告展示组件`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-autoadcomponent
- `广告服务框架错误码`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-ads
- `开放匿名设备标识服务错误码`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-oaid

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 Ads Kit（广告服务）、@ohos.advertising、广告服务框架、@ohos.identifier.oaid、开放匿名设备标识服务 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
