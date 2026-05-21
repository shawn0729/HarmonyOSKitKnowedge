# 如何修改沙箱路径下json文件的指定内容

可以通过以下步骤来完成：



```typescript
1. import { fileIo } from '@kit.CoreFileKit';
2.
3. // In the utility class, retrieve the Context from the Entry Ability and save it to AppStore, then use AppStore to retrieve it in the utility class
4. let context = AppStorage.get("context") as UIContext;
5. let filePath = context.getHostContext()!.filesDir + '/people.json';
6.
7. class Student {
8.  name: string = 'zhangsan';
9.  age: number = 10;
10. }
11.
12. let student = new Student();
13. // 1 Create a file and write its contents
14. let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
15. fileIo.writeSync(file.fd, JSON.stringify(student))
16. fileIo.close(file);
17. // 2 Read the contents of the JSON file through fileIo.readSync.
18. let data = fileIo.readTextSync(filePath);
19. let obj: Student = JSON.parse(data);
20. // 3 Change the specified content name to lisi
21. obj.name = 'lisi';
22. // 4 Rewrite JSON file
23. let fileModify = fileIo.openSync(filePath, fileIo.OpenMode.WRITE_ONLY | fileIo.OpenMode.TRUNC);
24. fileIo.writeSync(fileModify.fd, JSON.stringify(obj));
25. fileIo.close(fileModify);
26. // 5 Read the latest content
27. let content = fileIo.readTextSync(filePath);
28. console.info(`ModifySanFileContent content is :${content}`);

```


[UpdateSandboxJson.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CoreFileKit/entry/src/main/ets/pages/UpdateSandboxJson.ets#L21-L48)



**参考链接**



[文件管理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-fs)
