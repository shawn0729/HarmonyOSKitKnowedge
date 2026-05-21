---
name: arkts-animation-builder
description: 生成 ArkTS/HarmonyOS 动画和交互效果代码。当用户需要实现 animateTo 显式动画、属性动画 animation()、transition 转场动画、geometryTransition 共享元素转场、Spring/弹簧动画、手势跟随动画、循环动画、淡入淡出、缩放、位移、旋转效果、粒子动画、路径动画、或任何 UI 动效和交互反馈时，务必触发此 skill。即使用户只说"加个动画"或"让它动起来"，也应触发。
---

# ArkTS Animation Builder — 动画效果生成器

## HarmonyOS Kit 知识使用规则

本 skill 的工程实践、迁移步骤和 ownership 以当前 skill 原内容为准。涉及具体 HarmonyOS Kit API、错误码、导入路径、权限、版本兼容、FAQ、最佳实践时，必须读取 `references/harmonyos-sdk/` 下对应 Kit 资料。

先按本 skill 实践确定动画类型、状态驱动关系和交互边界，再按任务场景读取对应 Kit 的 `routing.md` / `guides.md`。API、导入、权限、错误码、版本兼容以 Kit references 和 sources 为准。排障、适配或行为异常必须读取对应 Kit 的 `best-practices-and-faq.md`。当本 skill 原规则与 Kit 资料冲突时，保留工程分层和 ownership，用 Kit 知识修正具体 API 调用。不确定时调用 `arkts-knowledge-verifier`。

### 本 skill 已融合的 Kit

Kit 任务场景覆盖见 `references/harmonyos-sdk/kit-task-scenarios.md`。

- ArkUI：用于页面动效迁移、状态过渡、转场衔接和动画体验对齐；入口路径 `references/harmonyos-sdk/arkui/routing.md`。

## API 版本

本 skill 的代码模板基于 **API 12+**（HarmonyOS 5.0.0+）。动画相关的版本变化：

- **keyframeAnimateTo()**（API 12+ 新增）：支持多关键帧动画序列
- **geometryTransition 的 `follow` 参数**（API 12+ 新增）：控制共享元素过渡路径
- 使用 `@kit.*` 导入：`import { curves } from '@kit.ArkUI'`（不要用 `@ohos.curves`）

生成代码前，先确认用户的目标 API 版本。检查方法：读取 `build-profile.json5` 的 `compatibleSdkVersion` 字段。遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 arkts-knowledge-verifier skill。

---

## 动画类型选择

```
你需要什么动画？
│
├─ 状态驱动的属性变化（点击后变大/变色/移动）
│   └─ animateTo()（显式动画）— 最常用
│       控制哪些属性变化带动画
│
├─ 组件始终带动画（任何属性变化自动动画）
│   └─ .animation()（属性动画）
│       写在属性链末尾，之前的属性变化自动动画
│
├─ 组件出现/消失时的过渡
│   └─ .transition()（转场动画）
│       配合 if 条件渲染使用
│
├─ 两个页面/组件间的元素衔接
│   └─ geometryTransition（共享元素转场）
│       同一 id 的元素在不同位置间平滑过渡
│
├─ 手指拖动/滑动跟随
│   └─ 手势 + animateTo / translate
│       PanGesture + 实时更新 offset
│
├─ 长按触发辅助操作（点击/长按分工）
│   └─ LongPressGesture 单独使用
│       适用：点击做 A，长按做 B（如查看 vs 新增）
│
├─ 列表拖拽排序
│   ├─ 4-A PanGesture 方案 — 自由度高，可自定义旋转/倾斜动画
│   └─ 4-B DragEvent 框架 — 系统级支持，配合 LazyForEach 性能优
│
└─ 循环/永久动画（loading 旋转、呼吸灯）
    └─ animateTo + iterations: -1
        或组合多个 animateTo
```

---

## 1. animateTo（显式动画）— 最常用

当某个用户操作（点击、滑动）触发状态变化时，用 animateTo 包裹状态赋值，让 UI 变化带动画：

