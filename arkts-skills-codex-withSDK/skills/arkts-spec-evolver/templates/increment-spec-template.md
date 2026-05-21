---
id: {{ id }}
type: {{ type }}                    # feature | bugfix | optimization
title: {{ title }}
priority: {{ priority }}            # P0/P1/P2
status: pending                     # pending | planned | in_progress | verifying | done | failed | deprecated
created: {{ date }}
source: {{ source }}                # issue #N / 用户反馈 / 测试发现 / 审计发现
affects:
  - L1: {{ sections }}
  - L2: {{ sections }}
  - L3: {{ sections }}
# deprecated_by:                   # 被哪个增量替代（废弃时填写）
# deprecated_reason:               # 废弃原因（废弃时填写）
---

## 背景

<!-- 为什么需要这个变更 -->

## 复现步骤

<!-- bugfix 类型专用，其他类型删除此节 -->
1. ...

## 根因分析

<!-- bugfix 类型专用，其他类型删除此节 -->

## 变更描述

### 对 L1 的影响
<!-- 如不影响 L1，删除此节 -->

### 对 L2 的影响
<!-- 如不影响 L2，删除此节 -->

### 对 L3 的影响
<!-- 如不影响 L3，删除此节 -->

## 实现指引

<!-- 具体实现方案、注意事项、参考踩坑 -->

## 验收标准

- [ ] 验收条件 1
- [ ] 验收条件 2

## 实现计划

<!-- spec-evolver plan 阶段自动生成 -->
- plan 文件:
- task 数量:
- 复杂度: 完整流程 / 简化流程

## 执行记录

<!-- spec-evolver execute 阶段自动填充 -->
- 执行时间:
- 触发 skill:
- 修改文件:
- commit:

## 验证记录

<!-- spec-evolver verify 阶段自动填充 -->
- 编译验证: ✅/❌
- 验收验证: X/Y 项通过
- 回归验证: ✅/❌
- 验证时间:

## 回退记录

<!-- 仅在验证失败回退时填充 -->
