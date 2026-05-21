# 如何主动清除控件的焦点

---

当组件处于获焦状态时，将其focusable属性或enabled属性设置为false，会自动使该组件失焦。焦点将按照[走焦规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#%E8%B5%B0%E7%84%A6%E8%A7%84%E8%8C%83)转移给其他组件。参考代码如下：



```typescript
1. @Entry
2. @Component
3. struct ClearComponentFocus {
4.  // Whether textInput is focus
5.  @State textFocusable: boolean = true;
6.  @State text: string = 'Gain focus';
7.
8.  build() {
9.  Column() {
10.  TextInput({ text: this.text })
11.  .focusable(this.textFocusable)
12.  .onFocus(() => {
13.  this.text = 'Gain focus';
14.  })
15.  .onBlur(() => {
16.  this.text = 'Lost Focus';
17.  })
18.  Button('Button1')
19.  .width(160)
20.  .height(70)
21.  .margin({ top: 20 })
22.  .onClick(() => {
23.  this.textFocusable = !this.textFocusable;
24.  })
25.  }
26.  .width('100%')
27.  .height('100%')
28.  }
29. }

```


[ProactivelyClearTheFocusOfTheControl.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ProactivelyClearTheFocusOfTheControl.ets#L21-L49)



**参考链接**



[设置组件是否获焦](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event#%E8%AE%BE%E7%BD%AE%E7%BB%84%E4%BB%B6%E6%98%AF%E5%90%A6%E5%8F%AF%E8%8E%B7%E7%84%A6)
