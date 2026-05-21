# HarmonyOS Development Skill 设计说明

本文档记录当前 `harmonyos-development` skill 的设计思路、目录结构和维护规则。

如果需要按系统架构方式阅读设计，可参考 [HarmonyOS Development Skill 4+1 架构视图](ARCHITECTURE-4+1.md)。

## 目标

这个 skill 用于让模型在生成或排查 HarmonyOS 代码时，先从本地文档中定位对应资料，再基于原文回答或生成代码。

当前覆盖 25 个能力领域，包括 ArkTS、ArkUI、Ability/程序框架、程序包结构、相机、图片、音视频媒体、Web、网络、数据和文件、账号登录、应用市场、支付、卡片、通知、后台任务、性能分析、扫码、传感器、分享、蜂窝通信、加解密等。

设计重点不是把文档内容重新加工成知识库，而是建立稳定、可扩展的路由层，让模型在需要时能准确访问对应 Markdown 原文。

## 核心设计

### 1. 不按 Kit 名称做一级路由

不使用 `Camera Kit`、`Image Kit`、`Account Kit` 这类 Kit 名称作为 skill 或一级目录命名，避免和 HarmonyOS API、产品名、用户问题中的 Kit 名称混淆。

一级入口改为能力领域，例如：

- `camera-development`：相机开发
- `image-processing`：图片处理
- `ability-framework`：Ability/程序框架
- `account-authentication`：账号与登录
- `data-management`：数据管理
- `network-development`：网络开发

这样后续增加其他资料时，可以继续按开发主题扩展，而不是把路由绑定到 Kit 名称。

### 2. 最佳实践和 FAQ 分开路由

每个领域都拆成两类资料：

- `best-practices-routing.md`：用于完整功能、方案设计、端到端流程。
- `faq-routing.md`：用于具体问题、异常、参数、配置、能力点和排障。

模型收到问题后先判断资料类型：

- 用户问“怎么实现某个功能”“完整流程怎么写”“有没有方案”：优先查最佳实践。
- 用户问“为什么报错”“某个属性怎么设置”“某个效果怎么处理”：优先查 FAQ。
- 如果边界不清晰，同一领域下最佳实践和 FAQ 都可以查。

### 3. 二级关键词只来自 Markdown 标题

二级路由文件里的关键词不人工总结，不维护“场景锚点”或“API 线索”。

每条路由只使用对应 Markdown 原文的第一个 `# 标题` 作为关键词来源。这样做的原因：

- 降低人为改写带来的偏差。
- 让路由和源文档保持可验证的一一对应关系。
- 后续批量新增资料时，可以通过脚本从标题生成路由，不需要人工维护大量触发词。

### 4. 路由文件只指路，不替代原文

`references/` 下的路由文件只负责告诉模型应该读取哪篇源文档。

命中路由后，模型必须读取 `sources/` 下对应的 Markdown 原文，再进行总结、排障或代码生成。

这样可以避免模型只看标题或摘要就回答，减少误判和幻觉。

## 当前目录结构

```text
skills/harmonyos-development/
  SKILL.md
  README.md
  references/
    <能力领域>/
      best-practices-routing.md
      faq-routing.md
      faq/
        <主题>-routing.md
  sources/
    <能力领域>/
      best-practices/
      faq/
    _assets/
      images/
      offline-image-report.md
  templates/
    code-generation.md
```

不是每个能力领域都同时具备最佳实践和 FAQ；没有对应资料时，不生成对应路由文件。资料量较大的 FAQ 会生成 `faq/` 子路由目录，总入口只负责指向子路由。

## 能力领域入口

| 能力领域 | 路由目录 |
| --- | --- |
| 账号与登录 | `references/account-authentication/` |
| 广告与流量变现 | `references/ads-monetization/` |
| 应用市场服务 | `references/appgallery-services/` |
| Ability/程序框架 | `references/ability-framework/` |
| 数据管理 | `references/data-management/` |
| ArkTS 编程语言 | `references/arkts-language/` |
| ArkUI 开发 | `references/arkui-development/` |
| Web 开发 | `references/web-development/` |
| 后台任务 | `references/background-tasks/` |
| 基础服务 | `references/basic-services/` |
| 相机开发 | `references/camera-development/` |
| 文件管理 | `references/file-management/` |
| 加解密算法框架 | `references/crypto-architecture/` |
| 卡片开发 | `references/form-development/` |
| 应用内支付 | `references/in-app-purchases/` |
| 图片处理 | `references/image-processing/` |
| 媒体开发（音频和视频） | `references/media-development/` |
| 媒体文件管理 | `references/media-library/` |
| 网络开发 | `references/network-development/` |
| 用户通知 | `references/notification-development/` |
| 性能分析 | `references/performance-analysis/` |
| 扫码服务 | `references/scan-code/` |
| 传感器服务 | `references/sensor-service/` |
| 分享服务 | `references/share-service/` |
| 蜂窝通信 | `references/telephony-service/` |

