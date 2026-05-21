---
name: crypto-architecture-kit-development
description: 用于加密安全业务，包括密钥生成与转换、加解密、签名验签、密钥协商、消息摘要、消息认证码、安全随机数、密钥派生、跨平台密文兼容和加密失败排查；需要实现或排查 HarmonyOS 加密能力时应使用。
---

# Crypto Architecture Kit 开发

## 业务场景入口

本 skill 是 `arkts-skills-codex` 中的独立加密安全业务能力入口，与融合型宿主 skill 并列。

当需求涉及数据加密、数据解密、密钥管理、签名验签、密钥协商、摘要校验、消息认证、安全随机数、密钥派生或跨平台密文兼容时，直接使用本 skill。

本 skill 负责 Crypto Architecture Kit 业务方案、算法选择、数据格式、兼容策略、异常排查和知识路由；不负责业务协议设计、服务端改造、工程脚手架、构建修复或整体工程编排。

事实依据以 `sources/Crypto Architecture Kit.md` 为准。

## 默认工作方式

1. 先识别请求的主主题：
   - 密钥生成和转换
   - 密钥生成和转换规格
   - 密钥生成和转换开发指导
   - 加解密
   - 加解密算法规格
   - 加解密开发指导
   - 签名验签
   - 签名验签开发指导
   - 密钥协商
   - 密钥协商开发指导
   - 消息摘要计算
   - 消息摘要计算开发指导
   - 消息认证码
   - 随机数
   - 密钥派生
   - 跨平台数据兼容实践指导
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

- 本地敏感数据加密、网络载荷加密、文件内容加密和密文解密
- 对称密钥、非对称密钥、密钥导入导出、密钥格式转换和密钥包装
- 数字签名、签名校验、摘要校验、消息认证和防篡改校验
- 密钥协商、安全随机数、密钥派生和会话密钥生成
- 跨平台密文、签名、公钥私钥、摘要结果的格式兼容
- 加解密失败、验签失败、密文格式不匹配和算法能力差异排查

## 主题路由规则

主题路由规则如下：

- 概览与路由：优先读取 `references/overview-and-routing.md`
- Crypto Architecture Kit（加解密算法框架服务）：优先读取 `references/crypto-architecture-kit.md`
- Crypto Architecture Kit：优先读取 `references/crypto-architecture-kit.md`
- 密钥生成和转换：优先读取 `references/topic-e7a37a4c.md`
- 密钥生成和转换规格：优先读取 `references/topic-f29df0c9.md`
- 密钥生成和转换开发指导：优先读取 `references/topic-73f6d990.md`
- 加解密：优先读取 `references/topic-93b13c0b.md`
- 加解密算法规格：优先读取 `references/topic-3f69fcf8.md`
- 加解密开发指导：优先读取 `references/topic-b269997c.md`
- 签名验签：优先读取 `references/topic-37c48bae.md`
- 签名验签开发指导：优先读取 `references/topic-dea5b287.md`
- 密钥协商：优先读取 `references/topic-7f49bf0c.md`
- 密钥协商开发指导：优先读取 `references/topic-966a788d.md`
- 消息摘要计算：优先读取 `references/topic-64238e20.md`
- 消息摘要计算开发指导：优先读取 `references/topic-eb6e73a9.md`
- 消息认证码：优先读取 `references/topic-9088e9bc.md`
- 随机数：优先读取 `references/topic-5bfedcff.md`
- 密钥派生：优先读取 `references/topic-b535db4c.md`
- 跨平台数据兼容实践指导：优先读取 `references/topic-a70c4d21.md`
- 最佳实践与FAQ：优先读取 `references/best-practices-and-faq.md`
- API与错误码：优先读取 `references/api-and-error-codes.md`

当 `references/*.md` 的信息不足时，再回到 `sources/Crypto Architecture Kit.md`。

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

- 本 skill 的事实依据以 `sources/Crypto Architecture Kit.md` 为准
- `references/*.md` 是首选路由索引，不替代事实源
- 不退化成单纯的链接列表
- 不输出脱离当前 kit 语境的泛化 HarmonyOS 建议
