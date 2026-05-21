---
name: form-kit-development
description: 用于服务卡片业务，包括桌面卡片、卡片提供方、卡片配置、生命周期、刷新、跳转、消息交互、卡片适配和卡片异常排查；需要实现或排查 HarmonyOS 卡片能力时应使用。
---

# Form Kit 开发

## 业务场景入口

本 skill 是 `arkts-skills-codex` 中的独立服务卡片业务能力入口，与融合型宿主 skill 并列。

当需求涉及桌面服务卡片、卡片提供方、卡片配置、卡片生命周期、卡片刷新、卡片跳转或卡片消息交互时，直接使用本 skill。

本 skill 负责 Form Kit 业务方案、配置要点、生命周期、交互刷新、异常排查和知识路由；不负责应用页面整体搭建、工程脚手架、构建修复或整体工程编排。

事实依据以 `sources/form-kit-full.md` 为准。

## 默认工作方式

1. 先识别请求的主主题：
   - ArkTS卡片开发
   - 提供方生命周期与配置
   - 管理ArkTS卡片生命周期
   - 卡片刷新与交互
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

- 服务卡片创建、配置、发布和适配
- 卡片提供方生命周期、卡片数据准备和卡片状态维护
- 卡片主动刷新、被动刷新、定时更新和数据交互
- 卡片跳转应用页面、卡片内事件和消息交互
- 音乐、资讯、工具等桌面卡片业务和卡片异常排查

## 主题路由规则

主题路由规则如下：

- 概览与路由：优先读取 `references/overview-and-routing.md`
- Form Kit（卡片开发服务）：优先读取 `references/form-kit.md`
- Form Kit：优先读取 `references/form-kit.md`
- ArkTS卡片开发：优先读取 `references/arkts.md`
- 提供方生命周期与配置：优先读取 `references/provider-lifecycle-and-config.md`
- 管理ArkTS卡片生命周期：优先读取 `references/arkts.md`
- 卡片刷新与交互：优先读取 `references/card-refresh-and-interaction.md`
- 最佳实践与FAQ：优先读取 `references/best-practices-and-faq.md`
- API与错误码：优先读取 `references/api-and-error-codes.md`

当 `references/*.md` 的信息不足时，再回到 `sources/form-kit-full.md`。

## 代码生成约束

- 涉及卡片创建、配置、生命周期时，必须先判断卡片配置文件、提供方生命周期和卡片类型
- 涉及卡片刷新、跳转、消息交互时，必须先区分主动刷新、被动刷新以及 router / call / message 事件
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

- 本 skill 的事实依据以 `sources/form-kit-full.md` 为准
- `references/*.md` 是首选路由索引，不替代事实源
- 不退化成单纯的链接列表
- 不输出脱离当前 kit 语境的泛化 HarmonyOS 建议
