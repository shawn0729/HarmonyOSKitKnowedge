# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 Network Kit API 参考入口时，读取本文件。

## API 总入口

- 2 Network Kit（网络服务）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-api-arkts
- 2.2 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-c

## 主题到 API 的映射规则

### 网络连接管理 相关接口

- ArkTS API
  - 2.1.1 @ohos.net.connection (网络连接管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection

### 以太网连接管理 相关接口

- ArkTS API
  - 2.1.2 @ohos.net.ethernet (以太网连接管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-ethernet

### 数据请求 相关接口

- ArkTS API
  - 2.1.3 @ohos.net.http (数据请求)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http
  - 2.3.2 @system.fetch (数据请求)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-fetch

### MDNS管理 相关接口

- ArkTS API
  - 2.1.4 @ohos.net.mdns (MDNS管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns

### 网络策略管理 相关接口

- ArkTS API
  - 2.1.5 @ohos.net.policy (网络策略管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-policy

### Socket连接 相关接口

- ArkTS API
  - 2.1.6 @ohos.net.socket (Socket连接)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket

### 流量管理 相关接口

- ArkTS API
  - 2.1.7 @ohos.net.statistics (流量管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-statistics

### 网络共享管理 相关接口

- ArkTS API
  - 2.1.8 @ohos.net.sharing (网络共享管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-sharing

### 图片增强 / 超分 / Processing

- ArkTS API
  - 2.1.9 @ohos.net.vpnExtension (VPN增强管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpnextension

### VPN管理 相关接口

- ArkTS API
  - 2.1.10 @ohos.net.vpn (VPN管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpn

### WebSocket连接 相关接口

- ArkTS API
  - 2.1.11 @ohos.net.webSocket (WebSocket连接)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-websocket

### 网络防火墙 相关接口

- ArkTS API
  - 2.1.12 @ohos.net.netFirewall (网络防火墙)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-netfirewall

### 网络安全校验 相关接口

- ArkTS API
  - 2.1.13 @ohos.net.networkSecurity (网络安全校验)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-networksecurity

### 扩展认证 相关接口

- ArkTS API
  - 2.1.14 @ohos.net.eap (扩展认证)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-eap

### 三方VPN能力 相关接口

- ArkTS API
  - 2.1.15 @ohos.app.ability.VpnExtensionAbility (三方VPN能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vpnextensionability

### VpnExtensionContext 相关接口

- ArkTS API
  - 2.1.16 VpnExtensionContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-vpnextensioncontext

### NetConnection 相关接口

- C API
  - 2.2.1.1 NetConnection：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection

### Netstack 相关接口

- C API
  - 2.2.1.2 Netstack：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack

### WebSocket 相关接口

- C API
  - 2.2.3.16 WebSocket：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket

### 已停止维护的接口 相关接口

- 通用入口
  - 2.3 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-arkts-dep

### 网络状态 相关接口

- ArkTS API
  - 2.3.1 @system.network (网络状态)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-network

### 错误码与异常定位

- 通用入口
  - 2.4 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-arkts-errcode
  - 2.4.1 HTTP错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-http
  - 2.4.2 Socket错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket
  - 2.4.3 webSocket错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket
  - 2.4.4 网络连接管理错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-connection
  - 2.4.5 以太网连接错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-ethernet
  - 2.4.6 扩展认证错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-eap
  - 2.4.7 网络共享错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-sharing
  - 2.4.8 策略管理错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-policy
  - 2.4.9 MDNS错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns
  - 2.4.10 流量管理错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-statistics
  - 2.4.11 VPN错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-vpn
  - 2.4.12 网络安全校验错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-networksecurity
  - 2.4.13 内核错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-kernel
  - 2.4.14 防火墙错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-netfirewall

## 直接映射

- `网络连接管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection
- `以太网连接管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-ethernet
- `数据请求`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-fetch
- `MDNS管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns
- `网络策略管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-policy
- `Socket连接`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket
- `流量管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-statistics
- `网络共享管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-sharing
- `VPN增强管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpnextension
- `VPN管理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpn
- `WebSocket连接`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-websocket
- `网络防火墙`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-netfirewall

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 Network Kit（网络服务）、@ohos.net.connection、网络连接管理、@ohos.net.ethernet、以太网连接管理 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
