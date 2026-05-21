# 当父组件绑定了onTouch，其子组件Button绑定了onClick，如何做到点击Button只响应Button的onClick，而不用响应父组件的onTouch

---

可以在Button组件中绑定onTouch，并在onTouch中使用stopPropagation()阻止事件冒泡到父组件。参考代码如下：



```less
1. @Entry
2. @Component
3. struct Index {
4.
5.  build() {
6.  Row() {
7.  Button('Click on me')
8.  .width(100)
9.  .backgroundColor('#f00')
10.  .onClick(() => {
11.  console.log('Button onClick');
12.  })
13.  .onTouch((event) => {
14.  console.log('Button onTouch');
15.  event.stopPropagation();
16.  })
17.  }
18.  .onTouch(() => {
19.  console.log('Row onTouch');
20.  })
21.  }
22. }

```


[NotRespondToParentComponentOnTouch.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/NotRespondToParentComponentOnTouch.ets#L21-L42)
