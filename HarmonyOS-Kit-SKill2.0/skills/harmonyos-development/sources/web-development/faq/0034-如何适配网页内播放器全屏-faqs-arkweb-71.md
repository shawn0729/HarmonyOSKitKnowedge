# 如何适配网页内播放器全屏

在工程中的module.json5配置文件中添加网络访问权限ohos.permission.INTERNET。



具体实现可参考如下代码



```typescript
1. import { mediaquery, window } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';
3. import { webview } from '@kit.ArkWeb';
4.
5. @Entry
6. @Component
7. struct WebPlayerFullScreen {
8.  @State color: string = '#DB7093';
9.  @State text: string = 'Portrait';
10.  @State portraitFunc: mediaquery.MediaQueryResult | void | null = null;
11.  // Full-screen exit processor, used to control the exit in full-screen state
12.  handler: FullScreenExitHandler | null = null;
13.  // The condition is met when the device is in landscape mode
14.  listener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)');
15.  controller: webview.WebviewController = new webview.WebviewController();
16.
17.  onPortrait(mediaQueryResult: mediaquery.MediaQueryResult) {
18.  // If the device is in landscape mode, change the corresponding page layout
19.  if (mediaQueryResult.matches as boolean) {
20.  this.color = '#FFD700';
21.  this.text = 'Landscape';
22.  } else {
23.  this.color = '#DB7093';
24.  this.text = 'Portrait';
25.  }
26.  }
27.
28.  aboutToAppear() {
29.  // Bind the current application instance
30.  // Bind callback function
31.  this.listener.on('change', (mediaQueryResult: mediaquery.MediaQueryResult) => {
32.  this.onPortrait(mediaQueryResult);
33.  });
34.  }
35.
36.  // Change the horizontal and vertical screen status function of the device
37.  private changeOrientation(isLandscape: boolean) {
38.  // Retrieve contextual information for UIAbility instances
39.  let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
40.  // Call this interface to manually change the device's horizontal and vertical screen status
41.  window.getLastWindow(context).then((lastWindow) => {
42.  lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT);
43.  });
44.  }
45.
46.  build() {
47.  Column() {
48.  Web({ src: 'https://developer.huawei.com/consumer/cn/design/', controller: this.controller })
49.  .javaScriptAccess(true)
50.  .domStorageAccess(true)
51.  .onFullScreenEnter((event) => {
52.  this.handler = event.handler;
53.  this.changeOrientation(true);
54.  })
55.  .onFullScreenExit(() => {
56.  if (this.handler) {
57.  this.handler.exitFullScreen();
58.  this.changeOrientation(false);
59.  }
60.  })
61.  }
62.  .width('100%')
63.  .height('100%')
64.  }
65. }

```


[FullscreenPlayerSupport.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkWebKit/entry/src/main/ets/pages/FullscreenPlayerSupport.ets#L21-L85)
