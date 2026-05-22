# 如何指定对象某些属性参与序列化

可以通过[JSON.stringify()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-json#jsonstringify)方法实现，stringify(value: Object, replacer?: (number | string)[] | null, space?: string | number): string中，当replacer为数组时，只有包含在这个数组中的属性名才会被序列化到最终的JSON字符串中；当参数为null或者未提供时，则对象所有的属性都会被序列化。



示例代码参考如下：



```typescript
1. import { JSON } from '@kit.ArkTS';
2.
3. interface Person {
4.  name: string;
5.  age: number;
6.  city: string;
7. }
8.
9. let obj: Person = { name: 'John', age: 30, city: 'ChongQing' };
10.
11. @Entry
12. @Component
13. struct JSONDemo {
14.  @State str: string = 'to json';
15.
16.  build() {
17.  Row() {
18.  Column() {
19.  Button(this.str)
20.  .onClick(() => {
21.  let jsonStr1 = JSON.stringify(obj); // All attributes are serialized
22.  console.info('jsonStr1：', jsonStr1); // jsonStr1： {"name":"John","age":30,"city":"ChongQing"}
23.  let jsonStr2 = JSON.stringify(obj, ['name']); // Specify the name attribute and serialize it
24.  console.info('jsonStr2：', jsonStr2); // jsonStr2： {"name":"John"}
25.  })
26.  }
27.  .width('100%')
28.  }
29.  .height('100%')
30.  }
31. }

```


[SpecifyCertainProperties.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SpecifyCertainProperties.ets#L21-L51)
