# 图片保存能力

## 覆盖范围

用于将 `PixelMap` 编码并保存到应用文件目录或系统相册。

## 保存到应用文件目录

适用：

- 应用内部缓存。
- 图片编辑结果中转。
- 上传、分享前的临时文件。

核心链路：

```text
PixelMap
  -> image.createImagePacker()
  -> image.PackingOption
  -> fileIo.openSync(...)
  -> packToFile(pixelMap, fd, options)
```

读取：

```text
examples/save-pixelmap-to-file-template.md
```

## 保存到系统相册

适用：

- 用户明确希望图片进入图库。
- 图片编辑结果需要被系统媒体库管理。

核心链路：

```text
PixelMap
  -> 先编码保存到应用文件目录
  -> 通过 Media Library Kit 保存到系统相册
  -> 处理授权、取消和写入失败
```

读取：

```text
examples/save-image-to-gallery-pattern.md
```

## 常见错误

- 以为写入应用沙箱文件就等于保存到系统相册。
- 保存相册时没有考虑授权。
- 编码后没有关闭文件描述符。
- 没有根据业务选择合适的图片格式和质量。
