# 登录信息的cookie应该在什么时机注入

[webview.once](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-f#webviewonce)可以订阅一次指定类型Web事件的回调。一般在web初始化完成后可以注入。



```typescript
1. import { webview } from '@kit.ArkWeb'
2.
3. webview.once("webInited", () => {
4.  console.log("setCookie");
5.  webview.WebCookieManager.configCookie("https://www.example.com", 'a=b,c=d,e=f');
6. })
7.
8. @Entry
9. @Component
10. struct WebComponent {
11.  controller: webview.WebviewController = new webview.WebviewController();
12.
13.  build() {
14.  Column() {
15.  Web({ src: 'www.example.com', controller: this.controller })
16.  }
17.  }
18. }

```


[CookieInject.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/CookieInject.ets#L21-L38)
