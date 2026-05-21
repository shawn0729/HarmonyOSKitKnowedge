# 标准化功能定位工作流程

## 概述

本文档描述 arkts-codebase-locator 技能在响应功能定位请求时的标准化工作流程。

## 主流程

### 阶段一：问题分析

1. 识别问题类型（参见 question-types.md）
2. 提取关键词和语义意图
3. 确定目标：组件、服务、数据层还是配置

### 阶段二：Repomap 初步探索

1. 读取 repomap.md 获取项目整体结构
2. 通过模块列表缩小候选范围
3. 识别相关 HAP/HSP 模块

### 阶段三：目录级导航

1. 按项目结构规范（参见 project-structure.md）定位目录
2. 优先检查约定路径：
   - 页面：`src/main/ets/pages/`
   - 组件：`src/main/ets/components/`
   - 服务：`src/main/ets/services/`
   - 模型：`src/main/ets/model/`

### 阶段四：文件级精确定位

1. 根据文件命名规范匹配目标文件
2. 必要时读取文件确认内容
3. 返回精确路径和关键代码位置

## 决策树

```
用户问题
  ├─ 是否涉及 UI/页面？ → pages/ 或 components/
  ├─ 是否涉及数据/状态？ → model/ 或 viewmodel/
  ├─ 是否涉及网络/IO？ → services/ 或 data/
  ├─ 是否涉及配置？ → 项目根或 resources/
  └─ 是否涉及导航？ → router 配置或 NavDestination
```

## 输出规范

定位结果需包含：
- 文件相对路径（相对于项目根）
- 关键类名或函数名
- 简短说明（1-2 句）
