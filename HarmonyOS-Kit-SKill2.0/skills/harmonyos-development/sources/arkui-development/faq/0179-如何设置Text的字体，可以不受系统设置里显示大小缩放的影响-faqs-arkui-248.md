# 如何设置Text的字体，可以不受系统设置里显示大小缩放的影响

---

目前，px2fp()和px2vp()等方法在修改系统显示大小后不会实时更新。字体的默认单位是 fp，界面像素单位是 px，可以使用像素单位来设置字体大小。参考如下：



```less
1. @Entry
2. @Component
3. struct CustomFontSetting {
4.  @State message: string = 'hello world';
5.
6.  build() {
7.  Column() {
8.  Text(this.message)
9.  .fontSize(53) // Default unit is fp, which changes with system display size.
10.  Text(this.message)
11.  .fontSize(this.getUIContext().fp2px(160) + 'px') // Use pixel units, unaffected by system display size.
12.  Blank()
13.  .color(0xff0000)
14.  .height(30)
15.  .width(226)
16.  .margin({ bottom: 20 }) // Default unit vp changes with system display size.
17.  Blank()
18.  .color(0xff0000)
19.  .height(30 + 'px')
20.  .width(this.getUIContext().vp2px(672) + 'px') // Use pixel units, unaffected by system display size.
21.  }
22.  }
23. }

```


[FontSetting.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/FontSetting.ets#L21-L44)
