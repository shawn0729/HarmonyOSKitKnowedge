# 如何生成UUID的字符串

使用util工具的generateRandomUUID函数可以生成字符串类型的UUID，示例如下：



```typescript
1. let uuid = util.generateRandomUUID(true);
2. console.info("RFC 4122 Version 4 UUID:" + uuid); // Output randomly generated UUID

```


[Uuid.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Uuid.ets#L7-L8)



**参考链接**



[util.generateRandomUUID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#utilgeneraterandomuuid9)
