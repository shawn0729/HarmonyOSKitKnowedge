# 返回的html里包含数学公式，怎么合理渲染到页面

HarmonyOS目前没有提供专门的数学公式渲染组件，可以使用WebView组件来加载支持数学公式渲染的网页。



示例代码如下：



```typescript
1. import { webview } from "@kit.ArkWeb"
2.
3. @Component
4. export struct CourseLearning {
5.  private webviewController: webview.WebviewController = new webview.WebviewController();
6.
7.  build() {
8.  Column() {
9.  Web({ src: $rawfile('Mathematics.html'), controller: this.webviewController })
10.  .domStorageAccess(true)
11.  .javaScriptAccess(true)
12.  }
13.  }
14. }

```


[CourseLearning.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkWebKit/entry/src/main/ets/pages/CourseLearning.ets#L18-L31)



示例代码中提供的html可参考[Mathematics.html](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/b39fe4e5abece291bdac1b844563003b397ce87d/ArkWebKit/entry/src/main/resources/rawfile/Mathematics.html)。