```typescript
@Component
struct AnimateExample {
  @State scale: number = 1
  @State opacity: number = 1

  build() {
    Column() {
      Image($r('app.media.photo'))
        .scale({ x: this.scale, y: this.scale })
        .opacity(this.opacity)
        .onClick(() => {
          animateTo({
            duration: 300,                    // 持续时间 ms
            curve: Curve.EaseInOut,           // 动画曲线
            delay: 0,                         // 延迟 ms
            iterations: 1,                    // 播放次数（-1 无限）
            playMode: PlayMode.Normal,        // Normal/Reverse/Alternate
            onFinish: () => {                 // 完成回调
              console.info('Animation done')
            }
          }, () => {
            // 在这个闭包里修改状态
            this.scale = this.scale === 1 ? 1.5 : 1
            this.opacity = this.opacity === 1 ? 0.5 : 1
          })
        })
    }
  }
}
```

### 关键理解

animateTo 的第二个参数（闭包）里修改的 @State 变量，其关联的 UI 属性变化会自动动画化。**不在闭包里的状态变化不会有动画**。

### 曲线选择指南

```typescript
// 预设曲线（满足 80% 场景）
Curve.Linear          // 匀速，适合进度条
Curve.EaseInOut       // 两头慢中间快，最通用的选择
Curve.EaseIn          // 开始慢后面快，适合退场
Curve.EaseOut         // 开始快后面慢，适合入场
Curve.FastOutSlowIn   // Material Design 标准曲线

// 弹簧曲线（有弹性效果，适合按钮/卡片）
curves.springMotion()                           // 默认弹簧
curves.springMotion(0.6, 0.9)                   // 自定义（响应、阻尼）
curves.interpolatingSpring(0, 1, 328, 34)       // 物理弹簧（质量、刚度、阻尼）

// 自定义贝塞尔
curves.cubicBezierCurve(0.33, 0, 0.67, 1)
```

**选择建议**：
- 不确定用什么 → `Curve.EaseInOut`
- 想要弹性活力感 → `curves.springMotion()`
- 列表项进入 → `Curve.FastOutSlowIn`

---

## 2. .animation()（属性动画）

写在属性链中，**之前**的属性变化会自动动画：

```typescript
@Component
struct PropertyAnimation {
  @State widthSize: number = 200
  @State heightSize: number = 100

  build() {
    Column() {
      Button('Animate')
        .width(this.widthSize)
        .height(this.heightSize)
        .animation({               // 之前的 width/height 变化会自动动画
          duration: 300,
          curve: Curve.EaseInOut,
        })
        .backgroundColor(Color.Blue)  // 这个属性在 animation() 之后，不受影响
        .onClick(() => {
          this.widthSize = this.widthSize === 200 ? 300 : 200
          this.heightSize = this.heightSize === 100 ? 150 : 100
        })
    }
  }
}
```

**animateTo vs .animation() 怎么选**：
- `animateTo`：精确控制哪次操作带动画（推荐，更灵活）
- `.animation()`：组件的属性变化始终带动画（简单场景）

---

## 3. transition（转场动画）

组件在 if 条件渲染中出现/消失时播放的动画：

```typescript
@Component
struct TransitionExample {
  @State isShow: boolean = false

  build() {
    Column() {
      Button(this.isShow ? '隐藏' : '显示')
        .onClick(() => {
          animateTo({ duration: 300 }, () => {
            this.isShow = !this.isShow
          })
        })

      if (this.isShow) {
        Text('Hello Animation')
          .fontSize(24)
          .transition(TransitionEffect.OPACITY           // 淡入淡出
            .combine(TransitionEffect.scale({ x: 0.8, y: 0.8 }))  // + 缩放
          )
      }
    }
  }
}
```

### TransitionEffect 组合

