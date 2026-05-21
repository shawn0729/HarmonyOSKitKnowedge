# 如何使用AES算法加密

具体实现可参考如下代码：



```cangjie
1. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
2. import { buffer, util } from '@kit.ArkTS';
3.
4. @Entry
5. @Component
6. struct AESEncryptionDecryption {
7.  build() {
8.  Row() {
9.  Button('加解密')
10.  .onClick(async () => {
11.  // 导入密钥
12.  let key = await getKey();
13.  // 加密
14.  let globalResult = await aesEncrypt('测试', key);
15.  // 解密
16.  aesDecrypt(globalResult, key);
17.  })
18.  .width('100%')
19.  .height(50)
20.  }
21.  .height('100%')
22.  }
23. }
24.
25. export const base = new util.Base64Helper();
26.
27. // 字节流转成可理解的字符串
28. export function uint8ArrayToString(array: Uint8Array) {
29.  // 将UTF-8编码转换成Unicode编码
30.  let out: string = '';
31.  let index: number = 0;
32.  let len: number = array.length;
33.  while (index < len) {
34.  let character = array[index++];
35.  switch (character >> 4) {
36.  case 0:
37.  case 1:
38.  case 2:
39.  case 3:
40.  case 4:
41.  case 5:
42.  case 6:
43.  case 7:
44.  out += String.fromCharCode(character);
45.  break;
46.  case 12:
47.  case 13:
48.  out += String.fromCharCode(((character & 0x1F) << 6) | (array[index++] & 0x3F));
49.  break;
50.  case 14:
51.  out += String.fromCharCode(((character & 0x0F) << 12) | ((array[index++] & 0x3F) << 6) |
52.  ((array[index++] & 0x3F) << 0));
53.  break;
54.  default:
55.  break;
56.  }
57.  }
58.  return out;
59. }
60.
61. // 字符串转成字节流
62. function stringToUint8Array(str: string) {
63.  return new Uint8Array(buffer.from(str, 'utf-8').buffer);
64. }
65.
66. // 获取密钥
67. async function getKey() {
68.  let symAlgName = 'AES128';
69.  let symKeyGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
70.  let dataUint8Array = stringToUint8Array('Whh82GtW/EVjBkD8');
71.  let keyBlob: cryptoFramework.DataBlob = { data: dataUint8Array };
72.  let promiseSymKey = await symKeyGenerator.convertKey(keyBlob);
73.  let key = base.encodeToStringSync(promiseSymKey.getEncoded().data); // 将密钥转换为base64存储
74.  return key;
75. }
76.
77. // 加密
78. async function aesEncrypt(text: string, puKey: string): Promise<string> {
79.  let globalResult = '';
80.  try {
81.  let cipherAlgName = 'AES128|ECB|PKCS7';
82.  let globalCipher = cryptoFramework.createCipher(cipherAlgName);
83.  let symAlgName = 'AES128';
84.  let symKeyGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
85.  let dataUint8Array = base.decodeSync(puKey);
86.  let keyBlob: cryptoFramework.DataBlob = { data: dataUint8Array };
87.  let promiseSymKey = await symKeyGenerator.convertKey(keyBlob);
88.  await globalCipher.init(cryptoFramework.CryptoMode.ENCRYPT_MODE, promiseSymKey, null);
89.  let result = await globalCipher.doFinal({ data: stringToUint8Array(text) });
90.  globalResult = base.encodeToStringSync(result.data);
91.  console.info('加密后的明文:' + globalResult);
92.  } catch (err) {
93.  console.info(err.message);
94.  }
95.  return globalResult;
96. }
97.
98. // 解密
99. async function aesDecrypt(text: string, key: string) {
100.  let globalResult = '';
101.  try {
102.  let cipherAlgName = 'AES128|ECB|PKCS7';
103.  let globalCipher = cryptoFramework.createCipher(cipherAlgName);
104.  let symAlgName = 'AES128';
105.  let symKeyGenerator = cryptoFramework.createSymKeyGenerator(symAlgName);
106.  let dataUint8Array = base.decodeSync(key);
107.  let keyBlob: cryptoFramework.DataBlob = { data: dataUint8Array };
108.  let promiseSymKey = await symKeyGenerator.convertKey(keyBlob);
109.  await globalCipher.init(cryptoFramework.CryptoMode.DECRYPT_MODE, promiseSymKey, null);
110.  let plainText: cryptoFramework.DataBlob = { data: base.decodeSync(text) };
111.  let result = await globalCipher.doFinal(plainText);
112.  globalResult = uint8ArrayToString(result.data);
113.  console.info('解密后的明文:' + globalResult);
114.  } catch (err) {
115.  console.info(err.message);
116.  }
117. }

```
