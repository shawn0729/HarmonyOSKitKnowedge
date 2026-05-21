# 如何开关闪光灯

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-13

---

使用[isFlashModeSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flashquery#isflashmodesupported11)方法检测设备是否支持需要设置的闪光灯模式后，使用[setFlashMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-flash#setflashmode11)设置闪光灯模式。



**参考代码**



```typescript
1. setFlash(captureSession: camera.PhotoSession,flashMode: camera.FlashMode) {
2.  if (captureSession != null) {
3.  let focusModeStatus: boolean = captureSession?.isFlashModeSupported(flashMode);
4.  if (focusModeStatus) {
5.  captureSession.setFlashMode(flashMode);
6.  }
7.  }
8. }

```


[SetFlash.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/SetFlash.ets#L22-L29)
