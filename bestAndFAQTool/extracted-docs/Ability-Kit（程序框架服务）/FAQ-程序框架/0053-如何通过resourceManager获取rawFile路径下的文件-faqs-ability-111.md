# 如何通过resourceManager获取rawFile路径下的文件

**解决方案**



可以通过[@ohos.resourceManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager)中的[getRawFileList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getrawfilelist10)方法获取RawFile路径下的所有文件。参考代码如下：



```typescript
1. import { BusinessError } from '@kit.BasicServicesKit';
2.
3. // Passing in '' indicates obtaining a list of files in the root directory of rawfile
4. try {
5.  let context = AppStorage.get('context') as UIContext;
6.  context.getHostContext()!.resourceManager.getRawFileList('', (error: BusinessError, value: Array<string>) => {
7.  if (error != null) {
8.  console.error(`callback getRawFileList failed, error code: ${error.code}, message: ${error.message}.`);
9.  } else {
10.  let rawFile = value;
11.  }
12.  });
13. } catch (error) {
14.  let code = (error as BusinessError).code;
15.  let message = (error as BusinessError).message;
16.  console.error(`callback getRawFileList failed, error code: ${code}, message: ${message}.`);
17. }

```


[GetRaw.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/GetRaw.ets#L21-L37)
