# 如何获取窗口的宽度

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-200

---

可以通过getWindowProperties接口获取窗口属性。窗口属性的windowRect表示窗口尺寸。参考代码如下：



```typescript
1. import { window } from '@kit.ArkUI';
2.
3. @Entry
4. @Component
5. struct WindowProperties {
6.  context = this.getUIContext();
7.
8.  build() {
9.  Text("Scroll Area")
10.  .width("100%")
11.  .height("100%")
12.  .backgroundColor(0X330000FF)
13.  .fontSize(16)
14.  .textAlign(TextAlign.Center)
15.  .onClick(() => {
16.  window.getLastWindow(this.context.getHostContext()).then((data) => {
17.  // get window attribute
18.  let properties = data?.getWindowProperties();
19.  // Get window width and height
20.  console.log("windowClass width: " + properties.windowRect.width);
21.  console.log("windowClass height: " + properties.windowRect.height);
22.  });
23.  })
24.  }
25. }

```


[WindowProperties.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/WindowProperties.ets#L21-L45)



**参考链接**



[WindowRect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-dialogrequest#windowrect10)
