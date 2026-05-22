# 如何实现字符串编解码

TextEncoder用于将字符串编码为字节数组，支持utf-8、utf-16le/be等编码格式。



TextDecoder用于将字节数组解码为字符串，支持多种编码格式，如utf-8、utf-16le/be、iso-8859和windows-1251。



以下示例代码展示了如何使用TextEncoder和TextDecoder进行字符串编解码：



```typescript
1. import { util } from '@kit.ArkTS';
2. // Create Encoder
3. let textEncoder:util.TextEncoder = new util.TextEncoder('gbk');
4. let buffer:ArrayBuffer = new ArrayBuffer(20);
5. let encodeResult:Uint8Array = new Uint8Array(buffer);
6.
7.
8. // code
9. encodeResult = textEncoder.encodeInto('hello');
10. console.info('Encode result: ', encodeResult);
11.
12.
13. // Create decoder
14. let textDecoder = util.TextDecoder.create('gbk');
15.
16.
17. // decode
18. let decodeResult = textDecoder.decodeToString(encodeResult);
19. console.info('Decode result: ', decodeResult);

```


[TextEncoder.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TextEncoder.ets#L21-L39)



**参考链接**



[TextEncoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#textencoder)、[TextDecoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#textdecoder)
