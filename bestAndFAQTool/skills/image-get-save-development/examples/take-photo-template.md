# 拍照获取图片模板

## 触发场景

用户需要拉起系统相机拍照，并获取照片 URI。

## 核心代码形态

```ts
const profile: cameraPicker.PickerProfile = {
  cameraPosition: camera.CameraPosition.CAMERA_POSITION_BACK
};

const result = await cameraPicker.pick(
  context,
  [cameraPicker.PickerMediaType.PHOTO],
  profile
);

const imageUri = result.resultUri;
```

## 迁移要求

- `context` 使用当前 Ability/UI 上下文。
- 按业务选择前置或后置摄像头。
- 处理用户取消、拍照失败和 `resultUri` 为空的情况。
