# 如何实现列表既可以左右滑、又可以上下滑动

---

实现列表的上下、左右滑动，参考代码如下：



1.代码页面布局部分



```typescript
1. import { CommonDataSource } from '../viewmodel/CommonDataSource';
2.
3.
4. @Observed
5. class ListItemData {
6.  text: string = '';
7.  id: string = '';
8. }
9.
10.
11. @Observed
12. class ListData {
13.  id: string = '';
14.  fundName: string = '';
15.  textDataSource: CommonDataSource<ListItemData> = new CommonDataSource<ListItemData>();
16. }
17.
18.
19. @Entry
20. @Component
21. struct ScrollListDemoPage {
22.  // Horizontal scrolling distance of list data
23.  @State remainOffset: number = 0;
24.  // Maintain a list controller array to store ListScrollers for all horizontal lists
25.  @State listScrollerArr: ListScroller[] = [];
26.  // The starting index of the list is used to refresh the list area displayed on the current screen
27.  @State startIndex: number = 0;
28.  // End index of list
29.  @State endIndex: number = 0;
30.  // List Data - Displayed Content
31.  @State listData: ListItemData[] = [];
32.  // Head title list, titles for each column
33.  private titleList: string[] = [];
34.  // List data source
35.  private dataSource = new CommonDataSource<ListData>();
36.  // Vertical scrolling of list data
37.  verticalScroller: Scroller = new Scroller();
38.  // Horizontal scrolling of list data
39.  horizontalScroller: Scroller = new Scroller();
40.  // Scroll the left name column
41.  leftScroller: Scroller = new Scroller();
42.  // Head title column scrolling
43.  topScroller: Scroller = new Scroller();
44.  // Head Title List Data Source
45.  headerList = new CommonDataSource<string>();
46.  // Actual processed data
47.  showList: ListData[] = [];
48.
49.
50.  aboutToAppear(): void {
51.  this.loadData();
52.  }
53.
54.
55.  loadData() {
56.  for (let i = 0; i < 30; i++) {
57.  this.titleList.push('title' + i);
58.  let itemData: ListItemData = {
59.  text: 'content' + i,
60.  id: i + ''
61.  };
62.  this.listData.push(itemData);
63.  }
64.  this.headerList.setData(this.titleList);
65.
66.
67.  for (let i = 0; i < 20; i++) {
68.  // Every time the next page of data is obtained, it is necessary to synchronously add a controller to the list
69.  this.listScrollerArr.push(new ListScroller());
70.  let listItemData: ListData = new ListData();
71.  listItemData.fundName = 'Equity fund' + i;
72.  listItemData.id = 'Equity fund' + i;
73.  listItemData.textDataSource = new CommonDataSource<ListItemData>();
74.  listItemData.textDataSource.setData(this.listData);
75.  this.showList.push(listItemData);
76.  }
77.  this.dataSource.setData(this.showList);
78.  }
79.
80.
81.  build() {
82.  Column() {
83.  // Headline Title
84.  this.titleBuilder()
85.  // Divider
86.  Divider()
87.  .strokeWidth('100%')
88.  .color(0xeeeeee)
89.
90.
91.  Row() {
92.  // Left column
93.  this.leftBuilder()
94.  // Right column
95.  this.rightScroll()
96.  }
97.  }
98.  .height('100%')
99.  .alignItems(HorizontalAlign.Start)
100.  }
101.
102.
103.  @Builder
104.  titleBuilder() {
105.  Row() {
106.  Column() {
107.  Text('name')
108.  }
109.  .width(140)
110.  .height(48)
111.  .backgroundColor(Color.White)
112.  .justifyContent(FlexAlign.Center)
113.  .alignItems(HorizontalAlign.Start)
114.  .padding({ left: 16 })
115.
116.
117.  // Top Title List
118.  List({ scroller: this.topScroller }) {
119.  LazyForEach(this.headerList, (item: string) => {
120.  ListItem() {
121.  Text(item)
122.  .height(48)
123.  .width(120)
124.  .textAlign(TextAlign.Start)
125.  .padding({ left: 16 })
126.  .backgroundColor(0xFFFFFF)
127.  }
128.  }, (item: string) => item)
129.  }
130.  .listDirection(Axis.Horizontal)
131.  .edgeEffect(EdgeEffect.None)
132.  .scrollBar(BarState.Off)
133.  .width('calc(100% - 140vp)')
134.  .layoutWeight(1)
135.  .onScrollFrameBegin((offset: number) => {
136.  for (let i = this.startIndex; i <= this.endIndex; i++) {
137.  this.listScrollerArr[i].scrollTo({
138.  xOffset: this.topScroller.currentOffset().xOffset + offset,
139.  yOffset: 0,
140.  animation: false
141.  });
142.  }
143.  return { offsetRemain: offset };
144.  })
145.  }
146.  .height(48)
147.  .width('100%')
148.  .justifyContent(FlexAlign.Start)
149.  }
150.
151.
152.  @Builder
153.  leftBuilder() {
154.  List({ scroller: this.leftScroller }) {
155.  LazyForEach(this.dataSource, (item: ListData) => {
156.  ListItem() {
157.  Column() {
158.  Text(item.fundName)
159.  .height('100%')
160.  .backgroundColor(0xFFFFFF)
161.  .layoutWeight(1)
162.  .margin({ left: 16 })
163.  Divider()
164.  .strokeWidth('100%')
165.  .color(0xeeeeee)
166.  }
167.  .justifyContent(FlexAlign.Center)
168.  .alignItems(HorizontalAlign.Start)
169.  }
170.  .height(60)
171.  }, (item: ListData) => JSON.stringify(item))
172.  }
173.  .listDirection(Axis.Vertical)
174.  .scrollBar(BarState.Off)
175.  .edgeEffect(EdgeEffect.None)
176.  .height('calc(100% - 48vp)')
177.  .width(140)
178.  .onScrollFrameBegin((offset: number) => {
179.  this.verticalScroller.scrollTo({
180.  xOffset: 0,
181.  yOffset: this.leftScroller.currentOffset().yOffset + offset,
182.  animation: false
183.  });
184.  return { offsetRemain: offset };
185.  })
186.  }
187.
188.
189.  @Builder
190.  rightScroll() {
191.  Scroll(this.horizontalScroller) {
192.  List({ initialIndex: 0, scroller: this.verticalScroller }) {
193.  LazyForEach(this.dataSource, (item: ListData, index: number) => {
194.  ListItem() {
195.  Column() {
196.  List({ scroller: this.listScrollerArr[index] }) {
197.  LazyForEach(item.textDataSource, (item: ListItemData) => {
198.  ListItem() {
199.  Text(item.text)
200.  .height('100%')
201.  .width('100%')
202.  .textAlign(TextAlign.Start)
203.  .padding({ left: 16 })
204.  .backgroundColor(0xFFFFFF)
205.  .fontColor('#ffe72929')
206.  .maxLines(1)
207.  .textOverflow({ overflow: TextOverflow.Ellipsis })
208.  }
209.  .width(120)
210.  }, (item: ListItemData, index: number) => JSON.stringify(item) + index + '')
211.  }
212.  .cachedCount(4)
213.  .height('100%')
214.  .width('100%')
215.  .layoutWeight(1)
216.  .listDirection(Axis.Horizontal)
217.  .scrollBar(BarState.Off)
218.  .nestedScroll({
219.  scrollForward: NestedScrollMode.PARENT_FIRST,
220.  scrollBackward: NestedScrollMode.PARENT_FIRST
221.  })
222.  .edgeEffect(EdgeEffect.None)
223.  .onDidScroll(() => {
224.  this.remainOffset = this.listScrollerArr[index]!.currentOffset().xOffset;
225.  })
226.  .onScrollFrameBegin((offset: number) => {
227.  this.topScroller.scrollTo({
228.  xOffset: this.listScrollerArr[index]!.currentOffset().xOffset + offset,
229.  yOffset: 0,
230.  animation: false
231.  });
232.  for (let i = this.startIndex; i <= this.endIndex; i++) {
233.  if (i !== index) {
234.  this.listScrollerArr[i].scrollTo({
235.  xOffset: this.listScrollerArr[index]!.currentOffset().xOffset + offset,
236.  yOffset: 0,
237.  animation: false
238.  });
239.  }
240.  }
241.  return { offsetRemain: offset };
242.  })
243.
244.
245.  Divider()
246.  .strokeWidth('100%')
247.  .color(0xeeeeee)
248.  }
249.  .height(60)
250.  }
251.  }, (item: ListData) => JSON.stringify(item))
252.  }
253.  .height('100%')
254.  .cachedCount(2)
255.  .flingSpeedLimit(1600)
256.  .listDirection(Axis.Vertical)
257.  .scrollBar(BarState.Off)
258.  .edgeEffect(EdgeEffect.None)
259.  .nestedScroll({ scrollForward: NestedScrollMode.PARENT_FIRST, scrollBackward: NestedScrollMode.PARENT_FIRST })
260.  .onScrollFrameBegin((offset: number) => {
261.  this.leftScroller.scrollTo({
262.  xOffset: 0,
263.  yOffset: this.verticalScroller.currentOffset().yOffset + offset,
264.  animation: false
265.  });
266.  return { offsetRemain: offset };
267.  })
268.  .onScrollIndex((start: number, end: number) => {
269.  this.startIndex = start;
270.  this.endIndex = end;
271.  // Scroll only the items within the current display range
272.  for (let i = start; i <= end; i++) {
273.  this.listScrollerArr[i].scrollTo({ xOffset: this.remainOffset, yOffset: 0, animation: false });
274.  }
275.  })
276.  }
277.  .position({ x: 140, y: 0 })
278.  .onDidScroll(() => {
279.  this.topScroller.scrollTo({ xOffset: this.remainOffset, yOffset: 0, animation: false });
280.  })
281.  .scrollBar(BarState.Off)
282.  .edgeEffect(EdgeEffect.None)
283.  .scrollable(ScrollDirection.Horizontal)
284.  .backgroundColor(0xDCDCDC)
285.  .height('calc(100% - 48vp)')
286.  .width('calc(100% - 140vp)')
287.  }
288. }

```


