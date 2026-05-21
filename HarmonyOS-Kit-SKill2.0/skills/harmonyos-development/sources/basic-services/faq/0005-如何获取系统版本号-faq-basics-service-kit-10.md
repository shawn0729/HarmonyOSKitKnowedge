# 如何获取系统版本号

可通过[@ohos.deviceInfo (设备信息)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-device-info)模块，查询设备信息。



示例如下：



```typescript
1. import { deviceInfo } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3.
4. let displayVersionInfo: string = deviceInfo.displayVersion; // product version
5. let osFullNameInfo: string = deviceInfo.osFullName; // system version
6. let versionIdInfo: string = deviceInfo.versionId; // version ID
7.
8. @Entry
9. @Component
10. struct GetSysVersion {
11.  build() {
12.  Row() {
13.  Column() {
14.  Button('get device info')
15.  .onClick(() => {
16.  hilog.info(0x000, 'displayVersion TAG', `displayVersion:${displayVersionInfo}`);
17.  hilog.info(0x000, 'osFullName TAG', `osFullName:${osFullNameInfo}`);
18.  hilog.info(0x000, 'versionId TAG', `versionId:${versionIdInfo}`);
19.  })
20.  }
21.  .width('100%')
22.  }
23.  .height('100%')
24.  }
25. }

```


[GetSysVersion.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/BasicsServiceKit/entry/src/main/ets/pages/GetSysVersion.ets#L21-L46)
