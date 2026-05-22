# 如何获取到resources下rawfile 的文件

可以通过[@ohos.resourceManager (资源管理)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager)模块中的[getRawFileContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getrawfilecontent9)接口来获取resources/rawfile目录下对应的rawfile文件内容。参考代码如下：



```typescript
1. import { fileIo } from '@kit.CoreFileKit';
2.
3. @Component
4. export struct GetRawfile {
5.  @State message: string = 'Hello World';
6.
7.  aboutToAppear(): void {
8.  this.getUIContext().getHostContext()?.resourceManager.getRawFileContent('test.txt', (_err, value) => {
9.  if (_err) {
10.  console.error('Failed to get raw file:', _err);
11.  return;
12.  }
13.  let fileBuffer: ArrayBufferLike = value.buffer;
14.  let context = this.getUIContext()
15.  .getHostContext(); // Obtain the application sandbox path for storing temporary files, and perform null checking
16.  let filePath = context!.filesDir + '/test.txt';
17.  console.info('testTag-filePath:' + filePath);
18.  let file = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
19.  let writeLen = fileIo.writeSync(file.fd, fileBuffer);
20.  console.info('testTag-write data to file succeed and size is:' + writeLen);
21.  fileIo.closeSync(file);
22.  });
23.  }
24.
25.  build() {
26.  RelativeContainer() {
27.  Text(this.message)
28.  .id('RawfileHelloWorld')
29.  .fontSize(50)
30.  .fontWeight(FontWeight.Bold)
31.  .alignRules({
32.  center: { anchor: '__container__', align: VerticalAlign.Center },
33.  middle: { anchor: '__container__', align: HorizontalAlign.Center }
34.  })
35.  }
36.  .height('100%')
37.  .width('100%')
38.  }
39. }

```


[GetRawfile.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CoreFileKit/entry/src/main/ets/pages/GetRawfile.ets#L21-L60)
