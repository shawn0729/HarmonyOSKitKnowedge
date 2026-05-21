# 如何使用Swiper组件实现下拉刷新

---

Swiper组件用于创建滑块视图容器，可以使用Refresh组件实现下拉刷新效果。



```typescript
1. @Entry
2. @Component
3. struct SwiperItemLeak {
4.  @State isStopSwiperSlide: boolean = false;
5.  @State positionY: number = 0;
6.  private swiperController: SwiperController = new SwiperController();
7.  @State curSwiperIndex: number = 0;
8.  private list: number[] = [];
9.
10.  aboutToAppear(): void {
11.  for (let i = 1; i <= 10; i++) {
12.  this.list.push(i);
13.  }
14.  }
15.
16.  build() {
17.  Refresh({ refreshing: $$this.isStopSwiperSlide}) {
18.  Swiper(this.swiperController) {
19.  ForEach(this.list, (item: number) => {
20.  Text(item.toString())
21.  .width('100%')
22.  .height('100%')
23.  .backgroundColor(0xAFEEEE * ((item + 1) / 0x0f))
24.  .textAlign(TextAlign.Center)
25.  .fontSize(30)
26.  },(item: number) => JSON.stringify(item))
27.  }
28.  .vertical(true)
29.  .width('100%')
30.  .height('100%')
31.  .cachedCount(3)
32.  .index(0)
33.  .autoPlay(false)
34.  .indicator(false)
35.  .effectMode(EdgeEffect.None)
36.  .loop(false)
37.  .duration(100)
38.  .disableSwipe(this.isStopSwiperSlide)
39.  .displayCount(1)
40.  .itemSpace(0)
41.  .curve(Curve.Linear)
42.  .backgroundColor(Color.Red)
43.  .position({ y: this.positionY })
44.  .onChange((index: number) => {
45.  this.curSwiperIndex = index;
46.  })
47.  }
48.  .onRefreshing(() => {
49.  setTimeout(() => {
50.  this.isStopSwiperSlide = false
51.  }, 2000)
52.  })
53.  .backgroundColor(0x89CFF0)
54.  .refreshOffset(64)
55.  .pullToRefresh(true)
56.  .width('100%')
57.  .height('100%')
58.  }
59. }

```


[UseSwiperDropdownToRefresh.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/UseSwiperDropdownToRefresh.ets#L21-L79)



**参考链接**



[Refresh](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-refresh)
