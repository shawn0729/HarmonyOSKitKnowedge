# 多个Cookie如何进行批量设置

[Class (WebCookieManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager)提供了[configCookieSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookiesync11)方法与[configCookie](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookie11)方法，用于同步和异步设置 Cookie。目前，接口不支持一次性批量设置多个 Cookie，建议通过多次调用 `configCookie` 或 `configCookieSync` 方法来实现多个 Cookie 的设置。



```typescript
1. import { webview } from '@kit.ArkWeb';
2.
3. webview.once("webInited", () => {
4.  console.info("webInited setCookie");
5.  webview.WebCookieManager.configCookie("https://www.example.com", 'a=b');
6.  webview.WebCookieManager.configCookie("https://www.example.com", 'c=d');
7.  webview.WebCookieManager.configCookie("https://www.example.com", 'e=f');
8. })
9.
10. @Entry
11. @Component
12. struct LoginCookieConfig {
13.  controller: webview.WebviewController = new webview.WebviewController();
14.
15.  build() {
16.  Column() {
17.  Button('fetchCookieSync')
18.  .onClick(() => {
19.  try {
20.  let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
21.  console.log(`fetchCookieSync cookie value is: ${value}`);
22.  } catch (error) {
23.  console.error(`fetchCookieSync failed,error is: ${JSON.stringify(error)}`);
24.  }
25.  })
26.  Web({ src: 'www.example.com', controller: this.controller })
27.  }
28.  }
29. }

```


[LoginCookieConfig.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/LoginCookieConfig.ets#L21-L49)
