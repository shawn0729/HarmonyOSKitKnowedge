# 如何实现类似keyframes的效果

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-157

---

可以通过设置动画的延迟播放时间（delay）或在onFinish回调中启动新动画来实现类似效果。参考代码如下：



```cangjie
1. @Entry
2. @Component
3. struct AnimateToExample {
4.  @State widthSize: number = 250;
5.  @State heightSize: number = 100;
6.  @State rotateAngle: number = 0;
7.  private flag: boolean = true;
8.  @State opacityValue: number = 1;
9.
10.  build() {
11.  Column() {
12.  Button('change size')
13.  .width(this.widthSize)
14.  .height(this.heightSize)
15.  .margin(30)
16.  .opacity(this.opacityValue)
17.  .onClick(() => {
18.  if (this.flag) {
19.  // Implement multi-stage animations by animateTo
20.  this.getUIContext().animateTo({
21.  duration: 2000,
22.  curve: Curve.EaseOut,
23.  iterations: 1,
24.  playMode: PlayMode.Normal,
25.  onFinish: () => {
26.  this.getUIContext().animateTo({
27.  duration: 2000,
28.  curve: Curve.EaseOut,
29.  iterations: 1,
30.  playMode: PlayMode.Normal,
31.  onFinish: () => {
32.  }
33.  }, () => {
34.  // Second stage, opacityValue becomes 0.2
35.  this.opacityValue = 0.2;
36.  })
37.  }
38.  }, () => {
39.  // First stage, opacityValue becomes 0.5
40.  this.opacityValue = 0.5;
41.  })
42.  }
43.  })
44.  }.width('100%').margin({ top: 5 })
45.  }
46. }

```


[SimilarKeyFramesEffect.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SimilarKeyFramesEffect.ets#L21-L66)



**参考链接**



[显式动画 (animateTo)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-explicit-animation)
