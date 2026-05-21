---
name: harmonyos-development
description: Use when the task involves HarmonyOS development questions covered by local best-practice or FAQ docs, including ArkTS, ArkUI, Ability/UIAbility/framework, package/module/HAP/HAR/HSP, camera, image, audio/video media, web, network, data/file storage, account/login, AppGallery/IAP, forms, notifications, background tasks, performance, scan, sensor, share, telephony, crypto, and troubleshooting.
---

# HarmonyOS 开发

本 skill 用于从本地 HarmonyOS 开发资料中路由到对应原文。资料按能力领域组织；每个领域再分最佳实践和 FAQ。

## 默认工作流

1. 先根据用户问题从资料入口选择能力领域目录。
2. 再判断资料类型：
   - 完整功能、方案设计、端到端流程：读取该领域的 `best-practices-routing.md`。
   - 具体问题、异常、参数、配置、能力点：读取该领域的 `faq-routing.md`。
   - 不确定时同一领域下两份路由都读。
3. 如果路由文件是子路由入口，先读取对应主题子路由。
4. 二级路由只使用 Markdown 一级标题作为关键词，不人工扩展同义词、不使用自己总结的触发词。
5. 命中标题后，必须读取 `sources/` 下对应原始 Markdown，再回答或生成代码。
6. 路由文件只负责指路，不替代原文。

## 资料入口

- 账号与登录：`references/account-authentication/`
- 广告与流量变现：`references/ads-monetization/`
- 应用市场服务：`references/appgallery-services/`
- Ability/程序框架：`references/ability-framework/`
- 数据管理：`references/data-management/`
- ArkTS 编程语言：`references/arkts-language/`
- ArkUI 开发：`references/arkui-development/`
- Web 开发：`references/web-development/`
- 后台任务：`references/background-tasks/`
- 基础服务：`references/basic-services/`
- 相机开发：`references/camera-development/`
- 文件管理：`references/file-management/`
- 加解密算法框架：`references/crypto-architecture/`
- 卡片开发：`references/form-development/`
- 应用内支付：`references/in-app-purchases/`
- 图片处理：`references/image-processing/`
- 媒体开发（音频和视频）：`references/media-development/`
- 媒体文件管理：`references/media-library/`
- 网络开发：`references/network-development/`
- 用户通知：`references/notification-development/`
- 性能分析：`references/performance-analysis/`
- 扫码服务：`references/scan-code/`
- 传感器服务：`references/sensor-service/`
- 分享服务：`references/share-service/`
- 蜂窝通信：`references/telephony-service/`
- 原始资料：`sources/`
- 代码生成检查：`templates/code-generation.md`

## 路由规则

- 一级领域直接从资料入口选择。
- FAQ 资料量较大的领域会先进入子路由入口，例如 `references/arkui-development/faq-routing.md`。
- 二级路由关键词必须来自对应 Markdown 的第一个 `# 标题`。
- 如果用户问题与多个标题接近，优先读取最具体的标题；仍不确定时读取多个候选原文。
- 如果标题没有覆盖用户问题，不要猜测有对应资料；说明未命中本地标题路由。
- 回答中可以基于已读取原文总结方案，但不能把路由文件当作事实源。

## 边界

- 不按 Kit 名称建立一级路由，避免与 API 或产品名混淆。
- 不在二级路由中维护人工总结的“场景锚点”或“API 线索”。
- 不用文件名替代标题；标题必须来自 Markdown 正文的 `# 标题`。
