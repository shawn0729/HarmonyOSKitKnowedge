# 分享面板 ShareKit

> 使用 `@kit.ShareKit` 拉起系统分享面板，替代 Android 的 `Intent.ACTION_SEND`。

---

## 基本导入

```typescript
import { systemShare } from '@kit.ShareKit'
import { uniformTypeDescriptor as utd } from '@kit.ArkData'
import { common } from '@kit.AbilityKit'
```

---

## 完整调用模板

```typescript
async function shareMedia(
  context: common.UIAbilityContext,
  uri: string,
  title: string,
  mimeType: string
): Promise<void> {
  // 1. 转换 MIME 类型为 UTD 类型 ID
  const ext = uri.substring(uri.lastIndexOf('.') + 1).toLowerCase()
  const utdTypeId = utd.getUniformDataTypeByFilenameExtension('.' + ext, utd.UniformDataType.IMAGE)

  // 2. 构建分享数据
  const shareData: systemShare.SharedData = new systemShare.SharedData({
    utd: utdTypeId,
    uri: uri,
    title: title,
    description: '分享 ' + title
  })

  // 3. 创建分享控制器
  const controller: systemShare.ShareController = new systemShare.ShareController(shareData)

  // 4. 展示分享面板
  controller.show(context, {
    selectionMode: systemShare.SelectionMode.SINGLE,
    previewMode: systemShare.SharePreviewMode.DETAIL
  }).then(() => {
    hilog.info(DOMAIN, TAG, 'ShareController show success')
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN, TAG, `ShareController show error: ${error.code}, ${error.message}`)
    promptAction.showToast({ message: '分享失败' })
  })
}
```

---

## MIME 类型判断

```typescript
private getMimeType(medium: Medium): string {
  if ((medium.type & TYPE_VIDEOS) !== 0) {
    return 'video/*'
  }
  if ((medium.type & TYPE_IMAGES) !== 0) {
    return 'image/*'
  }
  return '*/*'
}
```

---

## SharePreviewMode 配置

| 模式 | 效果 |
|------|------|
| `DETAIL` | 显示详情预览（推荐） |
| `NONE` | 不显示预览 |

## SelectionMode 配置

| 模式 | 效果 | 验证状态 |
|------|------|---------|
| `SINGLE` | 单选分享 | ✅ 已验证（ViewPagerPage.ets） |
| `MULTIPLE` | 多选分享 | ⚠️ 未验证 |

---

## module.json5 配置

### 配置规则

| 分享内容类型 | 是否需要配置 | 说明 |
|------------|------------|------|
| 图片/视频/文件 | 通常不需要 | 系统已内置支持 |
| 纯文本 | 需要配置 | 需声明 `ohos.want.action.send` |
| 自定义数据 | 需要配置 | 需声明 `ohos.want.action.send` |

### 配置示例（纯文本/自定义数据）

```json5
{
  "skills": [{
    "entities": ["entity.system.home"],
    "actions": [
      "ohos.want.action.home",
      "ohos.want.action.send"    // 发送数据
    ]
  }]
}
```

> ⚠️ **注意**：虽然图片/视频分享通常不需要额外声明，但某些设备可能需要。如遇分享失败，建议添加 `ohos.want.action.send` 配置。

---

## 常见错误

### 错误 1：不转换 UTD 直接传 MIME

```typescript
// 错误 — 部分设备不支持
const shareData = new systemShare.SharedData({
  mimeType: 'image/*',  // ❌
  uri: uri,
  title: title
})

// 正确 — 使用 UTD
const utdTypeId = utd.getUniformDataTypeByFilenameExtension('.' + ext, utd.UniformDataType.IMAGE)
const shareData = new systemShare.SharedData({
  utd: utdTypeId,
  uri: uri,
  title: title
})
```

### 错误 2：show() 后不 await

`controller.show()` 是异步的，但不会阻塞 UI。不需要 await，但错误需要通过 catch 处理。
