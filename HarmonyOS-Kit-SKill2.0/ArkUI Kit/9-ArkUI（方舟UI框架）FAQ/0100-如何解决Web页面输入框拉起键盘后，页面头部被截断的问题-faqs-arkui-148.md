# 如何解决Web页面输入框拉起键盘后，页面头部被截断的问题

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-148

---

**问题现象**



1. 通过子窗口实现弹窗，弹窗中嵌入Web页面。
2. Web页面中，点击TextInput输入框，键盘弹出。
3. 子窗口上移后，Web页面头部被截断。


**解决措施**



该问题可通过监听软键盘状态解决：软键盘弹出时，将子窗口高度设置为屏幕高度减去软键盘高度；软键盘收起时，子窗口高度设置为屏幕高度。参考代码如下：



```typescript
1. // Sub-window page layout
2. import { webview } from '@kit.ArkWeb';
3. import { window } from '@kit.ArkUI';
4.
5. @Entry
6. @Component
7. export struct SubWindowPage {
8.  @State webViewVisibility: Visibility = Visibility.Visible;
9.  private pageWidth = 320;
10.  private pageHeight = 500;
11.  private controller: webview.WebviewController = new webview.WebviewController();
12.  @State flexAlign: FlexAlign = FlexAlign.Center;
13.  @State screenHeight: number | string = '100%';
14.
15.  aboutToAppear() {
16.  window.getLastWindow(this.getUIContext().getHostContext()).then(currentWindow => {
17.  // Monitor keyboard pop-up and collapse
18.  currentWindow.on('avoidAreaChange', async data => {
19.  let property = currentWindow.getWindowProperties();
20.  let avoidArea = currentWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_KEYBOARD);
21.  this.screenHeight = this.getUIContext().px2vp(property.windowRect.height - avoidArea.bottomRect.height);
22.  });
23.  })
24.  }
25.
26.  build() {
27.  Stack() {
28.  Column() {
29.  Web({ src: $rawfile('index.html'), controller: this.controller })
30.  .javaScriptAccess(true)
31.  .fileAccess(false)
32.  .zoomAccess(false)
33.  .domStorageAccess(true)
34.  .onlineImageAccess(true)
35.  .horizontalScrollBarAccess(false)
36.  .verticalScrollBarAccess(false)
37.  .cacheMode(CacheMode.Online)
38.  .width(this.pageWidth)
39.  .height(this.pageHeight)
40.  .border({ radius: 6 })
41.  .visibility(this.webViewVisibility)
42.  .backgroundColor(Color.Pink)
43.  }
44.  .justifyContent(this.flexAlign)
45.  .alignItems(HorizontalAlign.Center)
46.  .width('100%')
47.  .height('100%')
48.  }
49.  .width('100%')
50.  .height(this.screenHeight)
51.  .backgroundColor('#999955')
52.  .alignContent(Alignment.Center)
53.  }
54. }

```


[TheHeaderTruncated.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TheHeaderTruncated.ets#L21-L74)



**参考链接**



[on('avoidAreaChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#onavoidareachange9)
