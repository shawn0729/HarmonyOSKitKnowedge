# 如何读取本地/预制数据库

**解决措施**



1. 将db文件推送到数据存储沙箱路径：/data/app/el2/100/database/(bundleName)/entry/rdb/。实现方式为使用文件管理接口打开本地数据库，读取其内容并写入沙箱路径下的db文件中。
  
  
  

```javascript
1. import { fileIo } from '@kit.CoreFileKit';
2. import { relationalStore } from '@kit.ArkData';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5.
6. // Obtaining the Context in EntryAbility, save it to AppStorage, then use AppStorage to retrieve it in the utility class.
7. let context = AppStorage.get('context') as UIContext;
8. let UiAbilityContent = context.getHostContext() as common.UIAbilityContext;
9. let RDBDirectory = UiAbilityContent.databaseDir;
10. let resource = UiAbilityContent.resourceManager;
11.
12. function initDatabase() {
13.  // Create a database sandbox directory
14.  try {
15.  let dirPath = RDBDirectory + '/rdb';
16.  fileIo.mkdirSync(dirPath);
17.  } catch (error) {
18.  console.error(`mkdir rdbPath failed, error code: ${error.code}, message: ${error.message}.`);
19.  }
20.
21.  // Set db name
22.  let dbName: string = 'Objective.db';
23.
24.  // Read the db file in the rawfile directory
25.  try {
26.  let content = resource.getRawFileContentSync(dbName);
27.  let cFile = RDBDirectory + '/rdb/' + dbName;
28.  let cacheFile = fileIo.openSync(cFile, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
29.  fileIo.write(cacheFile.fd, content.buffer);
30.  fileIo.closeSync(cacheFile.fd);
31.  } catch (error) {
32.  console.error(`callback getRawFd failed, error code: ${error.code}, message: ${error.message}.`);
33.  }
34. }

```
  [LocalDatabaseReader.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkDataKit/entry/src/main/ets/pages/LocalDatabaseReader.ets#L21-L55)

2. 通过[getRdbStore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f#relationalstoregetrdbstore)获取保存在沙箱路径下的db文件
  
  
  

```cangjie
1. async function getRDB(): Promise<relationalStore.RdbStore | undefined> {
2.  let result: relationalStore.RdbStore | undefined = undefined;
3.  const STORE_CONFIG: relationalStore.StoreConfig = {
4.  name: 'Objective.db',
5.  securityLevel: relationalStore.SecurityLevel.S1
6.  };
7.
8.  await relationalStore.getRdbStore(UiAbilityContent, STORE_CONFIG).then((rdbStore: relationalStore.RdbStore) => {
9.  result = rdbStore;
10.  console.info('Get RdbStore successfully.');
11.  }).catch((err: BusinessError) => {
12.  console.error(`Get RdbStore failed, code is ${err.code}, message is ${err.message}`);
13.  });
14.  return result;
15. }

```
  [LocalDatabaseReader.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkDataKit/entry/src/main/ets/pages/LocalDatabaseReader.ets#L59-L74)
