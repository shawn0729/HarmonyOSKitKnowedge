# 如何处理大整数

使用BigInt来处理大整数。



BigInt可以表示任意大小的整数。使用BigInt时，在整数字面量后面添加n后缀或使用BigInt()构造函数。



示例如下：



```typescript
1. @Entry
2. @Component
3. struct BigIntNum {
4.  build() {
5.  Row() {
6.  Column() {
7.  Button('BigInt num')
8.  .onClick(() => {
9.  let bigIntNum: bigint = 12345678901234567890n; // Add n suffix after integer
10.  let anotherBigInt: bigint = BigInt(9007199254740992); // Use BigInt() constructor
11.  let sumBigInt: bigint = bigIntNum + anotherBigInt;
12.  console.info('bigIntNum:' + bigIntNum);
13.  console.info('anotherBigInt:' + anotherBigInt);
14.  console.info('bigIntNum + anotherBigInt:' + sumBigInt);
15.  })
16.  }
17.  .width('100%')
18.  }
19.  .height('100%')
20.  }
21. }

```


[BigIntNum.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/BigIntNum.ets#L21-L41)
