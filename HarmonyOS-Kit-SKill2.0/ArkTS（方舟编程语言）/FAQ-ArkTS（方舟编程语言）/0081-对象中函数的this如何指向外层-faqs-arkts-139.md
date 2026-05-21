# 对象中函数的this如何指向外层

通过箭头函数实现。参考代码如下：



```typescript
1. interface T {
2.  start: () => number
3. }
4. @Component
5. struct PointingOuterLayer {
6.  @State num: number = 1
7.  obj: T = {
8.  start: () => {
9.  return this.num
10.  }
11.  }

```


[PointingOuterLayer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/PointingOuterLayer.ets#L21-L31)
