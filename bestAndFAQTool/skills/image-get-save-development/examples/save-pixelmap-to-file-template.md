# 保存 PixelMap 到文件模板

## 触发场景

用户需要把处理后的 `PixelMap` 编码并保存到应用可写目录。

## 核心代码形态

```ts
const packer = image.createImagePacker();
const options: image.PackingOption = {
  format: 'image/jpeg',
  quality: 95
};

const file = fileIo.openSync(
  filePath,
  fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE
);

await packer.packToFile(pixelMap, file.fd, options);
```

## 迁移要求

- `filePath` 必须是应用有权限写入的路径。
- `format` 根据业务选择 `image/jpeg`、`image/png` 等。
- `quality` 主要用于有损格式。
- 实际代码必须补充异常处理和文件关闭。