```typescript
// 基础效果
TransitionEffect.OPACITY              // 透明度 0→1
TransitionEffect.SLIDE                // 从边缘滑入
TransitionEffect.IDENTITY             // 无效果（用于组合的起点）

// 方向滑动
TransitionEffect.move(TransitionEdge.TOP)      // 从顶部滑入
TransitionEffect.move(TransitionEdge.BOTTOM)   // 从底部滑入
TransitionEffect.move(TransitionEdge.START)     // 从左侧滑入
TransitionEffect.move(TransitionEdge.END)       // 从右侧滑入

// 缩放
TransitionEffect.scale({ x: 0, y: 0 })        // 从点放大
TransitionEffect.scale({ x: 0.8, y: 0.8 })    // 从 80% 放大

// 旋转
TransitionEffect.rotate({ angle: 90 })

// 组合多个效果
TransitionEffect.OPACITY
  .combine(TransitionEffect.scale({ x: 0.8, y: 0.8 }))
  .combine(TransitionEffect.move(TransitionEdge.BOTTOM))
  .animation({ duration: 300, curve: Curve.EaseOut })

// 入场/出场不同效果
TransitionEffect.asymmetric(
  TransitionEffect.move(TransitionEdge.END),     // 入场：从右滑入
  TransitionEffect.move(TransitionEdge.START)     // 出场：从左滑出
)
```

**重要**：transition 必须配合 animateTo 触发条件变化才会播放。直接修改 if 条件不会有动画。

---

## 4. geometryTransition（共享元素转场）

让同一个 id 的组件在不同位置间平滑过渡：

```typescript
@Component
struct SharedElementExample {
  @State isExpanded: boolean = false

  build() {
    Stack() {
      if (!this.isExpanded) {
        // 缩略图
        Image($r('app.media.photo'))
          .width(100)
          .height(100)
          .borderRadius(8)
          .geometryTransition('photo_1')  // 相同 id
          .onClick(() => {
            animateTo({ duration: 500, curve: Curve.EaseInOut }, () => {
              this.isExpanded = true
            })
          })
      } else {
        // 大图
        Image($r('app.media.photo'))
          .width('100%')
          .height(300)
          .geometryTransition('photo_1')  // 相同 id
          .onClick(() => {
            animateTo({ duration: 500, curve: Curve.EaseInOut }, () => {
              this.isExpanded = false
            })
          })
      }
    }
  }
}
```

---

## 5. 手势跟随动画

手指拖动时元素跟随移动：

```typescript
@Component
struct DragAnimation {
  @State offsetX: number = 0
  @State offsetY: number = 0

  build() {
    Column() {
      Image($r('app.media.card'))
        .width(200)
        .height(300)
        .translate({ x: this.offsetX, y: this.offsetY })
        .gesture(
          PanGesture({ direction: PanDirection.All })
            .onActionStart(() => {
              // 手势开始
            })
            .onActionUpdate((event: GestureEvent) => {
              // 实时跟随（不用 animateTo，要即时响应）
              this.offsetX += event.offsetX
              this.offsetY += event.offsetY
            })
            .onActionEnd(() => {
              // 手势结束，弹回原位（用 animateTo 添加弹簧效果）
              animateTo({
                duration: 600,
                curve: curves.springMotion(0.6, 0.9)
              }, () => {
                this.offsetX = 0
                this.offsetY = 0
              })
            })
        )
    }
  }
}
```

**关键**：onActionUpdate 中**不用 animateTo**（要即时跟随），onActionEnd 中用 animateTo + 弹簧曲线（要平滑回弹）。

---

## 6. 循环动画

### Loading 旋转

```typescript
@Component
struct LoadingSpinner {
  @State angle: number = 0

  aboutToAppear(): void {
    // 启动无限旋转
    animateTo({
      duration: 1000,
      curve: Curve.Linear,
      iterations: -1,        // 无限循环
      playMode: PlayMode.Normal
    }, () => {
      this.angle = 360
    })
  }

  build() {
    Image($r('app.media.loading'))
      .width(40)
      .height(40)
      .rotate({ angle: this.angle })
  }
}
```

### 呼吸灯效果

```typescript
@Component
struct BreathingLight {
  @State scale: number = 1

  aboutToAppear(): void {
    animateTo({
      duration: 1500,
      curve: Curve.EaseInOut,
      iterations: -1,
      playMode: PlayMode.Alternate  // 来回播放
    }, () => {
      this.scale = 1.2
    })
  }

  build() {
    Circle()
      .width(100)
      .height(100)
      .fill(Color.Blue)
      .opacity(0.6)
      .scale({ x: this.scale, y: this.scale })
  }
}
```

