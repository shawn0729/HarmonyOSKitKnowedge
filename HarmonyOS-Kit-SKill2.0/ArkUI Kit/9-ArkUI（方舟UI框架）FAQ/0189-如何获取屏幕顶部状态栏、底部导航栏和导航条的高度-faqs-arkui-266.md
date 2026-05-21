# 如何获取屏幕顶部状态栏、底部导航栏和导航条的高度

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-266

---

可以使用window的[getWindowAvoidArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-uiextension#getwindowavoidarea)方法获取，示例代码如下：



```typescript
1. import { window } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3.
4. @Entry
5. @Component
6. struct GetAvoidAreaHeight {
7.  context = this.getUIContext();
8.
9.  build() {
10.  Column() {
11.  Button('GetAvoidAreaHeight')
12.  .onClick(() => {
13.  let systemAvoidAreaType = window.AvoidAreaType.TYPE_SYSTEM; // system
14.  let navigationIndicatorType = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // navigation
15.  if (this.context) {
16.  window.getLastWindow(this.context.getHostContext()).then((data) => {
17.  // Get the system default area, usually including the status bar and navigation bar
18.  let avoidArea1 = data.getWindowAvoidArea(systemAvoidAreaType);
19.  // Top status bar height
20.  let statusBarHeight = avoidArea1.topRect.height;
21.  // Bottom navigation bar height
22.  let bottomNavHeight = avoidArea1.bottomRect.height;
23.  // Get the navigation bar area
24.  let avoidArea2 = data.getWindowAvoidArea(navigationIndicatorType);
25.  // Get the height of the navigation bar area
26.  let indicatorHeight = avoidArea2.bottomRect.height;
27.  console.info(`statusBarHeight is ${statusBarHeight}`);
28.  console.info(`bottomNavHeight is ${bottomNavHeight}`);
29.  console.info(`indicatorHeight is ${indicatorHeight}`);
30.  }).catch((err: BusinessError) => {
31.  console.error(`Failed to obtain the window. Cause: ${JSON.stringify(err)}`);
32.  });
33.  }
34.  })
35.  }
36.  }
37. }

```


[AvoidAreaHeight.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/AvoidAreaHeight.ets#L21-L58)