[SlideTheListLeftRightUpAndDown.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SlideTheListLeftRightUpAndDown.ets#L21-L308)



2.加载的数据源



```typescript
1. export class CommonDataSource<T> implements IDataSource {
2.  private listeners: DataChangeListener[] = [];
3.  protected originDataArray: T[] = [];
4.
5.
6.  totalCount(): number {
7.  return this.originDataArray.length;
8.  }
9.
10.
11.  getAllData(): T[] {
12.  return this.originDataArray;
13.  }
14.
15.
16.  getData(index: number) {
17.  return this.originDataArray[index];
18.  }
19.
20.
21.  addData(index: number, data: T): void {
22.  this.originDataArray.splice(index, 0, data);
23.  this.notifyDataAdd(index);
24.  }
25.
26.
27.  pushData(data: T): void {
28.  this.originDataArray.push(data);
29.  this.notifyDataAdd(this.originDataArray.length - 1);
30.  }
31.
32.
33.  pushDataArray(...items: T[]): void {
34.  for (let data of items) {
35.  this.originDataArray.push(data);
36.  this.notifyDataAdd(this.originDataArray.length - 1);
37.  }
38.  }
39.
40.
41.  clear() {
42.  this.originDataArray.splice(0, this.originDataArray.length)
43.  this.listeners.forEach(listener => {
44.  listener.onDataDelete(0);
45.  })
46.  }
47.
48.
49.  setData(dataArray?: T[]) {
50.  if (dataArray) {
51.  this.originDataArray = dataArray;
52.  } else {
53.  this.originDataArray = [];
54.  }
55.  this.notifyDataReload();
56.  }
57.
58.
59.  registerDataChangeListener(listener: DataChangeListener): void {
60.  if (this.listeners.indexOf(listener) < 0) {
61.  this.listeners.push(listener);
62.  }
63.  }
64.
65.
66.  unregisterDataChangeListener(listener: DataChangeListener): void {
67.  const pos = this.listeners.indexOf(listener);
68.  if (pos >= 0) {
69.  this.listeners.splice(pos, 1);
70.  }
71.  }
72.
73.
74.  notifyDataReload() {
75.  this.listeners.forEach(listener => {
76.  listener.onDataReloaded();
77.  })
78.  }
79.
80.
81.  notifyDataAdd(index: number) {
82.  this.listeners.forEach(listener => {
83.  listener.onDataAdd(index);
84.  })
85.  }
86.
87.
88.  notifyDataMove(from: number, to: number) {
89.  this.listeners.forEach(listener => {
90.  listener.onDataMove(from, to);
91.  })
92.  }
93.
94.
95.  notifyDataDelete(index: number) {
96.  this.listeners.forEach(listener => {
97.  listener.onDataDelete(index);
98.  })
99.  }
100.
101.
102.  notifyDataChange(index: number) {
103.  this.listeners.forEach(listener => {
104.  listener.onDataChange(index);
105.  })
106.  }
107. }

```


[CommonDataSource.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/viewmodel/CommonDataSource.ets#L21-L127)
