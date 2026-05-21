# 如何解决点击子组件模块区域会触发父组件的点击事件问题

---

**问题现象**



当enabled的值为false时，点击Button按钮会触发父组件的点击事件。



**解决措施**



将Button组件包裹在容器组件中，并设置hitTestBehavior属性为[HitTestMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#hittestmode9).Block，以阻止事件冒泡。具体代码如下：



```typescript
1. @Entry
2. @Component
3. struct TouchExample {
4.  @State text: string = 'Parent component'
5.  @State parentComponentResponse: string = 'Response times of parent component'
6.  @State parentComponentResponseNum: number = 0
7.
8.  build() {
9.  Column() {
10.  Column(){
11.  Text(this.text).margin({bottom: 20})
12.  Text(this.parentComponentResponse + ':' + `${this.parentComponentResponseNum}`)
13.  Row(){
14.  //Wrap a container component around the Button component and set the hitTestBehavior property to HitTestMode.Block, which can prevent event bubbling.
15.  Button('Disable sub components').height(40).width(100).margin({top: 20})
16.  }
17.  .hitTestBehavior(HitTestMode.Block)
18.  }.onClick((e) => {
19.  this.parentComponentResponseNum ++;
20.  })
21.  .width('80%')
22.  .height('30%')
23.  .backgroundColor(Color.Gray)
24.  }
25.  .width('100%')
26.  .padding(30)
27.  }
28. }

```


[ResolveTriggerParentComponentClickEvent.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveTriggerParentComponentClickEvent.ets#L21-L48)



**参考链接**



[触摸测试控制](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior)
