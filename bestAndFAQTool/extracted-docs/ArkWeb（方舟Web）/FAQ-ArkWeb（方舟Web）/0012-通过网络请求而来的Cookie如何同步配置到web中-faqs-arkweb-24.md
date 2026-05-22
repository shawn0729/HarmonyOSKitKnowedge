# 通过网络请求而来的Cookie如何同步配置到web中

获取到的cookie利用[Class (WebCookieManager)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager)提供的[configCookieSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookiesync11)方法与[configCookie](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#configcookie11)方法可以实现对Cookie值的同步与异步设置，这样将请求而来的cookie同步到web中。



```typescript
1. import { webview } from '@kit.ArkWeb'
2. @Entry
3. @Component
4. struct WebComponent {
5.  controller: webview.WebviewController = new webview.WebviewController();
6.  headers : Array<webview.WebHeader> = [{ headerKey : "msg",headerValue : 'hello'}];
7.  build() {
8.  Column() {
9.  Button('configCookieSync')
10.  .onClick(() => {
11.  try {
12.  webview.WebCookieManager.configCookieSync('https://www.example.com', 'a=b;c=d;e=f');
13.  } catch (error) {
14.  console.error(`ErrorCode: ${error.code}, Message: ${error.message}`);
15.  }
16.  })
17.  Button('fetchCookieSync')
18.  .onClick(() => {
19.  try {
20.  let value = webview.WebCookieManager.fetchCookieSync('https://www.example.com');
21.  console.log("fetchCookieSync cookie = " + value);
22.  } catch (error) {
23.  console.error(`ErrorCode: ${error.code}, Message: ${error.message}`);
24.  }
25.  })
26.  Column() {
27.  Web({ src: 'www.example.com', controller: this.controller })
28.  .width('100%')
29.  .height('100%')
30.  }
31.  .layoutWeight(1)
32.  }
33.  }
34. }

```


[RequestCookie.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/RequestCookie.ets#L21-L54)
