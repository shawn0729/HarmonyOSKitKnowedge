# 如何实现软键盘弹出后，整体布局不变

---

通过[expandSafeArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea)属性把组件扩展其安全区域，使页面整体布局保持不变，当type为SafeAreaType.KEYBOARD时默认生效，组件不避让键盘。可参考如下代码：



```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextInputExample {
5.  scroller: Scroller = new Scroller();
6.  @State text: string = '';
7.
8.  build() {
9.  Scroll(this.scroller) {
10.  Column({ space: 20 }) {
11.  TextInput({ placeholder: 'Please enter the content.' })
12.  .expandSafeArea([SafeAreaType.KEYBOARD])
13.  .type(InputType.Password)
14.  .margin({ top: 200 })
15.  TextInput({ placeholder: 'Please enter the content.' })
16.  .expandSafeArea([SafeAreaType.KEYBOARD])
17.  .margin({ top: 200 })
18.  Text(`UserName：${this.text}`)
19.  .expandSafeArea([SafeAreaType.KEYBOARD])
20.  .width('80%')
21.  .margin({ top: 200 })
22.  TextInput({ placeholder: 'Please enter a user name.', text: this.text })
23.  .expandSafeArea([SafeAreaType.KEYBOARD])
24.  .margin({ top: 200 })
25.  .onChange((value: string) => {
26.  this.text = value;
27.  })
28.  }
29.  .width('100%')
30.  }
31.  .scrollBar(BarState.Off)
32.  }
33. }

```


[SoftKeyboardPopsUp.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SoftKeyboardPopsUp.ets#L21-L53)
