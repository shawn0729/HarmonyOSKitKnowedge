# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 ArkWeb API 参考入口时，读取本文件。

## API 总入口

- 2 ArkWeb（方舟Web）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkweb-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkweb-arkts
- 2.3 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkweb-c

## 主题到 API 的映射规则

### Webview 相关接口

- ArkTS API
  - 2.1.1 @ohos.web.webview (Webview)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-webview

### AdsBlockManager 相关接口

- ArkTS API
  - 2.1.1.3 Class (AdsBlockManager)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-adsblockmanager

### BackForwardCacheOptions 相关接口

- ArkTS API
  - 2.1.1.4 Class (BackForwardCacheOptions)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardcacheoptions

### BackForwardCacheSupportedFeatures 相关接口

- 通用入口
  - 2.1.1.5 Class (BackForwardCacheSupportedFeatures)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kts-apis-webview-backforwardcachesupportedfeatures

### GeolocationPermissions 相关接口

- ArkTS API
  - 2.1.1.6 Class (GeolocationPermissions)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions

### JsMessageExt 相关接口

- ArkTS API
  - 2.1.1.7 Class (JsMessageExt)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-jsmessageext

### 图片解码与图片源

- 通用入口
  - 2.2.1.23 Class (WebResourceRequest)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourcerequest
  - 2.2.1.24 Class (WebResourceResponse)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceresponse

