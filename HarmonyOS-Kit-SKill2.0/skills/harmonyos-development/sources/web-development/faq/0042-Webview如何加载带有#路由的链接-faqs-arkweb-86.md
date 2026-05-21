# Webview如何加载带有#路由的链接

Web组件的src使用'resource://rawfile/LoadWebLink.html#AAA'这种格式进行加载，具体可参考如下代码：



```typescript
1. import { webview } from '@kit.ArkWeb';
2.
3. @Entry
4. @Component
5. struct LoadWebLink {
6.  controller: webview.WebviewController = new webview.WebviewController();
7.
8.  build() {
9.  RelativeContainer() {
10.  Web({ src: 'resource://rawfile/LoadWebLink.html#AAA', controller: this.controller })
11.  }
12.  .height('100%')
13.  .width('100%')
14.  }
15. }

```


[RouteLink.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/RouteLink.ets#L21-L35)
