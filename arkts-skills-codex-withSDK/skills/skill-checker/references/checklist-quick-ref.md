# 合规检查速查表

本文件是检查规则的精简版，完整规范见项目根目录下的指南文件。

## Skill 必需 frontmatter 字段

```yaml
---
name: <skill-name>           # 必填，全局唯一，全小写 + 连字符
description: <一句话描述>      # 必填，非空
type: <type>                  # 必填，值来自 skill-taxonomy.yaml
domain: <domain>              # 必填，值来自 skill-taxonomy.yaml
style-set: <style-set>       # 条件必填：type=style 时
tags: [tag1, tag2]            # 可选，建议填写
---
```

## Agent 必需 frontmatter 字段

```yaml
---
name: <agent-name>            # 必填
description: <一句话描述>      # 必填
tools: Read, Glob, ...        # 必填，可用工具列表
skills: skill-a, skill-b      # 可选，逗号分隔，每个须对应 arkts-skills/skills/ 下的有效目录
model: opus                   # 可选
---
```

## Skill 命名规范

| 类型 | 前缀 | 示例 |
|------|------|------|
| Domain Skill | `arkts-` | arkts-data-layer |
| Pipeline Skill | `a2h-` | a2h-spec |
| 分析工具 | `android-` | android-screenshot-analyzer |
| 风格 Skill | `arkts-` | arkts-ui-component |

## 目录结构要求

```
arkts-skills/skills/<skill-name>/
├── SKILL.md            # 必须存在
└── references/         # 如 SKILL.md 中引用了 references/ 则必须存在
    └── *.md            # SKILL.md 中引用的每个文件都必须存在
```

## CI 五项校验

| 脚本 | 检查内容 |
|------|----------|
| lint:skills | SKILL.md 格式、frontmatter 完整性 |
| check:refs | references/ 引用完整性 |
| check:agents | Agent 的 skills 字段引用有效性 |
| check:counts | README.md 数量声明与实际一致 |
| check:plugin | plugin.json 格式和版本一致性 |

## README 计数位置

文件: `arkts-skills/skills/README.md`

需要更新的声明模式：
- `N 个 Pipeline Skills`
- `N 个 Domain Skills`
- `N 个 Agent`
