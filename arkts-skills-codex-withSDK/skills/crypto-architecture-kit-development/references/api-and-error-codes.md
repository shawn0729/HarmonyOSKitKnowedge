# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 Crypto Architecture Kit API 参考入口时，读取本文件。

## API 总入口

- 2 Crypto Architecture Kit（加解密算法框架服务）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts
- 2.2 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-c

## 主题到 API 的映射规则

### 加解密算法库框架 相关接口

- ArkTS API
  - 2.1.1 @ohos.security.cryptoFramework (加解密算法库框架)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework

### 已停止维护的接口 相关接口

- 通用入口
  - 2.1.2 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts-dep

### 加密算法 相关接口

- ArkTS API
  - 2.1.2.1 @system.cipher (加密算法)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-cipher

### CryptoArchitectureKit 相关接口

- C API
  - 2.2.1.1 CryptoArchitectureKit：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoarchitecturekit

### CryptoAsymCipherApi 相关接口

- C API
  - 2.2.1.2 CryptoAsymCipherApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi

### CryptoAsymKeyApi 相关接口

- C API
  - 2.2.1.3 CryptoAsymKeyApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi

### CryptoCommonApi 相关接口

- C API
  - 2.2.1.4 CryptoCommonApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi

### CryptoDigestApi 相关接口

- C API
  - 2.2.1.5 CryptoDigestApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptodigestapi

### CryptoKdfApi 相关接口

- C API
  - 2.2.1.6 CryptoKdfApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi

### CryptoKeyAgreementApi 相关接口

- C API
  - 2.2.1.7 CryptoKeyAgreementApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokeyagreementapi

### CryptoMacApi 相关接口

- C API
  - 2.2.1.8 CryptoMacApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptomacapi

### CryptoRandApi 相关接口

- C API
  - 2.2.1.9 CryptoRandApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi

### CryptoSignatureApi 相关接口

- C API
  - 2.2.1.10 CryptoSignatureApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosignatureapi

### CryptoSymCipherApi 相关接口

- C API
  - 2.2.1.11 CryptoSymCipherApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymcipherapi

### CryptoSymKeyApi 相关接口

- C API
  - 2.2.1.12 CryptoSymKeyApi：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptosymkeyapi

### 错误码与异常定位

- 通用入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts-errcode
  - 2.3.1 crypto framework错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-crypto-framework

## 直接映射

- `加解密算法库框架`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework
- `已停止维护的接口`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/crypto-architecture-arkts-dep
- `加密算法`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-cipher
- `CryptoArchitectureKit`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoarchitecturekit
- `CryptoAsymCipherApi`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymcipherapi
- `CryptoAsymKeyApi`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptoasymkeyapi
- `CryptoCommonApi`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptocommonapi
- `CryptoDigestApi`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptodigestapi
- `CryptoKdfApi`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokdfapi
- `CryptoKeyAgreementApi`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptokeyagreementapi
- `CryptoMacApi`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptomacapi
- `CryptoRandApi`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cryptorandapi

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 加解密算法库框架、已停止维护的接口、@system.cipher、加密算法、CryptoArchitectureKit 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
