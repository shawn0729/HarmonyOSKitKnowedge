# 如何遍历JSON对象

具体请参考如下示例代码：



```typescript
1. import { ArrayList } from '@kit.ArkTS';
2.
3.
4. interface Winner { num: number };
5. let tmpStr: Record<string, Winner> = JSON.parse('{ "0": {"num": 1}, "1": {"num": 2} }');
6. const arrayList: ArrayList<Winner> = new ArrayList();
7. Object.entries(tmpStr).forEach((item) => {
8.  const value = item[1];
9.  arrayList.add(value);
10. })

```


[Entries.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Entries.ets#L21-L30)
