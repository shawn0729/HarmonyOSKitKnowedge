# 如何通过PanGesture手势或者SwipeGesture手势实现自定义组件的惯性滚动效果

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-33

---

可以通过PanGesture绑定滑动手势事件，并使用[onActionEnd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-gestures-pangesture#%E4%BA%8B%E4%BB%B6)回调里的[velocityY](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-common#gestureevent%E5%AF%B9%E8%B1%A1%E8%AF%B4%E6%98%8E)字段生成离手惯性滚动动画。示例如下，具体滚动的速率可以通过调整参数达到预期效果。



```typescript
1. @Entry
2. @Component
3. struct PanGestureExample {
4.  @State offsetX: number = 0;
5.  @State offsetY: number = 0;
6.  @State positionX: number = 0;
7.  @State positionY: number = 0;
8.  private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Up | PanDirection.Down });
9.
10.  build() {
11.  Column() {
12.  Text('PanGesture offset: \nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
13.  }
14.  .height(200)
15.  .width(200)
16.  .padding(20)
17.  .border({ width: 3 })
18.  .margin(30)
19.  // 以组件左上角为坐标原点进行移动
20.  .translate({
21.  x: this.offsetX,
22.  y: this.offsetY,
23.  z: 0
24.  })
25.  .gesture(
26.  // 拖动
27.  PanGesture(this.panOption)
28.  .onActionStart((event?: GestureEvent) => {
29.  console.info('Pan start');
30.  })
31.  .onActionUpdate((event?: GestureEvent) => {
32.  if (event) {
33.  // 最后的位置加上偏移量
34.  this.offsetX = this.positionX + event.offsetX;
35.  this.offsetY = this.positionY + event.offsetY;
36.  }
37.  })
38.  .onActionEnd((event) => {
39.  this.offsetX = this.positionX + event.offsetX;
40.  this.offsetY = this.positionY + event.offsetY;
41.  this.positionX = this.positionX + event.offsetX;
42.  this.positionY = this.positionY + event.offsetY;
43.  let ySpeed = event.velocityY;
44.  this.getUIContext().animateTo({
45.  duration: 1000,
46.  curve: Curve.LinearOutSlowIn,
47.  iterations: 1,
48.  playMode: PlayMode.Normal,
49.  onFinish: () => {
50.  console.info('play end');
51.  }
52.  }, () => {
53.  this.offsetY = this.offsetY + ySpeed * 0.2;
54.  this.positionY = this.positionY + ySpeed * 0.2;
55.  })
56.  })
57.  )
58.  }
59. }

```


[InertialRolling.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/4d38726fbc68dda953def7ce5ff601f3254ee760/ArkUI/entry/src/main/ets/pages/InertialRolling.ets#L21-L79)
