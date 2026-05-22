# 图片获取能力

## 覆盖范围

用于从系统相册、页面内嵌选择器或系统相机获取图片 URI。

## 选型规则

- 选择已有图片，且希望拉起系统相册：使用 `PhotoViewPicker`。
- 希望在应用页面内嵌相册选择：使用 `PhotoPickerComponent`。
- 快速拍照获取图片：使用 `CameraPicker`。
- 需要自定义取景、预览、拍摄参数：使用 Camera Kit。

## 示例路由

- 相册选择：
  读取 `examples/pick-image-from-album-template.md`

- 拍照获取：
  读取 `examples/take-photo-template.md`

## 常见错误

- 把相册选择和拍照结果当作文件路径直接处理，忽略 URI 权限和可访问性。
- 简单拍照场景却直接设计完整自定义 Camera Kit 流程。
- 没有处理用户取消选择或拍照失败。
