# 如何存储文件才不会跟随app卸载而删除

**解决措施**



如果是用户文件，例如在应用内主动保存的文件，可以存储在媒体库公共目录/storage/media/100/local/files。公共目录下的文件不会在应用卸载时被删除。



**参考代码**



可以使用[@ohos.file.picker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-file-picker)中提供的save方法在公共目录创建文件，方法可以参考以下代码：



```typescript
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { picker, fileIo } from '@kit.CoreFileKit';
3.
4. let uri: string = '';
5.
6. // Save content to the public directory
7. export async function saveToUser(content: string) {
8.  try {
9.  let DocumentSaveOptions = new picker.DocumentSaveOptions();
10.  // New file name
11.  DocumentSaveOptions.newFileNames = ['test.txt'];
12.  let documentPicker = new picker.DocumentViewPicker();
13.  documentPicker.save(DocumentSaveOptions).then((DocumentSaveResult: Array<string>) => {
14.  console.info('DocumentViewPicker.save successfully, uri: ' + JSON.stringify(DocumentSaveResult));
15.  uri = DocumentSaveResult[0];
16.  // Write the content into the newly created file
17.  let file = fileIo.openSync(uri, fileIo.OpenMode.READ_WRITE);
18.  fileIo.writeSync(file.fd, content);
19.  }).catch((err: BusinessError) => {
20.  console.error('DocumentViewPicker.save failed with err: ' + JSON.stringify(err));
21.  });
22.  } catch (error) {
23.  let err: BusinessError = error as BusinessError;
24.  console.error('DocumentViewPicker failed with err: ' + err.message);
25.  }
26. }

```


[SaveToUser.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocationKit/entry/src/main/ets/pages/SaveToUser.ets#L21-L46)
