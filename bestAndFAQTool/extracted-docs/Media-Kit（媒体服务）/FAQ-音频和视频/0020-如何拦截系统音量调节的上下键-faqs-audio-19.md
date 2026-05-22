# 如何拦截系统音量调节的上下键

**问题现象**



在特定业务场景中，开发者需要拦截设备音量调节键的事件上报，以完成业务特定功能，比如阅读场景中，通过按音量上下键实现翻页的功能。



**解决措施**



通过[监听系统的多模态按键事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputconsumer#inputconsumeronkeypressed16)，拦截手机的音量的上下键的系统事件上报，并插入开发者自己的业务逻辑（比如相机拍摄、翻页阅读等功能），具体示例代码如下：



```typescript
1. import { inputConsumer, KeyEvent } from '@kit.InputKit';
2. import { KeyCode } from '@kit.InputKit';
3.
4.
5. @Entry
6. @Component
7. struct TestDemo14 {
8.  private volumeUpCallBackFunc: (event: KeyEvent) => void = () => {
9.  }
10.  private volumeDownCallBackFunc: (event: KeyEvent) => void = () => {
11.  }
12.
13.  aboutToAppear(): void {
14.  try {
15.  let options1: inputConsumer.KeyPressedConfig = {
16.  key: KeyCode.KEYCODE_VOLUME_UP,
17.  action: 1, // 按下按键的行为
18.  isRepeat: false, // 优先消费掉按键事件，不上报
19.  }
20.  let options2: inputConsumer.KeyPressedConfig = {
21.  key: KeyCode.KEYCODE_VOLUME_DOWN,
22.  action: 1, // 按下按键的行为
23.  isRepeat: false, // 优先消费掉按键事件，不上报
24.  }
25.
26.  // 点击了音量按键上事件回调
27.  this.volumeUpCallBackFunc = (event: KeyEvent) => {
28.  this.getUIContext().getPromptAction().showToast({ message: '点击了音量按键上' })
29.  // do something
30.  }
31.
32.  // 点击了音量按键下事件回调
33.  this.volumeDownCallBackFunc = (event: KeyEvent) => {
34.  this.getUIContext().getPromptAction().showToast({ message: '点击了音量按键下' })
35.  // do something
36.  }
37.  // 注册监听事件
38.  inputConsumer.on('keyPressed', options1, this.volumeUpCallBackFunc);
39.  inputConsumer.on('keyPressed', options2, this.volumeDownCallBackFunc);
40.  } catch (error) {
41.  console.error(`Subscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
42.  }
43.  }
44.
45.  build() {
46.  Column() {
47.  Row() {
48.  Button('取消监听音量按键上的监听')
49.  .onClick(() => {
50.  try {
51.  // 取消指定回调函数
52.  inputConsumer.off('keyPressed', this.volumeUpCallBackFunc);
53.  this.getUIContext().getPromptAction().showToast({ message: '取消监听音量按键上的监听事件成功！' })
54.  } catch (error) {
55.  console.error(`Unsubscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
56.  }
57.  })
58.  }.width('100%')
59.  .justifyContent(FlexAlign.Center)
60.  .margin({ top: 20, bottom: 50 })
61.
62.  Row() {
63.  Button('取消监听音量按键下的监听')
64.  .onClick(() => {
65.  try {
66.  // 取消指定回调函数
67.  inputConsumer.off('keyPressed', this.volumeDownCallBackFunc);
68.  this.getUIContext().getPromptAction().showToast({ message: '取消监听音量按键下的监听事件成功！' })
69.  } catch (error) {
70.  console.error(`Unsubscribe execute failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
71.  }
72.  })
73.  }.width('100%')
74.  .justifyContent(FlexAlign.Center)
75.  .margin({ top: 20, bottom: 50 })
76.  Row(){
77.  Text('已默认添加监听音量按键上和下的监听')
78.  }
79.  .width('100%')
80.  .justifyContent(FlexAlign.Center)
81.  }.width('100%').height('100%')
82.  }
83. }

```


[InterceptUpAndDownButtons.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/c3994a1eb136d499712e1b2ff74329da6ddc1851/AudioKit/entry/src/main/ets/pages/InterceptUpAndDownButtons.ets#L20-L102)
