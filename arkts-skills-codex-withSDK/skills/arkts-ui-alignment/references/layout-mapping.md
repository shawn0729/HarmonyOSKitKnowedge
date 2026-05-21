# Android→ArkTS 布局映射参考

> 组件映射详细版 + 代码示例 + 布局对照 + 单位转换。

---

## 布局容器映射

### LinearLayout → Column / Row

```xml
<!-- Android 垂直布局 -->
<LinearLayout android:orientation="vertical">
  <TextView ... />
  <Button ... />
</LinearLayout>
```

```typescript
// ArkTS 等价
Column() {
  Text('标题')
  Button('操作')
}
```

```xml
<!-- Android 水平布局 -->
<LinearLayout android:orientation="horizontal">
  <ImageView ... />
  <TextView ... />
</LinearLayout>
```

```typescript
// ArkTS 等价
Row() {
  Image($r('app.media.icon'))
  Text('标题')
}
```

### FrameLayout → Stack

```xml
<!-- Android 帧布局（层叠） -->
<FrameLayout>
  <ImageView ... />
  <TextView android:gravity="bottom|center" ... />
</FrameLayout>
```

```typescript
// ArkTS 等价
Stack({ alignContent: Alignment.Bottom }) {
  Image($r('app.media.cover'))
  Text('叠加文字')
}
```

### ConstraintLayout → Column / Row 组合

ArkTS 没有 ConstraintLayout 直接等价物。使用 Column + Row 嵌套组合：

```typescript
// 复杂布局用 Column + Row 嵌套
Column() {
  Row() {
    Image(coverUrl).width(60).height(60)
    Column() {
      Text(title).fontSize(16)
      Text(subtitle).fontSize(12).fontColor('#99000000')
    }.layoutWeight(1)
    Button('操作')
  }
}
```

### RelativeLayout → Row / Column + layoutWeight

```typescript
// 左-中-右 布局
Row() {
  Image(icon).width(40)            // 左侧固定宽度
  Column() {                       // 中间填充剩余空间
    Text(title)
  }.layoutWeight(1)
  Text(time)                       // 右侧固定
}
```

---

## 列表组件映射

### RecyclerView → List + LazyForEach

```java
// Android
RecyclerView recyclerView = findViewById(R.id.list);
recyclerView.setAdapter(new MyAdapter(items));
```

```typescript
// ArkTS — 使用 LazyForEach 虚拟化
List() {
  LazyForEach(this.dataSource, (item: ItemModel) => {
    ListItem() {
      ItemComponent({ item: item })
    }
  }, (item: ItemModel) => item.id.toString())
}
```

### GridView → Grid

```typescript
Grid() {
  ForEach(this.items, (item: ItemModel) => {
    GridItem() {
      ItemComponent({ item: item })
    }
  })
}
.columnsTemplate('1fr 1fr 1fr')  // 3 列等分
.rowsGap(8)
.columnsGap(8)
```

---

## 交互组件映射

### BottomNavigationView → 自定义 Row

```typescript
// 不要用 Tabs 在 Navigation 内部！
Row() {
  this.tabBarItem(0, $r('app.string.home'), $r('sys.symbol.house'))
  this.tabBarItem(1, $r('app.string.queue'), $r('sys.symbol.list_bullet'))
  this.tabBarItem(2, $r('app.string.inbox'), $r('sys.symbol.envelope'))
}
.width('100%')
.height(56)
.backgroundColor(Color.White)
.border({ width: { top: 0.5 }, color: '#E0E0E0' })
```

### DrawerLayout → SideBarContainer

```typescript
SideBarContainer(SideBarContainerType.Embed) {
  // 侧边栏内容
  Column() { ... }
  // 主内容
  Column() { ... }
}
.showSideBar(this.showSidebar)
.sideBarWidth(280)
```

### ViewPager2 → Swiper

```typescript
Swiper() {
  ForEach(this.pages, (page: PageModel) => {
    PageComponent({ data: page })
  })
}
.index(this.currentPage)
.indicator(true)
```

### CardView → Column + 圆角 + 阴影

```typescript
Column() {
  // 卡片内容
}
.borderRadius(12)
.backgroundColor(Color.White)
.shadow({ radius: 4, color: '#1A000000', offsetY: 2 })
.padding(16)
```

### AlertDialog

```typescript
AlertDialog.show({
  title: '确认删除',
  message: '删除后不可恢复',
  primaryButton: {
    value: '取消',
    action: () => {}
  },
  secondaryButton: {
    value: '删除',
    fontColor: '#E84026',
    action: () => { this.doDelete(); }
  }
});
```

### Snackbar → promptAction.showToast

```typescript
import { promptAction } from '@kit.ArkUI';

promptAction.showToast({
  message: '操作成功',
  duration: 2000
});
```

---

## 进度指示器映射

### ProgressBar (Linear)

```typescript
Progress({ value: this.percent, total: 100, type: ProgressType.Linear })
  .height(2)
  .width('100%')
  .color('#007DFF')
  .backgroundColor('#E0E0E0')
```

### ProgressBar (Circular / Ring)

```typescript
Progress({ value: this.percent, total: 100, type: ProgressType.Ring })
  .width(32)
  .height(32)
  .color('#007DFF')
  .style({ strokeWidth: 3 })
```

---

## 单位转换

| Android | ArkTS | 说明 |
|---------|-------|------|
| dp | vp | 1:1 对应，density-independent pixels |
| sp | fp | 字体大小，但 ArkTS 中通常直接用 vp |
| px | px | 物理像素（不推荐） |

ArkTS 中数值默认单位为 vp，直接使用数字即可：

```typescript
// ArkTS：数字就是 vp
Text('标题')
  .fontSize(16)   // 16vp，等同于 Android 16sp
  .margin({ top: 8 })  // 8vp，等同于 Android 8dp
```
