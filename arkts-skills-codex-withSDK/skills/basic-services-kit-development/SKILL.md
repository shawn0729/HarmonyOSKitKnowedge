---
name: basic-services-kit-development
description: 用于基础系统服务业务，包括公共事件通信、线程事件通信、账号管理、设备信息、电源热管理、USB 与串口、剪贴板、上传下载、压缩解压、打印扫描、系统时间和基础服务异常排查；需要实现或排查 HarmonyOS 基础服务能力时应使用。
---

# Basic Services Kit 开发

## 业务场景入口

本 skill 是 `arkts-skills-codex` 中的独立基础系统服务业务能力入口，与融合型宿主 skill 并列。

当需求涉及系统基础服务、跨进程/线程事件、账号、设备、电源、热管理、USB、剪贴板、上传下载、压缩解压、打印扫描或系统时间时，直接使用本 skill。

本 skill 负责 Basic Services Kit 业务方案、能力选型、权限与配置要点、异常排查和知识路由；不负责页面整体搭建、工程脚手架、构建修复或整体工程编排。

事实依据以 `sources/Basic Services Kit.md` 为准。

## 默认工作方式

1. 先识别请求的主主题：
   - 进程线程通信
   - 使用公共事件进行进程间通信
   - 账号管理
   - 应用账号
   - USB服务
   - 开发USB服务
   - USB Host模式开发
   - 开发USB串口通信服务
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

- 公共事件、跨进程事件、线程事件和应用内消息分发
- 应用账号、系统账号、设备信息、系统版本和设备标识相关能力
- USB 外设、USB Host、串口通信和外设数据传输
- 剪贴板、上传下载、缓存下载、压缩解压、打印和扫描
- 电源管理、亮屏休眠控制、热管理、系统时间、时区和系统设置
- 基础服务权限、能力兼容、服务调用失败和系统行为异常排查

## 主题路由规则

主题路由规则如下：

- 概览与路由：优先读取 `references/overview-and-routing.md`
- Basic Services Kit（基础服务）：优先读取 `references/basic-services-kit.md`
- Basic Services Kit：优先读取 `references/basic-services-kit.md`
- 进程线程通信：优先读取 `references/topic-1f0e778d.md`
- 使用公共事件进行进程间通信：优先读取 `references/topic-0af7d6b4.md`
- 账号管理：优先读取 `references/topic-b829fe77.md`
- 应用账号：优先读取 `references/topic-c1289e55.md`
- USB服务：优先读取 `references/usb.md`
- 开发USB服务：优先读取 `references/usb.md`
- USB Host模式开发：优先读取 `references/usb-host.md`
- 开发USB串口通信服务：优先读取 `references/usb.md`
- 最佳实践与FAQ：优先读取 `references/best-practices-and-faq.md`
- API与错误码：优先读取 `references/api-and-error-codes.md`

当 `references/*.md` 的信息不足时，再回到 `sources/Basic Services Kit.md`。

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

- 本 skill 的事实依据以 `sources/Basic Services Kit.md` 为准
- `references/*.md` 是首选路由索引，不替代事实源
- 不退化成单纯的链接列表
- 不输出脱离当前 kit 语境的泛化 HarmonyOS 建议
