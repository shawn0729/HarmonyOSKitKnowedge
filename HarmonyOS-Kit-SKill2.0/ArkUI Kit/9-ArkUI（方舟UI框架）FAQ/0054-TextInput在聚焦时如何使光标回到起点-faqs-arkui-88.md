# TextInput在聚焦时如何使光标回到起点

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-88

---

1. TextInput组件绑定[onEditChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#oneditchange8)事件，该事件可以在TextInput输入状态变化时触发。
2. 在事件回调用TextInputController.[caretPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput#caretposition10)方法设置光标位置，并需要用到setTimeout延迟方法。
  
  
  

```typescript
1. @Entry
2. @Component
3. struct TextInputDemo {
4.  controller: TextInputController = new TextInputController();
5.
6.  build() {
7.  Column() {
8.  TextInput({ controller: this.controller })
9.  .onEditChange((isEditing: boolean) => {
10.  if (isEditing) {
11.  setTimeout(() => {
12.  // The cursor will reset to the beginning of the text after 100ms
13.  this.controller.caretPosition(0);
14.  }, 100)
15.  }
16.  })
17.  }
18.  }
19. }

```
  [ReturnTheCursorToTheStartPoint.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ReturnTheCursorToTheStartPoint.ets#L21-L39)



**参考链接**



[TextInput](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-textinput)
