# ArkTS中有类似Java中的System.arraycopy数组复制的方法吗

可以通过 buffer.concat() 方法，将数组中的内容复制到新的 Buffer 对象中并返回。参考代码如下：



```typescript
1. import { buffer } from '@kit.ArkTS';
2.
3. let buf1 = buffer.from("1234");
4. let buf2 = buffer.from("abcd");
5. let buf = buffer.concat([buf1, buf2]);
6. console.info(buf.toString('hex'));
7. // Output result:3132333461626364

```


[Buffer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Buffer.ets#L21-L27)



**参考链接**



[buffer.concat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-buffer#bufferconcat)
