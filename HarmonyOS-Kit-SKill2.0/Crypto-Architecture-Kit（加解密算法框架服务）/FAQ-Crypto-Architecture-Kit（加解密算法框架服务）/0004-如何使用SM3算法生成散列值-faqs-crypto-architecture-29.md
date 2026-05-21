# 如何使用SM3算法生成散列值

调用[cryptoFramework.createMd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-cryptoframework#cryptoframeworkcreatemd)方法，传入SM3，可参考如下代码：



```typescript
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { util, buffer } from '@kit.ArkTS';
4.
5. let base64 = new util.Base64Helper();
6.
7. @Entry
8. @Component
9. struct SM3Encrypted {
10.  stringToUint8Array(str: string) {
11.  return new Uint8Array(buffer.from(str, 'utf-8').buffer);
12.  }
13.
14.  // Complete the summary in Promise format
15.  doMdByPromise() {
16.  // Summary algorithm name.
17.  let mdAlgName = 'SM3';
18.  // The data to be summarized.
19.  let message = 'Hello,world';
20.  let md = cryptoFramework.createMd(mdAlgName);
21.  console.info('[Promise]: Md algName is: ' + md.algName);
22.  let promiseMdUpdate = md.update({ data: this.stringToUint8Array(message) });
23.  promiseMdUpdate.then(() => {
24.  // Call digest() to return the result.
25.  let PromiseMdDigest = md.digest();
26.  return PromiseMdDigest;
27.  }).then(digestOutput => {
28.  let mdOutput = digestOutput.data;
29.  //Uint8Array to base64
30.  let str2 = base64.encodeToStringSync(mdOutput);
31.  //Convert to hexadecimal
32.  let str = this.uint8ArrayToHexStr(mdOutput);
33.  console.info('[Promise]: MD result: ' + mdOutput);
34.  let mdLen = md.getMdLength();
35.  console.info('[Promise]: MD len: ' + mdLen);
36.  }).catch((error: BusinessError) => {
37.  console.error('[Promise]: error: ' + error.message);
38.  });
39.  }
40.
41.  //The summary result is Uint8Array type, converted to hexadecimal string data
42.  uint8ArrayToHexStr(data: Uint8Array): string {
43.  let hexString = '';
44.  let i: number;
45.  for (i = 0; i < data.length; i++) {
46.  let char = ('00' + data[i].toString(16)).slice(-2);
47.  hexString += char;
48.  }
49.  return hexString;
50.  }
51.
52.  build() {
53.  Column({ space: 10 }) {
54.  Button('使用SM3加密')
55.  .onClick(() => {
56.  this.doMdByPromise();
57.  })
58.  }
59.  .alignItems(HorizontalAlign.Center)
60.  .height('100%')
61.  .width('100%')
62.  }
63. }

```


[SM3Encrypted.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CryptoArchitectureKit/entry/src/main/ets/pages/SM3Encrypted.ets#L21-L83)