---

## 停止动画技巧

```typescript
// 用 duration: 0 的 animateTo 立即停止
stopAnimation(): void {
  animateTo({ duration: 0 }, () => {
    this.scale = 1       // 立即回到初始值
    this.opacity = 1
  })
}
```

---

## 性能注意事项

1. **避免在动画中频繁创建/销毁组件**：transition 动画比重建组件开销小
2. **优先使用 translate/scale/rotate/opacity**：这些属性不触发重新布局，GPU 直接处理
3. **避免动画中修改 width/height**：会触发重新布局，性能差
4. **LazyForEach 中谨慎使用复杂动画**：可能导致帧率下降

```typescript
// 不推荐 — 触发布局重计算
animateTo({ ... }, () => {
  this.cardWidth = 300   // width 变化触发布局
  this.cardHeight = 200  // height 变化触发布局
})

// 推荐 — 使用 scale 代替
animateTo({ ... }, () => {
  this.cardScale = 1.5   // scale 不触发布局，性能好
})
```

---

## 常见错误 vs 正确写法

### 错误 1：transition 没配合 animateTo

```typescript
// 错误 — 没有动画效果
Button('Toggle').onClick(() => {
  this.isShow = !this.isShow  // 直接修改，transition 不生效
})

// 正确 — 用 animateTo 触发
Button('Toggle').onClick(() => {
  animateTo({ duration: 300 }, () => {
    this.isShow = !this.isShow
  })
})
```

### 错误 2：循环动画的 @State 初始值等于目标值

```typescript
// 错误 — 初始值就是 360，没有变化所以没有动画
@State angle: number = 360
aboutToAppear() {
  animateTo({ iterations: -1 }, () => {
    this.angle = 360  // 值没变！
  })
}

// 正确 — 初始值和目标值不同
@State angle: number = 0
aboutToAppear() {
  animateTo({ iterations: -1 }, () => {
    this.angle = 360
  })
}
```

### 错误 3：手势跟随用了 animateTo

```typescript
// 错误 — 拖动有延迟感
.onActionUpdate((event) => {
  animateTo({ duration: 100 }, () => {
    this.offsetX += event.offsetX  // 有延迟，不跟手
  })
})

// 正确 — 直接赋值
.onActionUpdate((event) => {
  this.offsetX += event.offsetX  // 即时响应
  this.offsetY += event.offsetY
})
```

---

## 生成检查清单

- [ ] 选择了合适的动画类型
- [ ] animateTo 的状态修改在闭包内
- [ ] transition 配合 animateTo 触发
- [ ] 循环动画的初始值 ≠ 目标值
- [ ] 手势跟随不用 animateTo
- [ ] 优先使用 translate/scale/rotate/opacity
- [ ] geometryTransition 的 id 在两个位置一致
- [ ] DragEvent 方案使用 `.draggable()` 启用，`onDragStart` 返回预览 builder

---

## 跨 Skill 协作

动画通常需要配合 UI 组件使用。如果用户需求涉及组件布局，读取 `arkts-component-builder/SKILL.md`。如果是完整业务功能（如带动画的列表详情页），读取 `arkts-pattern-library/SKILL.md`（它有编排协议引导完整流程）。完整路由矩阵见 `arkts-knowledge-verifier/references/skill-routing-guide.md`。

---

## References

- `references/explicit-animation.md` — animateTo 各种场景的完整示例
- `references/transition-patterns.md` — 页面/组件转场动画完整模板
- `references/gesture-animation.md` — 手势跟随动画完整实现（卡片滑动、下拉刷新、5-B 长按分工独立 Gesture、列表拖拽含 4-A PanGesture 方案与 4-B DragEvent 框架对比）
- `references/media-app-animations.md` — 媒体应用动画：下载进度环、播放按钮切换、MiniPlayer 显隐、半圆图表
- 遇到版本兼容性或其他不确定的 ArkTS 知识点（如属性、语法、权限等），参阅 **arkts-knowledge-verifier** skill
