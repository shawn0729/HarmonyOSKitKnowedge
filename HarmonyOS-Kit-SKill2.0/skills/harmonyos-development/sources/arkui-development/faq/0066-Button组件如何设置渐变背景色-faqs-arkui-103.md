# Button组件如何设置渐变背景色

---

将Button的默认背景色设置为全透明，以确保渐变颜色正常显示。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct Index {
4.  build() {
5.  Button('test')
6.  .width(200)
7.  .height(50)
8.  .backgroundColor('#00000000')
9.  .linearGradient({
10.  angle: 90,
11.  colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
12.  })
13.  }
14. }

```


[ButtonSetGradientBackgroundColor.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ButtonSetGradientBackgroundColor.ets#L21-L34)



**参考链接**



[Button](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-button)
