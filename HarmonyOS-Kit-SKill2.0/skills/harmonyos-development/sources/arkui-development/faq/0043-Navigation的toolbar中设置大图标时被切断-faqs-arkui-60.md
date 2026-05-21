# Navigation的toolbar中设置大图标时被切断

---

当图片尺寸超过toolbar高度时，可通过scale属性进行缩放调整。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct NavigationExample {
4.  build() {
5.  Column() {
6.  Navigation() {
7.  }.toolbarConfiguration(this.navigationToolbar)
8.  }
9.  .height('100%')
10.  .width('100%')
11.  .backgroundColor(Color.Gray)
12.  }
13.
14.  @Builder
15.  navigationToolbar() {
16.  Row() {
17.  Column() {
18.  Image($r('app.media.icon')).width(24)
19.  }.layoutWeight(1)
20.
21.  Column() {
22.  Image($r('app.media.icon')).width(24).scale({ x: 2, y: 2 })
23.  }.layoutWeight(1)
24.
25.  Column() {
26.  Image($r('app.media.icon')).width(24)
27.  }.layoutWeight(1)
28.  }
29.  .height(34)
30.  .width('100%').backgroundColor(Color.White)
31.  }
32. }

```


[CutOffWhenSettingLargeIcon.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CutOffWhenSettingLargeIcon.ets#L21-L52)



**参考链接**



[图形变换](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-transformation)
