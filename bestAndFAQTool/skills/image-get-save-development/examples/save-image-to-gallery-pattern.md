# 保存图片到系统相册模式

## 触发场景

用户需要把处理后的图片保存到系统图库，而不是只保存在应用目录。

## 推荐模式

```text
PixelMap
  -> 使用 ImagePacker 编码
  -> 先保存到应用文件目录
  -> 通过 Media Library Kit 写入系统相册
  -> 处理用户授权和失败场景
```

## 相关能力

- `photoAccessHelper`
- `SaveButton`
- `MediaAssetChangeRequest`
- `PhotoAccessHelper.applyChanges(...)`

## 迁移要求

- 不要把应用目录文件当作系统相册结果。
- 保存到图库必须考虑授权。
- 用户拒绝授权或取消操作时，业务要有可恢复反馈。
- 如需兼容不同保存入口，优先把“编码到文件”和“入库相册”拆成两个函数。
