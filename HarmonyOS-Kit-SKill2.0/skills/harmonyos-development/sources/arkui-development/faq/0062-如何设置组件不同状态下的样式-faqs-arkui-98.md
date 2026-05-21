# 如何设置组件不同状态下的样式

---

使用多态样式，在组件的StateStyles接口中，定义组件不同状态下的样式。参考代码如下：



```typescript
1. @Component
2. struct PolymorphicStyle {
3.  @Styles
4.  pressedStyles() {
5.  .backgroundColor('#ED6F21')
6.  .borderRadius(10)
7.  .borderStyle(BorderStyle.Dashed)
8.  .borderWidth(2)
9.  .borderColor('#33000000')
10.  .width(120)
11.  .height(30)
12.  .opacity(1)
13.  }
14.
15.
16.  build() {
17.  Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
18.  Text('pressed')
19.  .backgroundColor('#0A59F7')
20.  .borderRadius(20)
21.  .borderStyle(BorderStyle.Dotted)
22.  .borderWidth(2)
23.  .borderColor(Color.Red)
24.  .width(100)
25.  .height(25)
26.  .opacity(1)
27.  .fontSize(14)
28.  .fontColor(Color.White)
29.  .stateStyles({
30.  pressed: this.pressedStyles
31.  })
32.  .margin({ bottom: 20 })
33.  .textAlign(TextAlign.Center)
34.  }
35.  .width(350)
36.  .height(300)
37.  }
38. }

```


[SetStylesForComponentsInDifferentStates.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SetStylesForComponentsInDifferentStates.ets#L21-L58)



**参考链接**



[多态样式](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-polymorphic-style)
