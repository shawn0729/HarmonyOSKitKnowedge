# API Corrections

> **This file is auto-maintained by `a2h-retrospect`.**
> Manual edits are allowed but may be overwritten when retrospect detects updated corrections.
> Last updated: 2026-03-27

---

## Correction Index

| # | Category | Error | Correction |
|---|----------|-------|------------|
| 1 | Import Path | `@ohos.*` imports | `@kit.XxxKit` imports |
| 2 | API Name | `ShowActionMenuSuccessResponse` | `ActionMenuSuccessResponse` |

---

## 1. @ohos Import Path Deprecation

- **Date**: 2026-03-27
- **Category**: Import path
- **Source**: AntennaPod V1 migration (a2h-retrospect-report-2026-03-27)

**Error code**:
```typescript
import rdb from '@ohos.data.relationalStore';
import http from '@ohos.net.http';
import fileIo from '@ohos.file.fs';
```

**Correct code**:
```typescript
import { relationalStore } from '@kit.ArkData';
import { http } from '@kit.NetworkKit';
import { fileIo } from '@kit.CoreFileKit';
```

**Rule**: All `@ohos.*` import paths are deprecated since API 11. Use the corresponding `@kit.XxxKit` bundle import instead. Common mappings:

| Deprecated `@ohos.*` | Replacement `@kit.*` |
|----------------------|---------------------|
| `@ohos.data.relationalStore` | `@kit.ArkData` |
| `@ohos.data.preferences` | `@kit.ArkData` |
| `@ohos.net.http` | `@kit.NetworkKit` |
| `@ohos.file.fs` | `@kit.CoreFileKit` |
| `@ohos.promptAction` | `@kit.ArkUI` |
| `@ohos.router` | `@kit.ArkUI` |
| `@ohos.multimedia.media` | `@kit.MediaKit` |
| `@ohos.backgroundTaskManager` | `@kit.BackgroundTasksKit` |
| `@ohos.request` | `@kit.BasicServicesKit` |
| `@ohos.xml` | `@kit.ArkTS` |

---

## 2. promptAction API Name: ShowActionMenuSuccessResponse

- **Date**: 2026-03-27
- **Category**: API name
- **Source**: AntennaPod V1 migration (a2h-retrospect-report-2026-03-27)

**Error code**:
```typescript
import { promptAction } from '@kit.ArkUI';

promptAction.showActionMenu({...}).then((result: promptAction.ShowActionMenuSuccessResponse) => {
  // ERROR: ShowActionMenuSuccessResponse does not exist
});
```

**Correct code**:
```typescript
import { promptAction } from '@kit.ArkUI';

promptAction.showActionMenu({...}).then((result: promptAction.ActionMenuSuccessResponse) => {
  // Correct type name
});
```

**Rule**: The response type for `promptAction.showActionMenu()` is `ActionMenuSuccessResponse`, not `ShowActionMenuSuccessResponse`. The `Show` prefix does not appear in the type name.
