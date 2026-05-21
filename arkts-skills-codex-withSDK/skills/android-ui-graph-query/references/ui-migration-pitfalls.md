# UI Migration Pitfalls — 静默映射陷阱

编译通过但运行时异常的 Android → ArkUI 映射陷阱。
a2h-activity-converter 在 Phase 2 加载此文件，转换时必须逐条检查。

## CRITICAL — 必须处理，否则页面不可用

### P-01: SideBarContainer 子组件顺序反转
- **Android**: DrawerLayout 第一个子组件 = 主内容，第二个 = 侧边栏（通过 layout_gravity 标识）
- **ArkUI**: SideBarContainer 第一个子组件 = 侧边栏，第二个 = 主内容
- **错误表现**: 侧边栏和主内容位置互换，侧边栏占据全屏，主内容被挤到侧边
- **修复**: 转换时交换子组件顺序

### P-02: Tabs + Navigation 全屏遮盖
- **Android**: TabLayout + ViewPager 可嵌套在任意布局中
- **ArkUI**: Tabs 放在 Navigation 内部时，NavDestination 会覆盖整个 Navigation 区域（含 Tabs）
- **错误表现**: 切换到子页面后 Tab 栏消失
- **修复**: Tabs 放在 Navigation 外部，或使用自定义 Row 实现 Tab 栏

### P-03: CoordinatorLayout 滚动协调丢失
- **Android**: CoordinatorLayout + AppBarLayout + CollapsingToolbarLayout = 联动折叠
- **ArkUI**: 无直接等价物，Scroll + Column 不会自动联动
- **错误表现**: AppBar 不随滚动折叠，嵌套滚动可能冲突
- **修复**: 使用 Scroll 的 onScroll 回调手动计算 AppBar 高度和透明度

## HIGH — 功能缺失或数据不更新

### P-04: NavDestination 参数时序
- **Android**: Intent extras 在 onCreate/onResume 中可用
- **ArkUI**: NavDestination 的 pathInfo.param 仅在 onReady() 中可用，aboutToAppear() 中为 undefined
- **错误表现**: 页面参数始终为空，页面显示默认状态
- **修复**: 参数读取放在 onReady() 回调中，不放在 aboutToAppear()

### P-05: ForEach key 不完整导致 UI 不刷新
- **Android**: RecyclerView.Adapter notifyItemChanged(position) 精准更新
- **ArkUI**: ForEach 的 keyGenerator 只包含 id 时，属性变更（如 playState）不触发刷新
- **错误表现**: 数据变了但 UI 不更新
- **修复**: key 必须包含所有影响显示的字段：`item.id + '_' + item.playState`

### P-06: AppStorage 绑定时序
- **Android**: SharedPreferences 首次访问自动创建
- **ArkUI**: @StorageLink('key') 在组件实例化时绑定，如果 key 未预注册则绑定失败
- **错误表现**: 组件始终显示默认值，后续更新也无响应
- **修复**: 在 EntryAbility.onCreate 中预注册所有 AppStorage key

### P-07: ConstraintLayout 表达力缺口
- **Android**: ConstraintLayout 支持 chain、ratio、bias、barrier、guideline
- **ArkUI**: RelativeContainer 仅支持基本 alignRules
- **错误表现**: 复杂约束布局塌陷或错位
- **修复**: 复杂约束改用 Row/Column 嵌套 + Flex 布局模拟，或 onMeasureSize 自定义

### P-08: RecyclerView Adapter 模式丢失
- **Android**: Adapter 有粒度通知：notifyItemChanged/Inserted/Removed + DiffUtil
- **ArkUI**: 简单 ForEach(array) 丢失通知粒度，全量重渲染，动画消失
- **错误表现**: 列表无插入/删除动画，性能下降
- **修复**: 使用 LazyForEach + IDataSource 接口，实现 DataChangeListener

### P-09: NavigationView 语义丢失
- **Android**: NavigationView 集成抽屉头部、菜单项、选中状态管理
- **ArkUI**: 无等价物，需自定义 Column + List
- **错误表现**: 抽屉动画、选中高亮、头部滚动行为丢失
- **修复**: 自行实现选中状态管理和动画同步

## MEDIUM — 视觉偏差

### P-10: ViewPager → Swiper 生命周期差异
- **Android**: OnPageChangeCallback 在页面可见时触发
- **ArkUI**: Swiper onChange 触发时机与动画阶段关系不同
- **错误表现**: 页面初始化代码在错误时机执行
- **修复**: 关键初始化逻辑放在页面组件的 aboutToAppear 中，不依赖 onChange 回调

### P-11: BottomNavigationView 位置约束
- **Android**: BottomNavigationView 可放在任意位置
- **ArkUI**: Tabs + BarPosition.End 必须在 Column 中，不能被其他布局容器影响
- **错误表现**: Tab 栏位置错误或不可见
- **修复**: 确保 Tabs 组件是 Column 的直接子组件

### P-12: 默认 padding/margin 差异
- **Android**: Button 等组件有默认 padding（约 12dp），gravity 从父容器继承
- **ArkUI**: 组件默认 padding 为 0，对齐需显式设置
- **错误表现**: 按钮文字紧贴边框，文本左对齐而非居中
- **修复**: 显式设置 .padding() 和 .textAlign()

### P-13: RelativeLayout z-order 反转
- **Android**: RelativeLayout 子组件顺序不影响布局（由规则决定），但影响绘制顺序
- **ArkUI**: RelativeContainer 的子组件声明顺序决定 z-order
- **错误表现**: 需要在上层的组件被遮挡
- **修复**: 按 z-order 从底到顶排列子组件，或使用 .zIndex()

### P-14: Text 截断默认值
- **Android**: TextView 默认多行显示
- **ArkUI**: Text 默认单行 + 省略号
- **错误表现**: 多行文本只显示一行
- **修复**: 设置 .maxLines(N) 或去掉默认截断

### P-15: Image 缩放默认值
- **Android**: ImageView 默认 ScaleType.FIT_CENTER（适应边界，保持比例，居中）
- **ArkUI**: Image 默认 ObjectFit.Cover（填满裁切）
- **错误表现**: 图片裁切方式不同
- **修复**: 设置 .objectFit(ImageFit.Contain)

## 入口配置

### P-16: 入口页面未注册
- **问题**: 迁移后 main_pages.json 仍指向 pages/Index（Hello World）
- **错误表现**: 启动应用显示 Hello World 而非迁移后的主页
- **修复**: a2h-execute Stage 1 第一个 Batch 编译通过后，更新 main_pages.json 的 src 数组
