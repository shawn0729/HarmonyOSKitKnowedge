# 使用BuilderParam在父组件调用this的方法报错：Error message: undefined is not callable

---

**问题场景**



在子组件Child中使用@BuilderParam参数时，如果在父组件中将父组件的builder函数传递给子组件，并在builder函数中调用父组件的方法，可能会出现Error message: undefined is not callable的错误。



问题代码如下：



```typescript
1. @Component
2. struct Child {
3.  @Builder
4.  FunABuilder0() {};
5.
6.  @BuilderParam aBuilder0: () => void = this.FunABuilder0;
7.
8.  build() {
9.  Column() {
10.  this.aBuilder0()
11.  }
12.  }
13. }
14.
15. @Entry
16. @Component
17. struct Parent {
18.  @Builder
19.  componentBuilder() {
20.  Text('Parent builder')
21.  .onClick(() => {
22.  this.test1();
23.  })
24.  }
25.
26.  test1(): void {
27.  console.info('test1');
28.  }
29.
30.  build() {
31.  Column() {
32.  Child({ aBuilder0: this.componentBuilder })
33.  }
34.  }
35. }

```


[ResolvingIsNotCallable.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolvingIsNotCallable.ets#L21-L56)



**解决方案**



在JavaScript中调用this时，需要注意this的指向。当前代码在子组件中声明builder方法时，this指向的是父组件。而@Builder componentBuilder()通过this.componentBuilder的形式传给子组件@BuilderParam customBuilderParam，此时this指向的是子组件Child的label，即 “Child”。因此，在点击事件响应时，this指向的是Child，而Child中没有test1()方法，从而导致 JavaScript 错误。



为了解决这个问题，需要在父组件中声明子组件时，通过监听函数将 `this` 传递到子组件。应改为：



```typescript
1. Child({
2.  aBuilder0: () => {
3.  this.componentBuilder()
4.  }
5. })

```


[ResolvingIsNotCallable.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolvingIsNotCallable.ets#L71-L75)



**参考链接**



[@BuilderParam装饰器：引用@Builder函数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builderparam)
