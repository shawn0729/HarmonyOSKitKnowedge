# 蓝牙资源合理使用

无长时任务的应用退到后台时，不允许进行蓝牙扫描。



## 约束

应用退到后台时，系统会强制停止扫描；回到前台后，系统将恢复扫描。



## 示例

```typescript
1. import { UIAbility } from '@kit.AbilityKit';
2. import { ble } from '@kit.ConnectivityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5.
6. // ...
7. export default class EntryAbility extends UIAbility {
8.  // ...
9.  onForeground(): void {
10.  try {
11.  //Initiate Ble scan and broadcast as required by the service at the foreground
12.  ble.startBLEScan([scanFilter], scanOptions);
13.  ble.startAdvertising(setting, advData, advResponse);
14.  } catch (error) {
15.  let err = error as BusinessError;
16.  hilog.warn(0x000, 'testTag', `startBLEScan or startAdvertising failed, code=${err.code}, message=${err.message}`);
17.  }
18.  }
19.
20.  onBackground(): void {
21.  try {
22.  // Return to the background to stop the Ble scanning and broadcast, which is the same as the application
23.  ble.stopBLEScan();
24.  ble.stopAdvertising();
25.  } catch (error) {
26.  let err = error as BusinessError;
27.  hilog.warn(0x000, 'testTag', `stopBLEScan or stopAdvertising failed, code=${err.code}, message=${err.message}`);
28.  }
29.  }
30. }

```


[Bluetooth.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BptaUseResources/entry/src/main/ets/pages/Bluetooth.ets#L6-L45)



有关蓝牙相关接口的使用，详情可以参考[查找设备](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide)。
