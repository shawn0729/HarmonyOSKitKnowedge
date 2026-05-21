# 如何读取指定文件内容，并转为具体对象

可以使用[getRawFileContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getrawfilecontent9)方法，参考代码如下：



```typescript
1. import { Context } from '@kit.AbilityKit';
2. import { buffer } from '@kit.ArkTS';
3.
4. @Entry
5. @Component
6. struct Index {
7.  private context: Context | undefined = this.getUIContext().getHostContext();
8.  private str: string = '';
9.
10.  getRawFile(): ESObject {
11.  //Call the getRawFileContent interface to retrieve the content of a JSON file and read it as a string
12.  this.getUIContext().getHostContext()!.resourceManager.getRawFileContent('test.json', (err, data) => {
13.  try {
14.  this.str = buffer.from(data.buffer).toString();
15.  console.info(JSON.stringify(this.str));
16.  } catch (e) {
17.  console.info(JSON.stringify(e));
18.  }
19.  })
20.  //You can also call the getRawFileContentSync interface to retrieve the content of the JSON file and read it as a string
21.  try {
22.  let data: Uint8Array = this.context!.resourceManager.getRawFileContentSync('test.json');
23.  this.str = buffer.from(data.buffer).toString();
24.  } catch (e) {
25.  console.info(JSON.stringify(e));
26.  }
27.  // Convert string to ESObject
28.  let obj: ESObject = JSON.parse(this.str);
29.  console.info('ESObject', JSON.stringify(obj));
30.  return obj;
31.  }
32.
33.  build() {
34.  Column() {
35.  Button('get')
36.  .onClick(() => {
37.  this.getRawFile();
38.  })
39.  }.width('100%')
40.  }
41. }

```


[FileContentParser.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CoreFileKit/entry/src/main/ets/pages/FileContentParser.ets#L21-L61)
