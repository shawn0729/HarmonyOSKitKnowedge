# 图片读取能力

## 覆盖范围

用于通过 URI/path 创建 `ImageSource`，读取图片基础信息和 EXIF 信息。

## 核心链路

```text
图片 URI/path
  -> image.createImageSource(...)
  -> getImageInfo(...)
  -> getImageProperties(...)
  -> 按需解码或进入 PixelMap 处理
```

## API 选择

- 基础信息：`ImageSource.getImageInfo`
- EXIF 信息：`ImageSource.getImageProperties`
- EXIF 字段：`image.PropertyKey`

## 示例路由

- 读取基础信息或 EXIF：
  读取 `examples/read-image-info-template.md`

## 常见错误

- 无错误处理地调用图片读取 API。
- 读取所有 EXIF 字段，而不是只读取业务需要字段。
- 没有区分图片 URI、应用文件路径和临时文件路径。
