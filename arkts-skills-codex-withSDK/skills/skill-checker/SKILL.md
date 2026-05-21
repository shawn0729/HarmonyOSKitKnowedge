---
name: skill-checker
description: >
  检查新增或修改的 Skills、Agents、Commands、Rules 等能力是否符合项目开发规范和 Skill Hub 管理规范。
  当用户说"检查新增的 skill"、"我刚加了个新 skill"、"帮我检查下规范"、"检查 agent 是否合规"、
  "新增的内容是否符合规范"等，或者在对话中刚完成了 SKILL.md / Agent / Command / Rule 的创建或修改时，
  务必触发此 skill。即使用户只是说"看看有没有问题"或"跑一下检查"，也应触发。
---

# Skill Checker — 能力合规检查器

当开发者新增或修改了项目中的 Skills、Agents、Commands、Rules 等能力时，执行此 Skill 进行全面合规检查，并引导用户完成修复。

## 检查依据

以下三个文件是检查规则的权威来源：

1. `docs/guides/development-and-release-guide.md` — Skill/Agent 开发规范、CI 五项校验规则
2. `docs/guides/skill-hub-guide.md` — 分类体系、frontmatter 标签规则、manifest 规范
3. `skill-taxonomy.yaml` — type/domain/style-set/platform 的合法枚举值

**开始检查前，先读取这三个文件获取最新规范。** 规范可能随项目演进而更新，不要依赖记忆中的旧版本。

## 工作流程

### Step 1: 识别变更范围

确定哪些文件是新增或修改的。按优先级尝试以下方式：

1. **git diff 检测** — 运行 `git diff --name-only HEAD` 和 `git diff --name-only --cached` 查看未提交的变更文件
2. **用户指定** — 用户明确说了"我刚加了 xxx"
3. **主动询问** — 如果无法判断，问用户："你新增或修改了哪些文件？"

从变更文件中筛选出需要检查的目标：

| 文件模式 | 能力类型 |
|----------|----------|
| `arkts-*/skills/*/SKILL.md` | Skill |
| `arkts-agents/agents/*.md` | Agent |
| `commands/*.md` | Command |
| `rules/*.md` | Rule |

### Step 2: 逐项检查

对每个目标文件，按能力类型执行对应的检查清单。

#### Skill 检查清单

| # | 检查项 | 严重度 | 规则 |
|---|--------|--------|------|
| 1 | SKILL.md 存在 | ERROR | 目录下必须有 SKILL.md |
| 2 | frontmatter 格式 | ERROR | 首行为 `---`，有完整的 YAML frontmatter |
| 3 | name 字段 | ERROR | 非空，全局唯一 |
| 4 | description 字段 | ERROR | 非空 |
| 5 | type 字段 | ERROR | 非空，值在 `skill-taxonomy.yaml` 的 types 中 |
| 6 | domain 字段 | ERROR | 非空，值在 `skill-taxonomy.yaml` 的 domains 中 |
| 7 | style-set 字段 | ERROR | 当 type=style 时必填，值须在 taxonomy 中 |
| 8 | tags 字段 | WARN | 建议添加 tags 提升可搜索性 |
| 9 | references/ 完整性 | ERROR | SKILL.md 中引用的 `references/` 文件必须实际存在 |
| 10 | name 一致性 | ERROR | 如果同名 Skill 存在于其他平台集合中，name 必须完全一致 |

#### Agent 检查清单

| # | 检查项 | 严重度 | 规则 |
|---|--------|--------|------|
| 1 | frontmatter 存在 | ERROR | 首行为 `---`，有完整 YAML frontmatter |
| 2 | name 字段 | ERROR | 非空 |
| 3 | description 字段 | ERROR | 非空 |
| 4 | skills 引用有效 | ERROR | frontmatter 中 skills 列表里的每个 Skill 目录必须存在于 `arkts-skills/skills/` 下 |

#### Command / Rule 检查清单

| # | 检查项 | 严重度 | 规则 |
|---|--------|--------|------|
| 1 | 文件格式 | WARN | 应有清晰的标题和结构 |
| 2 | 内容完整 | WARN | 不应有 TODO/TBD 占位符 |

### Step 3: 报告结果

将检查结果整理为一份清晰的报告，格式如下：

```
## 检查报告

检查范围: N 个文件（X Skill, Y Agent, Z 其他）

### ERROR (必须修复)
1. [arkts-skills/skill-xxx] type 字段缺失 — frontmatter 中未找到 type 字段
2. [arkts-skills/skill-xxx] domain 值非法 — "networking" 不在 skill-taxonomy.yaml 中，合法值为: data, system, ...

### WARN (建议修复)
1. [arkts-skills/skill-xxx] tags 缺失 — 建议添加 tags 提升可搜索性

### PASS
1. [arkts-skills/skill-yyy] 全部通过 ✓
```

如果没有任何问题，直接报告"全部通过"。

### Step 4: 引导修复

如果存在 ERROR 或 WARN，询问用户：

> "发现 N 个问题需要修复。你希望：
> 1. **自动修复** — 我直接修改文件，完成后你审核确认
> 2. **手动修改** — 我告诉你具体该改什么，你自己改"

**自动修复模式：**
- 逐个修复问题，每修复一项后展示 diff 让用户确认
- 对于需要用户判断的字段（如 type 和 domain 的选择），给出推荐值并说明理由，等用户确认后再写入
- 修复完成后重新跑一遍检查确认全部通过

**手动修改模式：**
- 对每个问题给出明确的修复指令（改哪个文件、哪一行、改成什么）
- 用户修改后可以再次触发检查

### Step 5: 计数更新检查

检查 `arkts-skills/skills/README.md` 中的数量声明是否与实际目录数匹配。如果不匹配：

- 报告差异（"README 声明 29 个 Domain Skills，实际 30 个"）
- 在自动修复模式下，更新 README 中的数量

### Step 6: CI 验证

所有修复完成后，建议用户运行 CI 校验确认：

```bash
npm run ci
```

或单独跑 Skill Hub 校验：

```bash
cd scripts/skill-hub && python hub.py --validate-only
```

## 常见修复示例

**缺少 type/domain 标签：**
```yaml
# 修复前
---
name: arkts-new-skill
description: 一句话描述
---

# 修复后
---
name: arkts-new-skill
description: 一句话描述
type: domain        # ← 根据 skill 内容推断
domain: ui          # ← 根据 skill 内容推断
---
```

**Agent 引用不存在的 Skill：**
```
ERROR: Agent a2h-worker 引用了 skill "arkts-nonexistent"，但该目录不存在。
修复: 确认 skill 名称是否拼写正确，或先创建该 Skill。
```

## 注意事项

- 推断 type/domain 时，读取 SKILL.md 的完整内容来判断，不要仅凭名称猜测
- 如果无法确定合适的 type 或 domain，列出候选项让用户选择
- 检查 name 唯一性时，需扫描所有 `arkts-*/skills/` 下的同名目录
- taxonomy 以 `skill-taxonomy.yaml` 文件为准，不要硬编码枚举值
