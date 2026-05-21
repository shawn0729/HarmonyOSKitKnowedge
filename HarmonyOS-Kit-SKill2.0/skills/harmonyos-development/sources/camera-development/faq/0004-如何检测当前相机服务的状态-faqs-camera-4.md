# 如何检测当前相机服务的状态

---

设置状态回调以返回相机状态。



```typescript
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. const context = AppStorage.get("context") as UIContext;
4. let cameraManager = camera.getCameraManager(context.getHostContext()!);
5. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
6.  console.log(`camera : ${cameraStatusInfo.camera.cameraId}`);
7.  console.log(`status: ${cameraStatusInfo.status}`);
8. });

```


[GetCameraStatus.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetCameraStatus.ets#L21-L28)



相机状态：CameraStatus



CameraStatus是一个枚举，表示相机状态。







**参考链接**



[CameraStatus](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e#camerastatus)