- ArkTS API
  - 2.1.1.8 Class (MediaSourceInfo)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-mediasourceinfo
  - 2.1.1.23 Class (WebResourceHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webresourcehandler

- C API
  - 2.3.3.4 ArkWeb_ResourceHandler_：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-resourcehandler
  - 2.3.3.6 ArkWeb_ResourceRequest_：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-resourcerequest

### NativeMediaPlayerSurfaceInfo 相关接口

- ArkTS API
  - 2.1.1.9 Class (NativeMediaPlayerSurfaceInfo)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayersurfaceinfo

### PdfData 相关接口

- ArkTS API
  - 2.1.1.10 Class (PdfData)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-pdfdata

### ProxyConfig 相关接口

- ArkTS API
  - 2.1.1.11 Class (ProxyConfig)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyconfig

### PrefetchOptions 相关接口

- ArkTS API
  - 2.1.1.12 Class (PrefetchOptions)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-prefetchoptions

### ProxyController 相关接口

- ArkTS API
  - 2.1.1.13 Class (ProxyController)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxycontroller

### ProxyRule 相关接口

- ArkTS API
  - 2.1.1.14 Class (ProxyRule)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyrule

### WebviewController 相关接口

- ArkTS API
  - 2.1.1.15 Class (WebviewController)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller

### WebCookieManager 相关接口

- ArkTS API
  - 2.1.1.16 Class (WebCookieManager)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager

### WebDataBase 相关接口

- ArkTS API
  - 2.1.1.17 Class (WebDataBase)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdatabase

### WebDownloadDelegate 相关接口

- ArkTS API
  - 2.1.1.18 Class (WebDownloadDelegate)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloaddelegate

### WebDownloadItem 相关接口

- ArkTS API
  - 2.1.1.19 Class (WebDownloadItem)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloaditem

### WebDownloadManager 相关接口

- ArkTS API
  - 2.1.1.20 Class (WebDownloadManager)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webdownloadmanager

### WebHttpBodyStream 相关接口

- ArkTS API
  - 2.1.1.21 Class (WebHttpBodyStream)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream

### WebMessageExt 相关接口

- ArkTS API
  - 2.1.1.22 Class (WebMessageExt)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageext

### WebSchemeHandler 相关接口

- ArkTS API
  - 2.1.1.24 Class (WebSchemeHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler

### WebSchemeHandlerRequest 相关接口

- ArkTS API
  - 2.1.1.25 Class (WebSchemeHandlerRequest)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerrequest

### WebSchemeHandlerResponse 相关接口

- ArkTS API
  - 2.1.1.26 Class (WebSchemeHandlerResponse)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerresponse

### WebStorage 相关接口

- ArkTS API
  - 2.1.1.27 Class (WebStorage)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webstorage

### VerifyPinHandler 相关接口

- 通用入口
  - 2.1.1.28 Class (VerifyPinHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-verifypinhandler

### BackForwardList 相关接口

- ArkTS API
  - 2.1.1.29 Interface (BackForwardList)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardlist

### NativeMediaPlayerBridge 相关接口

- ArkTS API
  - 2.1.1.30 Interface (NativeMediaPlayerBridge)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayerbridge

### NativeMediaPlayerHandler 相关接口

- ArkTS API
  - 2.1.1.31 Interface (NativeMediaPlayerHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayerhandler

### WebMessagePort 相关接口

- ArkTS API
  - 2.1.1.32 Interface (WebMessagePort)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webmessageport

### 错误码与异常定位

- 通用入口
  - 2.2.1.17 Class (SslErrorHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-sslerrorhandler
  - 2.2.1.22 Class (WebResourceError)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceerror
  - 2.4 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkweb-arkts-errcode
  - 2.4.1 Webview错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-webview

- ArkTS API
  - 2.1.2 @ohos.web.netErrorList (ArkWeb网络协议栈错误列表)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-neterrorlist

### Web Native Messaging Extension Ability 相关接口

- ArkTS API
  - 2.1.3 @ohos.web.WebNativeMessagingExtensionAbility (Web Native Messaging Extension Ability)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionability

### Web Native Messaging Extension Context 相关接口

- ArkTS API
  - 2.1.4 @ohos.web.WebNativeMessagingExtensionContext (Web Native Messaging Extension Context)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensioncontext

### Web Native Messaging Extension Manager 相关接口

- ArkTS API
  - 2.1.5 @ohos.web.webNativeMessagingExtensionManager (Web Native Messaging Extension Manager)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-web-webnativemessagingextensionmanager

### ArkTS 组件 相关接口

- 通用入口
  - 2.2 ArkTS 组件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkweb-comp

### Web 相关接口

- 通用入口
  - 2.2.1 Web：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-web

- C API
  - 2.3.1.1 Web：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web

### 组件描述 相关接口

- 通用入口
  - 2.2.1.1 组件描述：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web

### 属性 相关接口

- 通用入口
  - 2.2.1.2 属性：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes

### 事件 相关接口

- 通用入口
  - 2.2.1.3 事件：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events

### ClientAuthenticationHandler 相关接口

- 通用入口
  - 2.2.1.4 Class (ClientAuthenticationHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-basic-components-web-clientauthenticationhandler

### ConsoleMessage 相关接口

- 通用入口
  - 2.2.1.5 Class (ConsoleMessage)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-consolemessage

### ControllerHandler 相关接口

- 通用入口
  - 2.2.1.6 Class (ControllerHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-controllerhandler

### DataResubmissionHandler 相关接口

- 通用入口
  - 2.2.1.7 Class (DataResubmissionHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-dataresubmissionhandler

### EventResult 相关接口

- 通用入口
  - 2.2.1.8 Class (EventResult)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-eventresult

### FileSelectorParam 相关接口

- 通用入口
  - 2.2.1.9 Class (FileSelectorParam)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorparam

### FileSelectorResult 相关接口

- 通用入口
  - 2.2.1.10 Class (FileSelectorResult)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorresult

### FullScreenExitHandler 相关接口

- 通用入口
  - 2.2.1.11 Class (FullScreenExitHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fullscreenexithandler

### HttpAuthHandler 相关接口

- 通用入口
  - 2.2.1.12 Class (HttpAuthHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-httpauthhandler

### JsGeolocation 相关接口

- 通用入口
  - 2.2.1.13 Class (JsGeolocation)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsgeolocation

### JsResult 相关接口

- 通用入口
  - 2.2.1.14 Class (JsResult)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsresult

### PermissionRequest 相关接口

- 通用入口
  - 2.2.1.15 Class (PermissionRequest)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-permissionrequest

### ScreenCaptureHandler 相关接口

- 通用入口
  - 2.2.1.16 Class (ScreenCaptureHandler)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-screencapturehandler

### WebContextMenuParam 相关接口

- 通用入口
  - 2.2.1.18 Class (WebContextMenuParam)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuparam

### WebContextMenuResult 相关接口

- 通用入口
  - 2.2.1.19 Class (WebContextMenuResult)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuresult

### WebCookie 相关接口

- 通用入口
  - 2.2.1.20 Class (WebCookie)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcookie

### WebKeyboardController 相关接口

- 通用入口
  - 2.2.1.21 Class (WebKeyboardController)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webkeyboardcontroller

### Interfaces（其他） 相关接口

- 通用入口
  - 2.2.1.25 Interfaces（其他）：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i

### WebController 相关接口

- 通用入口
  - 2.2.1.28 Class (WebController)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontroller

### ArkWeb_SchemeHandler_ 相关接口

- C API
  - 2.3.3.3 ArkWeb_SchemeHandler_：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-schemehandler

### ArkWeb_Response_ 相关接口

- C API
  - 2.3.3.5 ArkWeb_Response_：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-response

### ArkWeb_RequestHeaderList_ 相关接口

- C API
  - 2.3.3.7 ArkWeb_RequestHeaderList_：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-requestheaderlist

### ArkWeb_HttpBodyStream_ 相关接口

- C API
  - 2.3.3.8 ArkWeb_HttpBodyStream_：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-httpbodystream

### ArkWeb_WebMessage* 相关接口

- C API
  - 2.3.3.10 ArkWeb_WebMessage*：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessage8h

### ArkWeb_JavaScriptValue* 相关接口

- C API
  - 2.3.3.11 ArkWeb_JavaScriptValue*：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-javascriptvalue8h

### ArkWeb_WebMessagePort* 相关接口

- C API
  - 2.3.3.12 ArkWeb_WebMessagePort*：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-webmessageport8h

## 直接映射

- `Webview`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-webview
- `AdsBlockManager`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-adsblockmanager
- `BackForwardCacheOptions`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardcacheoptions
- `BackForwardCacheSupportedFeatures`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kts-apis-webview-backforwardcachesupportedfeatures
- `GeolocationPermissions`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions
- `JsMessageExt`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-jsmessageext
- `MediaSourceInfo`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-mediasourceinfo
- `NativeMediaPlayerSurfaceInfo`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayersurfaceinfo
- `PdfData`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-pdfdata
- `ProxyConfig`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxyconfig
- `PrefetchOptions`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-prefetchoptions
- `ProxyController`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-proxycontroller

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 ArkWeb（方舟Web）、@ohos.web.webview、Webview、Class、AdsBlockManager 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
