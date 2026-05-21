# 代码生成约束

## 默认回答顺序

1. 推荐实现方式
2. 为什么这样选
3. 代码或使用示例
4. 对应开发指南入口
5. 相关 API 入口
6. 如有必要，再补充最佳实践或 FAQ

## 优先机制

- Form Kit（卡片开发服务）
- Form Kit
- ArkTS卡片开发
- ArkTS卡片
- 创建ArkTS卡片
- 配置ArkTS卡片的配置文件
- 管理ArkTS卡片生命周期
- ArkTS卡片页面刷新
- ArkTS卡片主动刷新
- ArkTS卡片被动刷新
- ArkTS卡片页面交互
- ArkTS卡片适配
- 音乐服务卡片
- FormExtensionAbility
- FormEditExtensionAbility
- 卡片错误码

## 常见误区规避

- 不要在未区分主动刷新和被动刷新的情况下直接给出刷新方案
- 涉及页面跳转时先区分 router、call、message 交互路径
- 不要跳过卡片配置文件和生命周期约束直接生成卡片实现
- 涉及接口或错误定位时先给 API 与错误码入口，再补代码建议

## 不确定时的回退策略

- 先给当前最稳妥的推荐实现
- 再列出最相关的开发指南、API、最佳实践或 FAQ 入口
