---
name: arkui-tabs-problem-solving
description: Use when 实现、修改或排查 HarmonyOS ArkUI Tabs、TabContent、TabsController、自定义页签、页签对齐、横向滚动、隐藏默认页签栏、页签切换、选中态同步或 Tabs 显示与交互问题。
---

# ArkUI Tabs 问题解决

## 概述

使用本 Skill 处理 ArkUI Tabs 的实现、修改和排查任务。目标是把 FAQ 示例转化为诊断和修复流程，而不是复述原始 FAQ。

## 何时使用

当用户问题涉及以下内容时使用：

- `Tabs`、`TabContent` 或 `TabsController`
- 自定义页签、自定义 tab bar、隐藏默认页签栏
- 页签左对齐、居中、横向滚动、样式同步
- 点击自定义页签后内容不切换
- 滑动 Tabs 内容后外部页签选中态不同步
- 现有 Tabs 代码的排查、修改或重构

如果只是普通静态布局里出现了 “tab” 这个词，但没有使用 ArkUI `Tabs`，不要执行完整流程。

## 必要诊断

写代码或改代码前，先判断任务类型：

1. **默认 Tabs**：内置页签栏已满足需求。
2. **自定义 tab bar**：用户需要自定义布局、图标、对齐、滚动或视觉样式。
3. **同步问题**：页签样式变化但内容不切换，或内容切换但样式不同步。
4. **迁移任务**：把 FAQ 示例改写成项目可用的 ArkTS 代码。

## 生成规则

自定义 tab bar 场景必须满足：

- 创建一个 `TabsController`，并传入 `Tabs({ controller })`。
- 维护一个唯一的选中下标状态，通常是 `@State focusIndex` 或 `@State selectedIndex`。
- 自定义页签点击时，调用 `controller.changeIndex(index)` 并更新选中下标。
- 外部自定义 tab bar 替代默认页签栏时，使用 `.barHeight(0)` 隐藏默认栏。
- 使用 `onContentWillChange` 在滑动或 controller 切换内容时同步选中下标。
- 尽量从同一个数据源生成自定义页签和 `TabContent`。
- 页签数量可能超过宽度时，使用 `Scroll` + `Row`。

## 排查清单

当 Tabs 行为异常时，按顺序检查：

1. 自定义页签点击逻辑和 `Tabs` 是否共享同一个 `TabsController` 实例？
2. 自定义页签点击时是否调用 `controller.changeIndex(index)`？
3. 自定义页签点击时是否更新选中下标状态？
4. `Tabs` 是否通过 `Tabs({ controller: this.controller })` 绑定同一个 controller？
5. `onContentWillChange` 是否更新选中下标并返回 `true`？
6. 如果使用自定义 tab bar，是否通过 `.barHeight(0)` 隐藏默认页签栏？
7. 自定义页签数据和 `TabContent` 的数量、顺序是否一致？
8. 代码是否只改变了视觉选中态，却忘记切换 Tabs 内容？

## 示例路由

只读取当前问题需要的示例：

- 自定义 tab bar、隐藏默认栏或完整实现：
  读取 `examples/custom-tabs-template.md`。
- 点击后内容不切换、选中样式不同步或已有代码异常：
  读取 `examples/tabs-switch-diagnosis.md`。
- 左对齐、横向滚动或自定义 tab 布局：
  读取 `examples/tabs-alignment-pattern.md`。

## 代码迁移规则

改写 FAQ 代码时：

- 去掉文档行号。
- 替换示例组件名，例如 `CustomizeTheTabsBarAndItsAlignment`。
- 替换示例资源，例如 `$r('app.media.startIcon')`。
- 把 `tabArray = [0, 1]` 替换成用户真实 tab 数据模型。
- 保留核心连接关系：选中下标、`TabsController`、自定义 tab builder、`changeIndex`、`Tabs`、`TabContent`、`.barHeight(0)` 和 `onContentWillChange`。

## 质量门禁

生成代码完成前，确认：

- 选中下标只有一个可信来源。
- `TabsController` 不会在渲染过程中反复创建。
- 自定义页签点击会同时切换内容和视觉选中态。
- `onContentWillChange` 能同步滑动或 controller 引起的内容切换。
- `TabContent` 顺序和自定义页签顺序一致。
- 示例代码已替换为项目中的命名、资源、数据模型和样式需求。
