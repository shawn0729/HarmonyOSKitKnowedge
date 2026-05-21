# 如何进行base64编码

可使用util中的Base64Helper()方法进行base64编码，参考代码如下：



```typescript
1. import { util } from '@kit.ArkTS';
2.
3. @Entry
4. @Component
5. struct Base64Encode {
6.  @State message: string = 'Base64 encoding';
7.
8.  build() {
9.  Row() {
10.  Column() {
11.  Text(this.message)
12.  .fontSize(50)
13.  .fontWeight(FontWeight.Bold)
14.  .onClick(() => {
15.  let base64 = new util.Base64Helper();
16.  let arr = new Uint8Array([48, 49, 2, 1, 1, 4, 32, 115, 56]);
17.  let base64Str = base64.encodeToStringSync(arr); // Uint8Array to base64
18.  console.log('encodeToStringSync',base64Str);
19.  // base64.decodeSync(''); // base64 to Uint8Array
20.  // console.log('decodeSync',base64.decodeSync(''));
21.  })
22.  }
23.  .width('100%')
24.  }
25.  .height('100%')
26.  }
27. }

```


[Base64Encode.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Base64Encode.ets#L21-L47)
