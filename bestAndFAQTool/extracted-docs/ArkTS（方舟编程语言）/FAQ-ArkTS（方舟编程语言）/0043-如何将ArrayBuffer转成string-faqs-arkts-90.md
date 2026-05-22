# 如何将ArrayBuffer转成string

可以通过util.TextDecoder.create()方法创建一个实例，再通过[decodeToString()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#decodetostring12)方法进行转换。



```typescript
1. let decoder = util.TextDecoder.create('utf-8');
2. let str = decoder.decodeToString(new Uint8Array(arrayBuffer));

```


[TextDecoder.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TextDecoder.ets#L36-L37)



开发者可以将 proArrayBuffer 返回的 ArrayBuffer 类型的数据 arrayBufferVal 转换为字符串。



```typescript
1. import { util, buffer } from '@kit.ArkTS';
2.
3. let blobValue: buffer.Blob = new buffer.Blob(['name', 'age', 'sex']);
4. let proArrayBuffer = blobValue.arrayBuffer();
5.
6. proArrayBuffer.then((arrayBufferVal: ArrayBuffer) => {
7.  let decoder = util.TextDecoder.create('utf-8');
8.  let stringData = decoder.decodeToString(new Uint8Array(arrayBufferVal));
9.  console.log('stringData:', stringData);
10. });

```


[TextDecoder.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TextDecoder.ets#L21-L30)
