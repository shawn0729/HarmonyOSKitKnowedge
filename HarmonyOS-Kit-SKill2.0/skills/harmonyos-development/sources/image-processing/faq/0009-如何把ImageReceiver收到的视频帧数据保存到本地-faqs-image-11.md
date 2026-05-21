# 如何把ImageReceiver收到的视频帧数据保存到本地

---

如示例代码所示，保存接收到的前3帧数据，可根据业务需求进行调整。



```typescript
1. let size: image.Size = {
2.  width: 640,
3.  height: 480
4. }
5. let receiver: image.ImageReceiver = image.createImageReceiver(size, image.ImageFormat.JPEG, 8);
6. receiver.on('imageArrival', () => {
7.  console.info("imageArrival callback");
8.  receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
9.  if (err || nextImage === undefined) {
10.  console.error("receiveImage -error:" + err + " nextImage:" + nextImage);
11.  return;
12.  }
13.  nextImage.getComponent(image.ComponentType.JPEG, (err: BusinessError, imgComponent: image.Component) => {
14.  if (err || imgComponent === undefined) {
15.  console.error("receiveImage--getComponent -error:" + err + " imgComponent:" + imgComponent);
16.  return;
17.  }
18.
19.  if (imgComponent.byteBuffer as ArrayBuffer) {
20.  let sourceOptions: image.SourceOptions = {
21.  sourceDensity: 120,
22.  sourcePixelFormat: 8,
23.  sourceSize: {
24.  height: 1080,
25.  width: 1920
26.  },
27.  }
28.  let imageResource = image.createImageSource(imgComponent.byteBuffer, sourceOptions);
29.  let imagePackerApi = image.createImagePacker();
30.  let packOpts: image.PackingOption = { format: "image/jpeg", quality: 90 };
31.  const filePath: string = context.getHostContext()!.cacheDir + "/image.jpg";
32.  let file = fs.openSync(filePath, fs.OpenMode.CREATE | fs.OpenMode.READ_WRITE);
33.  imagePackerApi.packToFile(imageResource, file.fd, packOpts).then(() => {
34.  console.error('pack success: ' + filePath);
35.  }).catch((error: BusinessError) => {
36.  console.error('Failed to pack the image. And the error is: ' + error);
37.  })
38.  imageResource.createPixelMap({}).then((res) => {
39.  this.imgUrl = res;
40.  });
41.  } else {
42.  return;
43.  }
44.  nextImage.release();
45.  });
46.  });
47. });

```


[SaveVideoFrameDataLocally.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/SaveVideoFrameDataLocally.ets#L31-L77)