## 入口文件

主入口是：

```text
skills/harmonyos-development/SKILL.md
```

入口文件只保留必要工作流：

1. 先选能力领域。
2. 再选资料类型：最佳实践或 FAQ。
3. 如果路由文件是子路由入口，先读取对应主题子路由。
4. 从路由文件中用标题命中源文档。
5. 读取 `sources/` 下的原始 Markdown。
6. 基于原文回答或生成代码。

## 图片离线化

为了让 skill 在离线环境下可用，Markdown 图片引用已经本地化。

- 本地图片目录：`skills/harmonyos-development/sources/_assets/images/`
- 离线化报告：`skills/harmonyos-development/sources/_assets/offline-image-report.md`
- GIF 首帧 WebP 转换报告：`skills/harmonyos-development/sources/_assets/gif-first-frame-webp-report.md`
- PNG Lossless WebP 转换报告：`skills/harmonyos-development/sources/_assets/png-lossless-webp-report.md`
- 原始图片备份目录：`original-images/`
- 当前离线图片数量：1205 个

Markdown 中的远程图片链接已替换为相对路径，例如：

```md
![](../../_assets/images/example.webp)
```

代码示例里的网络图片 URL 不做替换，避免改变示例代码语义。

可复用脚本：

```text
scripts/offline_markdown_images.py
scripts/replace_gif_with_first_frame_webp.py
scripts/replace_png_with_lossless_webp.py
```

## 当前资料规模

- 业务源文档：1004 篇
- 路由文件：57 个
- 离线图片：1205 个
- assets 图片目录体积：约 155M
- 原始图片备份：1168 个，约 2.6G，位于 `original-images/`
- 覆盖领域：25 个能力领域
- 单个路由文件当前最大 130 行；超过 160 行的 FAQ 路由需要拆分为子路由。

## 维护规则

新增资料时按以下规则处理：

1. 先把整理好的 Kit 资料放在仓库顶层对应原始目录中；也可以在脚本中配置绝对路径来源。
2. 在 `scripts/integrate_kit_knowledge.py` 中维护 Kit 原始目录到能力领域的映射。当前 `media-development` 使用 `/media/wxjshr/wxj/zxy/code/bestAndFAQTool/extracted-docs/Media-Kit（媒体服务）`，不再使用旧 `Audio-Kit（音频服务）` 和旧 `Media-Kit（媒体服务）`。
3. 执行 `python3 scripts/integrate_kit_knowledge.py`，将 Markdown 复制到 `sources/<领域>/<best-practices|faq>/` 并生成路由。
4. 执行 `python3 scripts/offline_markdown_images.py skills/harmonyos-development`，离线化远程图片并更新报告。
5. 执行 `python3 scripts/replace_gif_with_first_frame_webp.py --backup-dir original-images`，将 GIF 替换为首帧 WebP，并把原始 GIF 按同名文件备份。
6. 执行 `python3 scripts/replace_png_with_lossless_webp.py --backup-dir original-images`，将 PNG 替换为 lossless WebP，并把原始 PNG 按同名文件备份。
7. 路由关键词只从每篇 Markdown 的第一个 `# 标题` 抽取。
8. 不新增人工总结的触发词、场景锚点、API 线索。
9. 不把路由文件当作事实源，回答前必须读取原文。
10. 如果单个 FAQ 路由超过 160 行，在 `scripts/integrate_kit_knowledge.py` 中配置子路由分组。

## 适用问题示例

模型遇到以下问题时，应进入这个 skill：

- “我想做相机预览功能，怎么做？”
- “自定义 Tabs 页签怎么做？”
- “ArkTS 中 TaskPool 和 Worker 有什么区别？”
- “UIAbility 的生命周期或 Context 怎么获取？”
- “HAP、HAR、HSP 的关系是什么？”
- “RDB 数据库查询失败怎么排查？”
- “网络请求 401 如何处理？”
- “图片保存到相册失败怎么排查？”
- “音频播放或录制怎么实现？”
- “卡片刷新失败怎么排查？”

这些示例不是固定触发词，只用于说明路由思路。真正的二级命中仍以 Markdown 标题路由为准。

## 验证

当前 skill 需要通过结构校验：

```bash
python3 /home/wxjshr/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/harmonyos-development
```

期望输出：

```text
Skill is valid!
```
