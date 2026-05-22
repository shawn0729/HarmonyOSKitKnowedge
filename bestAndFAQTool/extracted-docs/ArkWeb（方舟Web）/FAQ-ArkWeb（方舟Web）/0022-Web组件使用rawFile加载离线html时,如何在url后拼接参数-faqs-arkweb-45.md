# Web组件使用rawFile加载离线html时,如何在url后拼接参数

使用Web组件加载时，可直接在URL中拼接参数。加载后，H5侧获取并使用这些参数。



**参考代码**



通过Web组件使用rawFile加载离线HTML，URL中包含参数。



```typescript
1. import { webview } from '@kit.ArkWeb'
2.
3. @Entry
4. @Component
5. struct WebComponent {
6.  controller: webview.WebviewController = new webview.WebviewController()
7.
8.  build() {
9.  Column() {
10.  Web({ src: 'resource://rawfile/LoadingURLTransferParameters.html?key=value', controller: this.controller })
11.  .javaScriptAccess(true)
12.  .domStorageAccess(true)
13.  }
14.  .width('100%')
15.  .height('100%')
16.  }
17. }

```


[UrlAdd.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/UrlAdd.ets#L21-L37)



H5侧通过以下方式获取URL中的参数并使用。



```xml
1. <!DOCTYPE html>
2. <html>
3. <head>
4.  <title>Parameter-based HTML</title>
5. </head>
6. <body>
7. <h1>Welcome!</h1>
8. <h1 id="params"></h1>
9.
10. <script>
11.  function getParams() {
12.  var params = {};
13.  window.location.search.substring(1).split('&').forEach(function(param) {
14.  var pair = param.split('=');
15.  params[pair[0]] = decodeURIComponent(pair[1]);
16.  });
17.  return params;
18.  }
19.  document.getElementById('params').innerHTML = JSON.stringify(getParams());
20. </script>
21. </body>
22. </html>

```


[LoadingURLTransferParameters.html](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/resources/rawfile/LoadingURLTransferParameters.html#L7-L28)
