# 如何对相册图片进行编辑裁剪

---

可以通过[图片处理](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image)模块的[pixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap)方法对图片进行编辑裁剪。



其中包括但不限于：



- [pixelMap.crop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#crop9)方法，可以根据输入的尺寸对图片进行裁剪。
- [pixelMap.opacity](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#opacity9)方法，可以通过设置透明比率对图片设置透明效果。
- [pixelMap.scale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#scale9)方法，可以根据输入的宽高对图片进行缩放。
- [pixelMap.rotate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#rotate9)方法，可以根据输入的角度对图片进行旋转。
- [pixelMap.flip](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#flip9)方法，可以根据输入的条件对图片进行翻转。


以下示例代码为[pixelMap.crop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap#crop9)图片裁剪方法的使用：



```typescript
1. // Crop 4:3
2. class RegionItem {
3.  /**
4.  * width coordinate.
5.  */
6.  x: number;
7.
8.  /**
9.  * height coordinate.
10.  */
11.  y: number;
12.
13.  constructor(x: number, y: number) {
14.  this.x = x;
15.  this.y = y;
16.  }
17. }
18.
19. export async function cropCommon(pixelMap: PixelMap, cropWidth: number, cropHeight: number, cropPosition: RegionItem) {
20.  pixelMap.crop({
21.  size: {
22.  width: cropWidth,
23.  height: cropHeight
24.  },
25.  x: cropPosition.x,
26.  y: cropPosition.y
27.  });
28. }
29.
30. // Pass in three parameters: image. PixelMap, image width, and image height. After obtaining the cropped image width and height,
31. // pass the parameters into the cropCommon method
32. export async function banner(pixelMap: PixelMap, width: number, height: number) {
33.  if (width <= height) {
34.  const cropWidth = width;
35.  const cropHeight = Math.floor(width * 0.75);
36.  const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / 2));
37.  cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
38.  return;
39.  }
40.  if (width * 0.75 >= height) {
41.  const cropWidth = Math.floor(height / 0.75);
42.  const cropHeight = height;
43.  const cropPosition = new RegionItem(Math.floor((width - cropWidth) / 2), 0);
44.  cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
45.  return;
46.  }
47.  const cropWidth = width;
48.  const cropHeight = Math.floor(width * 0.75);
49.  const cropPosition = new RegionItem(0, Math.floor((height - cropHeight) / 2));
50.  cropCommon(pixelMap, cropWidth, cropHeight, cropPosition);
51. }

```


[CropCommon.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/CropCommon.ets#L21-L71)
