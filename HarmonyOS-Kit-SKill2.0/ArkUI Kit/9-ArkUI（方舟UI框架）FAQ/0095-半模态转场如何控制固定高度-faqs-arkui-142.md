# 半模态转场如何控制固定高度

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-142

---

通过设置bindSheet()的参数options对高度进行控制。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct SheetTransitionExample {
4.  @State isShow: boolean = false;
5.  @State sheetHeight: number = 300;
6.
7.  @Builder
8.  myBuilder() {
9.  Column() {
10.  Button('change height')
11.  .margin(10)
12.  .fontSize(20)
13.  .onClick(() => {
14.  this.sheetHeight = 500;
15.  })
16.
17.  Button('Set Illegal height')
18.  .margin(10)
19.  .fontSize(20)
20.  .onClick(() => {
21.  this.sheetHeight = 0;
22.  })
23.  }
24.  .width('100%')
25.  .height('100%')
26.  }
27.
28.  build() {
29.  Column() {
30.  Button('transition modal 1')
31.  .onClick(() => {
32.  this.isShow = true;
33.  })
34.  .fontSize(20)
35.  .margin(10)
36.  .bindSheet(this.isShow, this.myBuilder(), { height: this.sheetHeight, backgroundColor: Color.Green })
37.  }
38.  .justifyContent(FlexAlign.Center)
39.  .width('100%')
40.  .height('100%')
41.  }
42. }

```


[SemiModalControlWithFixedHeight.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SemiModalControlWithFixedHeight.ets#L21-L62)



**参考链接**



[半模态转场](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition)
