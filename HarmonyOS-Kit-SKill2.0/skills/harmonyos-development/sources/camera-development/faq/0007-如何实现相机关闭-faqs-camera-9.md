# 如何实现相机关闭

---

实现相机关闭的参考代码如下：



```typescript
1. // Stop the current session
2.  photoSession.stop();
3.
4. // Release camera input stream
5.  cameraInput.close();
6.
7. // Release preview output stream
8.  previewOutput.release();
9.
10. // Release the photo output stream
11.  photoOutput.release();
12.
13. // Release session
14.  photoSession.release();
15.
16. // Session left blank
17.  photoSession = undefined;

```


[CloseSession.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/CloseSession.txt#L7-L23)



**参考链接**



[拍照实践(ArkTS)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting-case)
