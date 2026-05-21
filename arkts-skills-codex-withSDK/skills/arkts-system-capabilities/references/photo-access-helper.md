# photoAccessHelper 媒体查询指南

> HarmonyOS 媒体库访问的完整使用模式，替代 Android 的 MediaStore + ContentProvider。

---

## 基本导入与初始化

```typescript
import { photoAccessHelper } from '@kit.MediaLibraryKit'
import { dataSharePredicates } from '@kit.ArkData'

const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context)
```

---

## 查询媒体资源

```typescript
async function getMediaAssets(context: Context): Promise<photoAccessHelper.PhotoAsset[]> {
  const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context)

  const fetchOptions: photoAccessHelper.FetchOptions = {
    fetchColumns: [
      photoAccessHelper.PhotoKeys.URI,
      photoAccessHelper.PhotoKeys.DISPLAY_NAME,
      photoAccessHelper.PhotoKeys.SIZE,
      photoAccessHelper.PhotoKeys.DATE_ADDED,
      photoAccessHelper.PhotoKeys.DURATION,
      photoAccessHelper.PhotoKeys.WIDTH,
      photoAccessHelper.PhotoKeys.HEIGHT,
      photoAccessHelper.PhotoKeys.PHOTO_TYPE,
    ],
    predicates: new dataSharePredicates.DataSharePredicates()
  }

  const fetchResult = await phAccessHelper.getAssets(fetchOptions)
  const count = fetchResult.getCount()
  const assets: photoAccessHelper.PhotoAsset[] = []

  if (count > 0) {
    let asset = await fetchResult.getFirstObject()
    let index = 0
    while (index < count) {
      assets.push(asset)
      index++
      if (index < count) {
        asset = await fetchResult.getNextObject()
      }
    }
  }

  fetchResult.close()  // 必须关闭！
  return assets
}
```

---

## FetchResult 遍历模式（关键）

**FetchResult 不是数组**，是游标式迭代器。必须按以下模式遍历：

```typescript
// ✅ 正确模式
let asset = await fetchResult.getFirstObject()
let index = 0
while (index < count) {
  // 处理 asset
  processAsset(asset)
  index++
  if (index < count) {
    asset = await fetchResult.getNextObject()
  }
}
fetchResult.close()  // 必须关闭

// ❌ 错误 — 不能用 for...of
for (const asset of fetchResult) { ... }  // 不支持

// ❌ 错误 — 不能一次性获取全部
const allAssets = await fetchResult.getAllObjects()  // 大量数据会内存溢出
```

---

## 获取文件 URI

```typescript
// 获取资源 URI（可用于 Image 组件显示）
const uri = asset.uri  // 格式: file://media/Photo/xxx

// ⚠️ 视频 URI 不能传给 Image 组件（会显示灰色空白）
// 图片 URI 可以直接传给 Image 组件
Image(asset.uri)
  .sourceSize({ width: 256, height: 256 })  // 缩略图优化
```

---

## 按类型筛选

```typescript
// 只查图片
const predicates = new dataSharePredicates.DataSharePredicates()
predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_TYPE, photoAccessHelper.PhotoType.IMAGE)

// 只查视频
predicates.equalTo(photoAccessHelper.PhotoKeys.PHOTO_TYPE, photoAccessHelper.PhotoType.VIDEO)
```

---

## 权限要求

媒体库访问需要声明权限：

```json5
// module.json5
"requestPermissions": [
  {
    "name": "ohos.permission.READ_IMAGEVIDEO",
    "reason": "$string:permission_read_media_reason",
    "usedScene": {
      "abilities": ["EntryAbility"],
      "when": "inuse"
    }
  }
]
```

并在运行时用 `abilityAccessCtrl` 动态请求（见 permission-helper.md）。
