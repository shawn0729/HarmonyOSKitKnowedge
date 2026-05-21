# Network Kit 总览与主题路由

## 使用方式

- 当用户问题主题不明确时，先根据下面的主题索引定位主主题，再读取对应 reference。
- 默认先看开发指南；需要接口细节时再看 API；需要避坑和排障时再补最佳实践或 FAQ。

## 主题索引

### Network Kit（网络服务）

#### 主题入口

- 开发指南入口
  - 1 Network Kit（网络服务）开发指南：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-kit
    - 关键词：Network Kit（网络服务）

### Network Kit

#### 主题入口

- 开发指南入口
  - 1.1 Network Kit简介：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-mgmt-overview
    - 关键词：Network Kit

### Network Kit术语

#### 主题入口

- 开发指南入口
  - 1.2 Network Kit术语：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-terminology
    - 关键词：Network Kit术语

### 访问网络

#### 主题入口

- 开发指南入口
  - 1.3 访问网络：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-kit-data-transmission
    - 关键词：访问网络
  - 1.3.1 使用HTTP访问网络：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/http-request
    - 关键词：HTTP访问网络
  - 1.3.2 使用WebSocket访问网络：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/websocket-connection
    - 关键词：WebSocket访问网络
  - 1.3.3 使用WebSocket访问网络(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-websocket-guidelines
    - 关键词：WebSocket访问网络 / C++
  - 1.3.4 使用Socket访问网络：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/socket-connection
    - 关键词：Socket访问网络
  - 1.3.5 使用MDNS访问局域网服务：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-mdns
    - 关键词：MDNS访问局域网服务

### 连接网络

#### 主题入口

- 开发指南入口
  - 1.4 连接网络：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-kit-network-connecttion
    - 关键词：连接网络
  - 1.4.1 管理网络连接：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-connection-manager
    - 关键词：网络连接
  - 1.4.2 管理网络连接(C/C++)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-netmanager-guidelines
    - 关键词：网络连接 / C++
  - 1.4.3 连接VPN：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-vpnextension
    - 关键词：连接VPN

### 网络

#### 主题入口

- 开发指南入口
  - 1.5 管理网络：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-kit-network-management
    - 关键词：网络

### 管理网络

#### 主题入口

- 开发指南入口
  - 1.5.1 统计网络流量消耗：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-statistics
    - 关键词：统计网络流量消耗
  - 1.5.2 使用网络防火墙：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-netfirewall
    - 关键词：网络防火墙
  - 1.5.3 扩展认证：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-eap
    - 关键词：扩展认证

### API与错误码

#### 核心 API

- API入口
  - 2 Network Kit（网络服务）API参考：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-api
    - 关键词：Network Kit（网络服务）
  - 2.1 ArkTS API：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-api-arkts
    - 关键词：ArkTS
  - 2.1.1 @ohos.net.connection (网络连接管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-connection
    - 关键词：@ohos.net.connection / 网络连接管理
  - 2.1.2 @ohos.net.ethernet (以太网连接管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-ethernet
    - 关键词：@ohos.net.ethernet / 以太网连接管理
  - 2.1.3 @ohos.net.http (数据请求)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-http
    - 关键词：@ohos.net.http / 数据请求
  - 2.1.4 @ohos.net.mdns (MDNS管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-mdns
    - 关键词：@ohos.net.mdns / MDNS管理
  - 2.1.5 @ohos.net.policy (网络策略管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-policy
    - 关键词：@ohos.net.policy / 网络策略管理
  - 2.1.6 @ohos.net.socket (Socket连接)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-socket
    - 关键词：@ohos.net.socket / Socket连接
  - 2.1.7 @ohos.net.statistics (流量管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-statistics
    - 关键词：@ohos.net.statistics / 流量管理
  - 2.1.8 @ohos.net.sharing (网络共享管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-sharing
    - 关键词：@ohos.net.sharing / 网络共享管理
  - 2.1.9 @ohos.net.vpnExtension (VPN增强管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpnextension
    - 关键词：@ohos.net.vpnExtension / VPN增强管理
  - 2.1.10 @ohos.net.vpn (VPN管理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpn
    - 关键词：@ohos.net.vpn / VPN管理
  - 2.1.11 @ohos.net.webSocket (WebSocket连接)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-websocket
    - 关键词：@ohos.net.webSocket / WebSocket连接
  - 2.1.12 @ohos.net.netFirewall (网络防火墙)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-netfirewall
    - 关键词：@ohos.net.netFirewall / 网络防火墙
  - 2.1.13 @ohos.net.networkSecurity (网络安全校验)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-networksecurity
    - 关键词：@ohos.net.networkSecurity / 网络安全校验
  - 2.1.14 @ohos.net.eap (扩展认证)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-eap
    - 关键词：@ohos.net.eap / 扩展认证
  - 2.1.15 @ohos.app.ability.VpnExtensionAbility (三方VPN能力)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-vpnextensionability
    - 关键词：@ohos.app.ability.VpnExtensionAbility / 三方VPN能力
  - 2.1.16 VpnExtensionContext：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-vpnextensioncontext
    - 关键词：VpnExtensionContext
  - 2.2 C API：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-c
  - 2.2.1 模块：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-module
  - 2.2.1.1 NetConnection：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection
    - 关键词：NetConnection
  - 2.2.1.2 Netstack：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack
    - 关键词：Netstack
  - 2.2.2 头文件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-headerfile
  - 2.2.2.1 net_connection.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-h
    - 关键词：net_connection.h
  - 2.2.2.2 net_connection_type.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h
    - 关键词：net_connection_type.h
  - 2.2.2.3 net_ssl_c.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-h
    - 关键词：net_ssl_c.h
  - 2.2.2.4 net_ssl_c_type.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h
    - 关键词：net_ssl_c_type.h
  - 2.2.2.5 net_websocket.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-h
    - 关键词：net_websocket.h
  - 2.2.2.6 net_websocket_type.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h
    - 关键词：net_websocket_type.h
  - 2.2.2.7 net_http.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-h
    - 关键词：net_http.h
  - 2.2.2.8 net_http_type.h：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h
    - 关键词：net_http_type.h
  - 2.2.3 结构体：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-struct
  - 2.2.3.1 NetConn_NetHandle：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandle
    - 关键词：NetConn_NetHandle
  - 2.2.3.2 NetConn_NetCapabilities：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netcapabilities
    - 关键词：NetConn_NetCapabilities
  - 2.2.3.3 NetConn_NetAddr：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr
    - 关键词：NetConn_NetAddr
  - 2.2.3.4 NetConn_Route：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-route
    - 关键词：NetConn_Route
  - 2.2.3.5 NetConn_HttpProxy：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-httpproxy
    - 关键词：NetConn_HttpProxy
  - 2.2.3.6 NetConn_ConnectionProperties：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-connectionproperties
    - 关键词：NetConn_ConnectionProperties
  - 2.2.3.7 NetConn_NetHandleList：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandlelist
    - 关键词：NetConn_NetHandleList
  - 2.2.3.8 NetConn_NetSpecifier：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netspecifier
    - 关键词：NetConn_NetSpecifier
  - 2.2.3.9 NetConn_NetConnCallback：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netconncallback
    - 关键词：NetConn_NetConnCallback
  - 2.2.3.10 NetConn_ProbeResultInfo：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-proberesultinfo
    - 关键词：NetConn_ProbeResultInfo
  - 2.2.3.11 NetConn_TraceRouteInfo：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteinfo
    - 关键词：NetConn_TraceRouteInfo
  - 2.2.3.12 NetConn_TraceRouteOption：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteoption
    - 关键词：NetConn_TraceRouteOption
  - 2.2.3.13 NetStack_CertBlob：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certblob
    - 关键词：NetStack_CertBlob
  - 2.2.3.14 NetStack_CertificatePinning：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificatepinning
    - 关键词：NetStack_CertificatePinning
  - 2.2.3.15 NetStack_Certificates：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificates
    - 关键词：NetStack_Certificates
  - 2.2.3.16 WebSocket：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket
    - 关键词：WebSocket
  - 2.2.3.17 WebSocket_CloseResult：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-closeresult
    - 关键词：WebSocket_CloseResult
  - 2.2.3.18 WebSocket_CloseOption：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-closeoption
    - 关键词：WebSocket_CloseOption
  - 2.2.3.19 WebSocket_ErrorResult：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-errorresult
    - 关键词：WebSocket_ErrorResult
  - 2.2.3.20 WebSocket_OpenResult：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-openresult
    - 关键词：WebSocket_OpenResult
  - 2.2.3.21 WebSocket_Header：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-header
    - 关键词：WebSocket_Header
  - 2.2.3.22 WebSocket_RequestOptions：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-requestoptions
    - 关键词：WebSocket_RequestOptions
  - 2.2.3.23 Http_Buffer：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer
    - 关键词：Http_Buffer
  - 2.2.3.24 Http_HeaderValue：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headervalue
    - 关键词：Http_HeaderValue
  - 2.2.3.25 Http_HeaderEntry：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headerentry
    - 关键词：Http_HeaderEntry
  - 2.2.3.26 Http_ClientCert：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-clientcert
    - 关键词：Http_ClientCert
  - 2.2.3.27 Http_CustomProxy：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-customproxy
    - 关键词：Http_CustomProxy
  - 2.2.3.28 Http_Proxy：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-proxy
    - 关键词：Http_Proxy
  - 2.2.3.29 Http_PerformanceTiming：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-performancetiming
    - 关键词：Http_PerformanceTiming
  - 2.2.3.30 Http_RequestOptions：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-requestoptions
    - 关键词：Http_RequestOptions
  - 2.2.3.31 Http_Response：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-response
    - 关键词：Http_Response
  - 2.2.3.32 Http_Request：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request
    - 关键词：Http_Request
  - 2.2.3.33 Http_EventsHandler：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-eventshandler
    - 关键词：Http_EventsHandler
  - 2.2.3.34 Http_Headers：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers
    - 关键词：Http_Headers
  - 2.3.1 @system.network (网络状态)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-network
    - 关键词：@system.network / 网络状态
  - 2.3.2 @system.fetch (数据请求)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-fetch
    - 关键词：@system.fetch / 数据请求

#### 已停止维护接口

- API入口
  - 2.3 已停止维护的接口：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-arkts-dep
    - 关键词：已停止维护的接口

#### 错误码

- API入口
  - 2.4 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-arkts-errcode
    - 关键词：错误码
  - 2.4.1 HTTP错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-http
    - 关键词：HTTP错误码
  - 2.4.2 Socket错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-socket
    - 关键词：Socket错误码
  - 2.4.3 webSocket错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-websocket
    - 关键词：webSocket错误码
  - 2.4.4 网络连接管理错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-connection
    - 关键词：网络连接管理错误码
  - 2.4.5 以太网连接错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-ethernet
    - 关键词：以太网连接错误码
  - 2.4.6 扩展认证错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-eap
    - 关键词：扩展认证错误码
  - 2.4.7 网络共享错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-sharing
    - 关键词：网络共享错误码
  - 2.4.8 策略管理错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-policy
    - 关键词：策略管理错误码
  - 2.4.9 MDNS错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-mdns
    - 关键词：MDNS错误码
  - 2.4.10 流量管理错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-statistics
    - 关键词：流量管理错误码
  - 2.4.11 VPN错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-vpn
    - 关键词：VPN错误码
  - 2.4.12 网络安全校验错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-networksecurity
    - 关键词：网络安全校验错误码
  - 2.4.13 内核错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-kernel
    - 关键词：内核错误码
  - 2.4.14 防火墙错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-net-netfirewall
    - 关键词：防火墙错误码

### 最佳实践与FAQ

#### 最佳实践

- 最佳实践入口
  - 3.1 网络连接安全配置：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-network-ca-security
    - 关键词：网络连接安全配置
  - 3.2 多网并发网络加速：
    - https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-path-network-turbo
    - 关键词：多网并发网络加速

#### 常见问题

- FAQ入口
  - 4 Network Kit（网络服务）FAQ：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-kit
    - 关键词：Network Kit（网络服务）

#### 场景排障

- FAQ入口
  - 4.1 http请求中response错误码返回6是什么意思：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-3
    - 关键词：http请求中response错误码返回6是什么意思
  - 4.2 调用camera拍摄的照片如何上传到服务器：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-4
    - 关键词：调用camera拍摄的照片如何上传到服务器
  - 4.3 http网络连接中的通用知识：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-6
    - 关键词：http网络连接中的通用知识
  - 4.4 HTTP接口如何设置Cookie：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-7
    - 关键词：HTTP接口如何设置Cookie
  - 4.5 Stage模型如何配置支持http明文传输：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-16
    - 关键词：Stage模型如何配置支持http明文传输
  - 4.6 Image组件加载网络图片，PixelMap与直接访问url有什么区别：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs-V5/faqs-network-17-V5
    - 关键词：Image组件加载网络图片 / PixelMap与直接访问url有什么区别
  - 4.7 http请求中能否不设置Content-Type参数：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-18
    - 关键词：http请求中能否不设置Content / Type参数
  - 4.8 http请求响应为空，报错请求已被取消或数量超过100：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-22
    - 关键词：http请求响应为空 / 报错请求已被取消或数量超过100
  - 4.9 Socket接口库是否支持绑定域名：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-23
    - 关键词：Socket接口库是否支持绑定域名
  - 4.10 http请求并发的最大数量限制是多少：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-28
    - 关键词：http请求并发的最大数量限制是多少
  - 4.11 http是否支持连接复用：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-30
    - 关键词：http是否支持连接复用
  - 4.12 应用能否指定使用某一网络来发请求：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-32
  - 4.13 网络相关的三方库有哪些：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-34
    - 关键词：网络相关的三方库有哪些
  - 4.14 三方库@ohos/axios中发起post请求，如何以queryParams形式传递参数：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-35
    - 关键词：三方库@ohos / axios中发起post请求 / 如何以queryParams形式传递参数
  - 4.15 ArkTS中HTTP请求如何以JSON形式进行传输：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-36
    - 关键词：ArkTS中HTTP请求如何以JSON形式进行传输
  - 4.16 手机网络正常，但是调用connection.hasDefaultNet()接口失败：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-37
    - 关键词：手机网络正常 / 但是调用connection.hasDefaultNet / 接口失败
  - 4.17 httpRequest.request请求https接口ssl证书验证失败：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-41
    - 关键词：httpRequest.request请求https接口ssl证书验证失败
  - 4.18 如何判断使用的是移动蜂窝网络：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-45
  - 4.19 http请求如何以表单形式进行传输：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-47
    - 关键词：http请求如何以表单形式进行传输
  - 4.20 request和requestInStream的使用边界问题：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-52
    - 关键词：request和requestInStream的使用边界问题
  - 4.21 如何判断当前网络能否上网：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-61
    - 关键词：如何判断当前网络能否上网
  - 4.22 如何监听判断VPN类型网络：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-67
    - 关键词：如何监听判断VPN类型网络
  - 4.23 如何解决应用退至后台TCP连接会被中断：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-73
    - 关键词：如何解决应用退至后台TCP连接会被中断
  - 4.24 网络波动情况下，底层系统是否会关闭Socket连接：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-33
    - 关键词：网络波动情况下 / 底层系统是否会关闭Socket连接
  - 4.25 http请求执行的线程是否可控：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-27
    - 关键词：http请求执行的线程是否可控
  - 4.26 Socket连接报错，错误码88：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-14
    - 关键词：Socket连接报错 / 错误码88
  - 4.27 如何判断当前网络的IP地址版本是多少：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-71
    - 关键词：如何判断当前网络的IP地址版本是多少

## 路由提示

- 问 Network Kit（网络服务） 相关问题时，转到 `network-kit.md`
- 问 Network Kit 相关问题时，转到 `network-kit.md`
- 问 Network Kit术语 相关问题时，转到 `network-kit.md`
- 问 访问网络 相关问题时，转到 `topic-001b0844.md`
- 问 连接网络 相关问题时，转到 `topic-0a6e07c7.md`
- 问 网络 相关问题时，转到 `topic-7ddbe15c.md`
- 问 管理网络 相关问题时，转到 `topic-b366160b.md`
- 问 Network Kit（网络服务）、@ohos.net.connection、网络连接管理、@ohos.net.ethernet、以太网连接管理 时，转到 `api-and-error-codes.md`
- 问 网络连接安全配置、多网并发网络加速、Network Kit（网络服务）、调用camera拍摄的照片如何上传到服务器、http网络连接中的通用知识 时，转到 `best-practices-and-faq.md`
