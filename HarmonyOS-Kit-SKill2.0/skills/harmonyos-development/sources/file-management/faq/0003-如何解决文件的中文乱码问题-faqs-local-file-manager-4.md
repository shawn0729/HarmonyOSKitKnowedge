# 如何解决文件的中文乱码问题

读取文件内容的buffer数据后，通过TextDecoder对文件内容进行解码。



```javascript
1. import { util } from '@kit.ArkTS';
2. import { fileIo } from '@kit.CoreFileKit';
3.
4. // In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
5. let context = AppStorage.get("context") as UIContext;
6. // Create a file to write Chinese characters
7. let filePath = context.getHostContext()!.filesDir + "/test0.txt";
8. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
9. // Write a paragraph of content to a file
10. let writeLen = fileIo.writeSync(file.fd, "Hello, world");
11. fileIo.closeSync(file);
12. console.info(`GarbledCnCharacters The length of str is: ${writeLen}`);
13. let stream = fileIo.createStreamSync(filePath, "r+");
14. let buffer = new ArrayBuffer(4096);
15. stream.readSync(buffer);
16. // Set the encoding format to "utf-8"
17. let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
18. // Retrieve the corresponding text after decoding the input
19. let readString = textDecoder.decodeToString(new Uint8Array(buffer), { stream: false });
20. console.info(`GarbledCnCharacters read content is:${readString}`);

```


[HandleFileEncodingProblem.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CoreFileKit/entry/src/main/ets/pages/HandleFileEncodingProblem.ets#L21-L40)



**参考链接**



[TextDecoder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-util#textdecoder)
