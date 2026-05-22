# 如何实现类似Java中的反射方法调用能力

可以通过[动态import](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dynamic-import#%E5%8A%A8%E6%80%81import%E5%AE%9E%E7%8E%B0%E6%96%B9%E6%A1%88%E4%BB%8B%E7%BB%8D)的方式实现类似反射能力，具体实现可参考以下代码。



```typescript
1. import('./module').then(
2.  module => {
3.  const t = module.DataTable.tagName();
4.  });

```


[DynamicImport.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/DynamicImport.ets#L21-L24)



```typescript
1. export class DataTable {
2.  constructor() {
3.  }
4.  static tagName(){
5.  return 'data-table'
6.  }
7. }

```


[module.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/module.ets#L21-L27)
