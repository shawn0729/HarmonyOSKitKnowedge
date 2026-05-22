# 对象反序列化时number类型丢失精度如何解决

1. 通过[JSON.parse()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json#jsonparse)解析，可以通过传入options参数，指定options为bigIntMode: JSON.BigIntMode.PARSE_AS_BIGINT，来处理BigInt的模式。     示例代码参考如下：


  
  
  

```typescript
1. import { JSON } from '@kit.ArkTS';
2.
3. let options: JSON.ParseOptions = {
4.  bigIntMode: JSON.BigIntMode.PARSE_AS_BIGINT,
5. }
6. let numberText = '{"largeNumber":1122333444455556666677777888889}';
7. let numberObj = JSON.parse(numberText, (key: string, value: Object | undefined | null): Object | undefined | null => {
8.  if (key === "largeNumber") {
9.  return value;
10.  }
11.  return value;
12. }, options) as Object;
13.
14. @Entry
15. @Component
16. struct BigIntDemo {
17.  @State str: string = 'bigint num';
18.
19.  build() {
20.  Row() {
21.  Column() {
22.  Button(this.str)
23.  .onClick(() => {
24.  console.info((numberObj as object)?.["largeNumber"]); // 1122333444455556666677777888889
25.  })
26.  }
27.  .width('100%')
28.  }
29.  .height('100%')
30.  }
31. }


```
  [NumberLosesAccuracy.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/NumberLosesAccuracy.ets#L21-L51)

2. 使用三方库[json-bigint](https://ohpm.openharmony.cn/#/cn/detail/@ohmos%2Fjson-bigint)处理。
