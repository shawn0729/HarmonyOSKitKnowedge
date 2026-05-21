---
name: share-kit-development
description: 用于内容分享业务，包括系统分享面板、应用发起分享、目标应用接收分享、文本/图片/视频/链接分享、碰一碰分享、隔空传送、分享结果处理和分享失败排查；需要实现或排查 HarmonyOS 分享能力时应使用。
---

# Share Kit 开发

## 业务场景入口

本 skill 是 `arkts-skills-codex` 中的独立内容分享业务能力入口，与融合型宿主 skill 并列。

当需求涉及系统分享、应用内发起分享、目标应用处理分享内容、分享面板、跨设备分享、碰一碰分享或隔空传送时，直接使用本 skill。

本 skill 负责 Share Kit 业务方案、分享数据建模、分享面板、目标应用处理、跨设备分享、异常排查和知识路由；不负责页面整体搭建、工程脚手架、构建修复或整体工程编排。

事实依据以 `sources/Share Kit Full.md` 为准。

## 默认工作方式

1. 先识别请求的主主题：
   - 系统分享
   - 宿主应用发起分享
   - 目标应用处理分享内容
   - 常见分享场景
   - 碰一碰分享
   - 手机与手机碰一碰分享
   - 手机与PC/2in1碰一碰分享
   - 隔空传送
   - 最佳实践与FAQ
2. 再补充 0 到 2 个补充主题。
3. 默认按以下顺序组织资料：
   - 开发指南
   - API 参考
   - 最佳实践
   - FAQ
4. 回答默认先给推荐实现方式，再给原因、代码示例、文档入口。

## 业务场景

当用户需求属于以下任一业务场景时应使用本 skill：

- 文本、图片、视频、链接、文件等内容分享
- 系统分享面板、自定义操作区、目标应用名单和分享结果处理
- 目标应用接收分享内容、分享详情页处理和分享后回跳
- 碰一碰分享、手机与 PC/2in1 分享、隔空传送和可信设备传输
- 分享数据类型不支持、分享面板拉起失败、文件无法分享等异常排查

## 主题路由规则

主题路由规则如下：

- 概览与路由：优先读取 `references/overview-and-routing.md`
- Share Kit（分享服务）：优先读取 `references/share-kit.md`
- Share Kit：优先读取 `references/share-kit.md`
- Share Kit术语：优先读取 `references/share-kit.md`
- Share Kit体验规范：优先读取 `references/share-kit.md`
- 系统分享：优先读取 `references/system-share.md`
- 宿主应用发起分享：优先读取 `references/host-app-sharing.md`
- 目标应用处理分享内容：优先读取 `references/target-app-share-handling.md`
- 常见分享场景：优先读取 `references/common-share-scenarios.md`
- 碰一碰分享：优先读取 `references/knock-share.md`
- 手机与手机碰一碰分享：优先读取 `references/phone-to-phone-knock-share.md`
- 手机与PC/2in1碰一碰分享：优先读取 `references/phone-to-pc-2in1-knock-share.md`
- 隔空传送：优先读取 `references/air-transfer.md`
- 最佳实践与FAQ：优先读取 `references/best-practices-and-faq.md`
- API与错误码：优先读取 `references/api-and-error-codes.md`

当 `references/*.md` 的信息不足时，再回到 `sources/Share Kit Full.md`。

## 代码生成约束

- 涉及接口或错误定位时，优先给出 API 与错误码入口，再补充实现建议
- 涉及排障或适配问题时，优先结合 FAQ 与最佳实践做纠偏

## 回答结构

1. 推荐实现方式
2. 为什么这样选
3. 代码或使用示例
4. 对应开发指南入口
5. 相关 API 入口
6. 如有必要，再补充最佳实践或 FAQ

## 边界

- 本 skill 的事实依据以 `sources/Share Kit Full.md` 为准
- `references/*.md` 是首选路由索引，不替代事实源
- 不退化成单纯的链接列表
- 不输出脱离当前 kit 语境的泛化 HarmonyOS 建议
