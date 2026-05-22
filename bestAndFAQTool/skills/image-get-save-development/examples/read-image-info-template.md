# 读取图片信息模板

## 触发场景

用户需要读取图片宽高、基础信息或 EXIF 信息。

## 基础信息

```ts
const source = image.createImageSource(path);

source.getImageInfo((err, info) => {
  if (err) {
    hilog.error(0x0000, TAG, `getImageInfo failed: ${err.code}, ${err.message}`);
    return;
  }

  hilog.info(0x0000, TAG, `image info: ${JSON.stringify(info)}`);
});
```

## EXIF 信息

```ts
const keys = [
  image.PropertyKey.IMAGE_WIDTH,
  image.PropertyKey.IMAGE_LENGTH,
  image.PropertyKey.F_NUMBER
];

try {
  const properties = await source.getImageProperties(keys);
  hilog.info(0x0000, TAG, `image properties: ${JSON.stringify(properties)}`);
} catch (err) {
  const error = err as BusinessError;
  hilog.error(0x0000, TAG, `getImageProperties failed: ${error.code}, ${error.message}`);
}
```

## 迁移要求

- `path` 可来自相册选择 URI、拍照 URI 或应用文件路径。
- EXIF 字段只请求业务需要的 `PropertyKey`。
- 所有读取失败都要有错误处理。
