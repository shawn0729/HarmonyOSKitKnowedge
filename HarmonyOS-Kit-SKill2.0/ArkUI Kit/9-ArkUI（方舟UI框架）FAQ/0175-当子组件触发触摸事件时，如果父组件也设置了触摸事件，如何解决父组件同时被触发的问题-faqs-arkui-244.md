# 当子组件触发触摸事件时，如果父组件也设置了触摸事件，如何解决父组件同时被触发的问题

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-244

---

**问题现象**



当子组件触发触摸事件时，如果父组件也设置了触摸事件，父组件同样会触发。



**解决措施**



在onTouch函数中调用event.stopPropagation()可阻止事件冒泡。参考以下代码：



```typescript
1. @Entry
2. @Component
3. struct TouchExample {
4.  @State text: string = 'Parent component'
5.  @State parentComponentResponse: string = 'Response times of parent component'
6.  @State parentComponentResponseNum: number = 0
7.  @State childComponentResponse: string = 'Number of sub component responses'
8.  @State childComponentResponseNum: number = 0
9.
10.  build() {
11.  Column() {
12.  Column(){
13.  Text(this.text).margin({bottom: 20})
14.  Text(this.parentComponentResponse + ':' + `${this.parentComponentResponseNum}`)
15.  Text(this.childComponentResponse + ':' + `${this.childComponentResponseNum}`)
16.
17.  Button('child').height(40).width(100).margin({top: 20})
18.  .onTouch((e) => {
19.  this.childComponentResponseNum ++
20.  e.stopPropagation()
21.  })
22.  }
23.  .onTouch(() => {
24.  this.parentComponentResponseNum ++
25.  })
26.  }.width('100%').padding(30)
27.  }
28. }

```


[ResolveTriggerOfParentComponent.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveTriggerOfParentComponent.ets#L21-L48)



**参考链接**



[触摸事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-events-touch)中的TouchEvent对象说明
