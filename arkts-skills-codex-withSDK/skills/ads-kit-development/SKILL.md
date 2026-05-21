---
name: ads-kit-development
description: 用于广告变现业务，包括横幅广告、原生广告、激励广告、插屏广告、开屏广告、贴片广告、实时竞价、广告展示异常和设备标识相关问题；需要实现或排查 HarmonyOS 广告能力时应使用。
---

# Ads Kit 开发

## 业务场景入口

本 skill 是 `arkts-skills-codex` 中的独立广告变现业务能力入口，与融合型宿主 skill 并列。

当需求涉及广告投放、广告位接入、广告展示、广告收益、实时竞价、广告加载失败、广告白屏、设备标识或广告合规说明时，直接使用本 skill。

本 skill 负责 Ads Kit 业务方案、配置要点、展示链路、异常排查和知识路由；不负责页面整体搭建、工程脚手架、构建修复或整体工程编排。

事实依据以 `sources/Ads Kit Full.md` 为准。

## 默认工作方式

1. 先识别请求的主主题：
   - 开发准备
   - 流量变现服务开发
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

- 广告流量变现、广告位规划和广告服务接入
- 横幅、原生、激励、插屏、开屏、贴片等广告展示场景
- 实时竞价、广告请求、广告加载和广告展示状态处理
- 广告展示异常、白屏、设备侧限制和投放失败排查
- 匿名设备标识、广告合规说明和个人数据处理相关问题

## 主题路由规则

主题路由规则如下：

- 概览与路由：优先读取 `references/overview-and-routing.md`
- Ads Kit（广告服务）：优先读取 `references/ads-kit.md`
- Ads Kit：优先读取 `references/ads-kit.md`
- Ads Kit术语：优先读取 `references/ads-kit.md`
- 开发准备：优先读取 `references/topic-23ff0dd5.md`
- 流量变现服务开发：优先读取 `references/topic-c05e90e0.md`
- 最佳实践与FAQ：优先读取 `references/best-practices-and-faq.md`
- API与错误码：优先读取 `references/api-and-error-codes.md`

当 `references/*.md` 的信息不足时，再回到 `sources/Ads Kit Full.md`。

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

- 本 skill 的事实依据以 `sources/Ads Kit Full.md` 为准
- `references/*.md` 是首选路由索引，不替代事实源
- 不退化成单纯的链接列表
- 不输出脱离当前 kit 语境的泛化 HarmonyOS 建议
