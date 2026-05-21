# 如何解决子组件全屏后margin不会生效的问题

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-32

---

父组件全屏显示，子组件默认撑满。设置左右margin值后，子组件可能会超出屏幕范围。可以使用`constraintSize`属性限制子组件的最大宽高。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct Index {
4.  @State message: string = 'Hello World';
5.
6.  build() {
7.  Row() {
8.  Column() {
9.  Text(this.message)
10.  .fontSize(50)
11.  .fontWeight(FontWeight.Bold)
12.  .textAlign(TextAlign.Center)
13.  .width('100%')
14.  .constraintSize({ maxWidth: '100%' })
15.  .backgroundColor(Color.Blue)
16.  .margin({ left: 50, right: 50 })
17.  }
18.  .width('100%')
19.  }
20.  .height('100%')
21.  }
22. }

```


[ResolveFullScreenNonEffectiveness.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveFullScreenNonEffectiveness.ets#L21-L42)



**参考链接**



[尺寸设置](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size)中的constraintSize
