# 如何定义一个具有任意键的对象

可使用Record类型，有几个属性就对应几个类型参数，参考代码如下：



```typescript
1. const asd: Record<string, number | string> = {
2.  'name': 'xc',
3.  'age': 29
4. }

```


[UnknowType.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/UnknowType.ets#L21-L24)
