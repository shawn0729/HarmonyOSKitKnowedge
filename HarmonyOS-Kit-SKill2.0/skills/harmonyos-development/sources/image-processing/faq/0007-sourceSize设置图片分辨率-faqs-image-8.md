# sourceSize设置图片分辨率

---

可以通过[sourceSize](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image#sourcesize)属性设置图片分辨率。实例代码如下，原图尺寸为1280×960，示例将图片解码为40×40。



```typescript
1. @Entry
2. @Component
3. struct Index {
4.  build() {
5.  Column() {
6.  Row({ space: 50 }) {
7.  Image($r('app.media.example'))
8.  .sourceSize({
9.  width: 40,
10.  height: 40
11.  })
12.  .objectFit(ImageFit.ScaleDown)
13.  .aspectRatio(1)
14.  .width('25%')
15.  .border({ width: 1 })
16.  .overlay('width:40 height:40', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
17.  }
18.  }
19.  }
20. }

```


[DisplayAspectRatio.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/DisplayAspectRatio.ets#L21-L40)
