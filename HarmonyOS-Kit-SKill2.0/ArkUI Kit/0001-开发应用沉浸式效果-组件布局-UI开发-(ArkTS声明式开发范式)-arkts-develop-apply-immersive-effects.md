# 开发应用沉浸式效果-组件布局-UI开发 (ArkTS声明式开发范式)

原文链接：https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects

---

## 概述

典型应用全屏窗口UI元素包括顶部[状态栏](https://developer.huawei.com/consumer/cn/doc/design-guides/status-bar-0000001776775568)、应用界面和底部导航区域（根据用户设置可表现为[导航条](https://developer.huawei.com/consumer/cn/doc/design-guides/navigation-0000001957075737)或三键导航），其中状态栏和导航区域，通常在沉浸式布局下称为避让区；避让区之外的区域称为安全区。开发应用沉浸式效果主要指通过调整状态栏、应用界面和底部导航区域的显示效果来减少状态栏、导航条或三键导航等系统界面的突兀感，从而使用户获得最佳的UI体验。



**图1** 界面元素示意图（此处以导航区域表现为导航条为例给出示意）



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Aj7rf9mMRuCeUMuIGY3OHQ/zh-cn_image_0000002596776313.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C49C3228A814EF3B950B4E2B4DEB0D5E903F427C7885EFF182E977665FED707F)



开发应用沉浸式效果主要要考虑如下几个设计要素：



- UI元素避让处理：底部导航区域可以响应点击事件，除此之外的可交互UI元素和应用关键信息不建议放到导航区域。状态栏显示系统信息，如果与界面元素有冲突，需要考虑避让状态栏。

- 沉浸式效果处理：设置状态栏的颜色和导航区域的显隐与界面元素颜色相匹配，不出现明显的突兀感。



针对上面的设计要求，可以通过如下两种方式实现应用沉浸式效果：



- [窗口全屏布局方案](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects#%E7%AA%97%E5%8F%A3%E5%85%A8%E5%B1%8F%E5%B8%83%E5%B1%80%E6%96%B9%E6%A1%88)：调整布局系统为全屏布局，界面元素延伸到状态栏和导航区域实现沉浸式效果。当不隐藏避让区时，可通过接口查询状态栏和导航区域进行可交互元素避让处理，并设置状态栏或导航区域的颜色或显隐等属性与界面元素匹配。当隐藏避让区时，通过对应接口设置全屏布局即可。
- [组件安全区方案](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects#%E7%BB%84%E4%BB%B6%E5%AE%89%E5%85%A8%E5%8C%BA%E6%96%B9%E6%A1%88)：布局系统保持安全区内布局，然后通过接口延伸绘制内容（如背景色，背景图）到状态栏和导航区域实现沉浸式效果。该方案下，界面元素仅做绘制延伸，无法单独布局到状态栏和导航区域，针对需要单独布局UI元素到状态栏和导航区域的场景建议使用窗口全屏布局方案处理。



## 窗口全屏布局方案

窗口全屏布局方案主要涉及以下[应用扩展布局，全屏显示，不隐藏避让区](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects#%E5%BA%94%E7%94%A8%E6%89%A9%E5%B1%95%E5%B8%83%E5%B1%80%E5%85%A8%E5%B1%8F%E6%98%BE%E7%A4%BA%E4%B8%8D%E9%9A%90%E8%97%8F%E9%81%BF%E8%AE%A9%E5%8C%BA)和[应用扩展布局，隐藏避让区](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects#%E5%BA%94%E7%94%A8%E6%89%A9%E5%B1%95%E5%B8%83%E5%B1%80%E9%9A%90%E8%97%8F%E9%81%BF%E8%AE%A9%E5%8C%BA)两个应用场景。



### 应用扩展布局，全屏显示，不隐藏避让区

可以通过调用窗口强制全屏布局接口[setWindowLayoutFullScreen()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowlayoutfullscreen9)实现界面元素延伸到状态栏和导航区域；然后通过接口[getWindowAvoidArea()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowavoidarea9)和[on('avoidAreaChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#onavoidareachange9)获取并动态监听避让区域的变更信息，页面布局根据避让区域信息进行动态调整；设置状态栏或导航区域的颜色或显隐等属性与界面元素进行匹配。



1. 调用setWindowLayoutFullScreen()接口设置窗口全屏。


  
  

```typescript
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';
5.
6. export default class EntryAbility extends UIAbility {
7.  // ...
8.
9.  onWindowStageCreate(windowStage: window.WindowStage): void {
10.  windowStage.loadContent('pages/Index', (err, data) => {
11.  if (err.code) {
12.  return;
13.  }
14.
15.  let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
16.  // 1. 设置窗口全屏
17.  let isLayoutFullScreen = true;
18.  windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
19.  console.info('Succeeded in setting the window layout to full-screen mode.');
20.  }).catch((err: BusinessError) => {
21.  console.error(`Failed to set the window layout to full-screen mode. Code is ${err.code}, message is ${err.message}`);
22.  });
23.  // 进行后续步骤2-3中的操作
24.  });
25.  }
26. }


```

2. 使用[getWindowAvoidArea()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#getwindowavoidarea9)接口获取当前布局遮挡区域（此处以状态栏、导航区域为例）。


  
  

```typescript
1. // EntryAbility.ets
2. // 2. 获取布局避让遮挡的区域
3. let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // 此处以导航条避让为例
4. let avoidArea = windowClass.getWindowAvoidArea(type);
5. let bottomRectHeight = avoidArea.bottomRect.height; // 获取到导航区域的高度
6. AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
7.
8. type = window.AvoidAreaType.TYPE_SYSTEM; // 以状态栏避让为例
9. avoidArea = windowClass.getWindowAvoidArea(type);
10. let topRectHeight = avoidArea.topRect.height; // 获取状态栏区域高度
11. AppStorage.setOrCreate('topRectHeight', topRectHeight);


```

3. 注册监听函数，动态获取避让区域的实时数据。常见的触发避让区回调的场景如下：应用窗口在全屏模式、悬浮模式、分屏模式之间的切换；应用窗口旋转；多折叠设备在屏幕折叠态和展开态之间的切换；应用窗口在多设备之间的流转。


  
  

```typescript
1. // EntryAbility.ets
2. // 3. 注册监听函数，动态获取避让区域数据
3. windowClass.on('avoidAreaChange', (data) => {
4.  if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
5.  let topRectHeight = data.area.topRect.height;
6.  AppStorage.setOrCreate('topRectHeight', topRectHeight);
7.  } else if (data.type == window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
8.  let bottomRectHeight = data.area.bottomRect.height;
9.  AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
10.  }
11. });


```

4. 布局中的UI元素需要避让状态栏和导航区域，否则可能产生UI元素重叠等情况。


  
  
  说明
       避让区域存在大小为0的情况，当获取到的避让区域为0时，开发者需注意针对性处理适配此时的页面区域和布局，避免贴边、内容裁剪等问题，影响应用界面正常显示或美观性。

     如下例子中，对控件顶部设置padding（具体数值与状态栏高度一致），实现对状态栏的避让；对底部设置padding（具体数值与底部导航区域高度一致），实现对导航条的避让。如果去掉顶部和底部的padding设置，即不避让状态栏和导航条，UI元素就会发生重叠。具体可见下文步骤中图2和图3的效果对比。


  
  

```typescript
1. // Index.ets
2. @Entry
3. @Component
4. struct Index {
5.  @StorageProp('bottomRectHeight')
6.  bottomRectHeight: number = 0;
7.  @StorageProp('topRectHeight')
8.  topRectHeight: number = 0;
9.
10.  build() {
11.  Column() {
12.  Row() {
13.  Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
14.  }.backgroundColor('#2786d9')
15.
16.  Row() {
17.  Text('Display Content 2').fontSize(30)
18.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
19.
20.  Row() {
21.  Text('Display Content 3').fontSize(30)
22.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
23.
24.  Row() {
25.  Text('Display Content 4').fontSize(30)
26.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
27.
28.  Row() {
29.  Text('Display Content 5').fontSize(30)
30.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
31.
32.  Row() {
33.  Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
34.  }.backgroundColor('#96dffa')
35.  }
36.  .width('100%')
37.  .height('100%')
38.  .alignItems(HorizontalAlign.Center)
39.  .backgroundColor('#d5d5d5')
40.  .justifyContent(FlexAlign.SpaceBetween)
41.  // top数值与状态栏区域高度保持一致；bottom数值与导航区域高度保持一致
42.  .padding({
43.  top: this.getUIContext().px2vp(this.topRectHeight),
44.  bottom: this.getUIContext().px2vp(this.bottomRectHeight)
45.  })
46.  }
47. }


```

5. 根据实际的UI界面显示或相关UI元素背景颜色等，还可以按需设置状态栏的文字颜色、背景色或设置导航区域的显示或隐藏，以使UI界面效果呈现和谐。状态栏和导航区域默认是透明的，透传的是应用界面的背景色。

     此例中UI颜色主要有两种，比较简单，故未对状态栏文字颜色、背景色进行设置，未对导航区域进行隐藏。

     **图2** 布局避让状态栏和导航区域（此处以导航区域表现为导航条为例给出示意）

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/CCXA44RfRLufjLvdYUMfBQ/zh-cn_image_0000002566336634.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=682D10AFED47A61048D8AFE567C1A3680B8587F4C3267AA8F87AEE580229498C)

     **图3** 布局未避让状态栏和导航区域，UI元素重叠（此处以导航区域表现为导航条为例给出示意）

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/gZyz4ppwQuykc0tPkAKKkQ/zh-cn_image_0000002596936249.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75661E92FF4285946F4F3BEBE21BE939E69B44315462B652197D5B3241DBD954)



### 应用扩展布局，隐藏避让区

此场景下状态栏和导航区域需要隐藏，适用于游戏、电影等应用场景。用户可以通过从底部上滑唤出导航条或三键导航。



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/nnVy6wZdRmWIeBLs8hnMgA/zh-cn_image_0000002566176984.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9D1E215D26986195CFB52FC0B49DD9F36E28C2AAC7DAA80D40AA1BED7D7E2F6)



1. 调用setWindowLayoutFullScreen()接口设置窗口全屏。


  
  

```typescript
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';
5.
6. export default class EntryAbility extends UIAbility {
7.  // ...
8.
9.  onWindowStageCreate(windowStage: window.WindowStage): void {
10.  windowStage.loadContent('pages/Index', (err, data) => {
11.  if (err.code) {
12.  return;
13.  }
14.
15.  let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
16.  // 1. 设置窗口全屏
17.  let isLayoutFullScreen = true;
18.  windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
19.  console.info('Succeeded in setting the window layout to full-screen mode.');
20.  }).catch((err: BusinessError) => {
21.  console.error(`Failed to set the window layout to full-screen mode. Code is ${err.code}, message is ${err.message}`);
22.  });
23.  // 进行后续步骤2中的状态栏和导航区域的隐藏操作
24.  });
25.  }
26. }


```

2. 调用[setSpecificSystemBarEnabled()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setspecificsystembarenabled11)接口设置状态栏和导航区域的具体显隐状态，此场景下将其设置为隐藏。


  
  

```typescript
1. // EntryAbility.ets
2. // 2. 设置状态栏隐藏
3. windowClass.setSpecificSystemBarEnabled('status', false).then(() => {
4.  console.info('Succeeded in setting the status bar to be invisible.');
5. }).catch((err: BusinessError) => {
6.  console.error(`Failed to set the status bar to be invisible. Code is ${err.code}, message is ${err.message}`);
7. });
8. // 2. 设置导航区域隐藏
9. windowClass.setSpecificSystemBarEnabled('navigationIndicator', false).then(() => {
10.  console.info('Succeeded in setting the navigation indicator to be invisible.');
11. }).catch((err: BusinessError) => {
12.  console.error(`Failed to set the navigation indicator to be invisible. Code is ${err.code}, message is ${err.message}`);
13. });


```

3. 在界面中无需进行导航区域避让操作。


  
  

```typescript
1. // Index.ets
2. @Entry()
3. @Component
4. struct Index {
5.  build() {
6.  Row() {
7.  Column() {
8.  Row() {
9.  Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
10.  }.backgroundColor('#2786d9')
11.
12.  Row() {
13.  Text('Display Content 2').fontSize(30)
14.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
15.
16.  Row() {
17.  Text('Display Content 3').fontSize(30)
18.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
19.
20.  Row() {
21.  Text('Display Content 4').fontSize(30)
22.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
23.
24.  Row() {
25.  Text('Display Content 5').fontSize(30)
26.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
27.
28.  Row() {
29.  Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
30.  }.backgroundColor('#96dffa')
31.  }
32.  .width('100%')
33.  .height('100%')
34.  .alignItems(HorizontalAlign.Center)
35.  .justifyContent(FlexAlign.SpaceBetween)
36.  .backgroundColor('#d5d5d5')
37.  }
38.  }
39. }


```



## 组件安全区方案

应用未使用setWindowLayoutFullScreen()接口设置窗口全屏布局时，默认采取组件安全区布局方案。



应用在默认情况下窗口背景绘制范围是全屏，但UI元素被限制在安全区内（自动排除状态栏和导航区域）进行布局，来避免界面元素被状态栏和导航区域遮盖。



**图4** 界面元素自动避让状态栏和导航区域示意图



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/q6wajaSUTOORB8aimDBMfA/zh-cn_image_0000002596776315.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACFC6D73579913536F29E7C495EC33DDC1A87DAD6AD117395A7D35AD296EE3D5)



针对状态栏和导航区域颜色与界面元素颜色不匹配问题，可以通过如下两种方式实现沉浸式效果：



- 状态栏和导航区域颜色相同场景，可以通过设置窗口的背景色来实现沉浸式效果。窗口背景色可通过[setWindowBackgroundColor()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-window#setwindowbackgroundcolor9)进行设置。


  
  

```typescript
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3.
4. export default class EntryAbility extends UIAbility {
5.  // ...
6.
7.  onWindowStageCreate(windowStage: window.WindowStage): void {
8.  windowStage.loadContent('pages/Index', (err) => {
9.  if (err.code) {
10.  return;
11.  }
12.
13.  // 设置全窗颜色和应用元素颜色一致
14.  windowStage.getMainWindowSync().setWindowBackgroundColor('#d5d5d5');
15.  });
16.  }
17. }


```
     界面状态栏和导航区域颜色相同场景。


  
  

```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct Example {
5.  build() {
6.  Column() {
7.  Row() {
8.  Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
9.  }.backgroundColor('#2786d9')
10.
11.  Row() {
12.  Text('Display Content 2').fontSize(30)
13.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
14.
15.  Row() {
16.  Text('Display Content 3').fontSize(30)
17.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
18.
19.  Row() {
20.  Text('Display Content 4').fontSize(30)
21.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
22.
23.  Row() {
24.  Text('Display Content 5').fontSize(30)
25.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
26.
27.  Row() {
28.  Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
29.  }.backgroundColor('#96dffa')
30.  }
31.  .width('100%').height('100%')
32.  .alignItems(HorizontalAlign.Center)
33.  .backgroundColor('#d5d5d5')
34.  .justifyContent(FlexAlign.SpaceBetween)
35.  }
36. }


```
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/cKoiBChmQ4eQXeB3lVpxmw/zh-cn_image_0000002566336636.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5156D7EE5FA3A616BA7949E0938EF0CC50E57A3F2051DF21BE0379CD4170D22B)

- 状态栏和导航区域颜色不同时，可以使用[expandSafeArea](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea)属性扩展安全区域属性进行调整。


  
  

```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct Example {
5.  build() {
6.  Column() {
7.  Row() {
8.  Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
9.  }.backgroundColor('#2786d9')
10.  // 设置顶部绘制延伸到状态栏
11.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
12.
13.  Row() {
14.  Text('Display Content 2').fontSize(30)
15.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
16.
17.  Row() {
18.  Text('Display Content 3').fontSize(30)
19.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
20.
21.  Row() {
22.  Text('Display Content 4').fontSize(30)
23.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
24.
25.  Row() {
26.  Text('Display Content 5').fontSize(30)
27.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
28.
29.  Row() {
30.  Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
31.  }.backgroundColor('#96dffa')
32.  // 设置底部绘制延伸到导航区域
33.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
34.  }
35.  .width('100%').height('100%')
36.  .alignItems(HorizontalAlign.Center)
37.  .backgroundColor('#d5d5d5')
38.  .justifyContent(FlexAlign.SpaceBetween)
39.  }
40. }


```
     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/5M12R224Qnyt_jqAGBqfaw/zh-cn_image_0000002596936251.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23A51A57ECF4735C2DD38632A1701BC057911500E747B2E2854DEF811271FBCE)



### 扩展安全区域属性原理

- 布局阶段按照安全区范围大小进行UI元素布局。

- 布局完成后查看设置了expandSafeArea的组件边界（不包括margin）是否和安全区边界相交。

- 如果设置了expandSafeArea的组件和安全区边界相交，根据expandSafeArea传递的属性则进一步扩大组件绘制区域大小覆盖状态栏、导航区域这些非安全区域。

- 上述过程仅改变组件自身绘制大小，不进行二次布局，不影响子节点和兄弟节点的大小和位置。

- 子节点可以单独设置该属性，只需要自身边界和安全区域重合就可以延伸自身大小至非安全区域内，需要确保父组件未设置clip等裁剪属性。

- 配置expandSafeArea属性组件进行绘制扩展时，需要关注组件不能配置固定宽高尺寸，百分比除外。

- 组件可以设置通用属性safeAreaPadding，给自身添加组件级安全区域。该属性作为一种特殊边距，在提供布局约束的同时作为安全区可以被一些系统组件利用。


  * safeAreaPadding位于原有的padding内侧。容器自外向内各层分别为border、padding、safeAreaPadding、内容区。当border和padding确定后，若容器可用空间不足以满足safeAreaPadding的设置，则优先分配给左侧和上侧safeAreaPadding、其次分配给右侧和下侧safeAreaPadding。safeAreaPadding实际尺寸确定后，余下空间为内容区。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/vkTR3vxlQROQRaDAbBfQMg/zh-cn_image_0000002566176986.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=624F2F6DE92DAEDAF430D8074E46609FAA353EEEBBFEDB0DB47B646BAE21D404)

  * 系统组件如Navigation、List、Scroll、Tabs等可以利用外层或容器自身safeAreaPadding实现扩大裁剪范围等能力。



### 背景图和视频场景

设置背景图、视频组件大小为安全区域大小并配置expandSafeArea属性。



说明



Video组件在使用expandSafeArea扩展到安全区域时，组件视频显示内容区域不支持扩展。



```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct SafeAreaExample1 {
5.  build() {
6.  Stack() {
7.  Image($r('app.media.bg'))
8.  .height('100%').width('100%')
9.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]) // 图片组件的绘制区域扩展至状态栏和导航区域。
10.  }.height('100%').width('100%')
11.  }
12. }

```



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/l8wnxAfxQByq8BVlV6f90A/zh-cn_image_0000002596776317.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C9C0BCAE7740C99692AF9B48E41161871F16DD11682B3808E0767B1964A84962)



### 滚动类场景

滚动容器设置expandSafeArea属性生效，但当父组件是滚动容器时，子组件设置expandSafeArea属性不生效。对于滚动容器的子组件，有两种方法实现沉浸式效果：



1. 设置父组件滚动容器和子组件相同的背景色，给父组件设置expandSafeArea属性扩展安全区。


  
  

```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct ScrollExample {
5.  scroller: Scroller = new Scroller()
6.  private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
7.
8.  build() {
9.  Stack({ alignContent: Alignment.TopStart }) {
10.  Scroll(this.scroller) {
11.  Column() {
12.  ForEach(this.arr, (item: number) => {
13.  Stack() {
14.  Text('Display Content ' + item.toString()).fontSize(30)
15.  }
16.  .width('80%').padding(20).borderRadius(15).backgroundColor(Color.White).margin({ top:30, bottom:30 })
17.  }, (item: string) => item)
18.  }.width('100%').backgroundColor('rgb(213,213,213)')
19.  }.backgroundColor('rgb(213,213,213)')
20.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
21.  }.width('100%').height('100%')
22.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
23.  }
24. }


```
     **图5** 滚动类容器设置expandSafeArea属性实现沉浸式效果

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/q05In60OQcaf7L7FlwKuNA/zh-cn_image_0000002566336638.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3865F29E98BF11AD07A8F2A7E6AC3D563B1110304D0D11FBE450DE791D8A5C97)

2. 设置父组件滚动容器和子组件相同的背景色，设置滚动容器的内容裁剪属性clipContent(ContentClipMode.SAFE_AREA)，将内容层裁剪区域扩展至避让区。


  
  

```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct ScrollExample {
5.  scroller: Scroller = new Scroller()
6.  private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
7.
8.  build() {
9.  Stack({ alignContent: Alignment.TopStart }) {
10.  Scroll(this.scroller) {
11.  Column() {
12.  ForEach(this.arr, (item: number) => {
13.  Stack() {
14.  Text('Display Content ' + item.toString()).fontSize(30)
15.  }
16.  .width('80%').padding(20).borderRadius(15).backgroundColor(Color.White).margin({ top:30, bottom:30 })
17.  }, (item: string) => item)
18.  }.width('100%').backgroundColor('rgb(213,213,213)')
19.  }.backgroundColor('rgb(213,213,213)')
20.  .clipContent(ContentClipMode.SAFE_AREA)
21.  }.width('100%').height('100%')
22.  }
23. }


```



**图6** 滚动类容器设置clipContent属性实现沉浸式效果



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/PaItezLJSc2Si09xPlIRuA/zh-cn_image_0000002596936253.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68EF65B3BB87438ABD6A316C8B4E431405484D8F9E8BEAE5E7C8AC634BE985C5)



### 底部页签场景

要求页签背景色能够延伸到导航区域（此处以导航区域表现为导航条为例给出示意），但页签内部可操作元素需要在导航区域之上。



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Mr1IOhDLQ_aFQnoOk3tBqA/zh-cn_image_0000002566176988.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C39CEE3E0ED7BC09EF54C5DF4E07D1654774E15BD15BDCCC9472C4070BE6E76F)



针对底部的页签部分，Navigation组件和Tabs组件默认实现了页签的延伸处理，开发者只需要保证Navigation和Tabs组件的底部边界和底部导航区域重合即可。若开发者显式调用expandSafeArea接口，则安全区效果由expandSafeArea参数指定。



如果未使用上述组件而是采用自定义方式实现页签的场景，可以针对底部元素设置expandSafeArea属性实现底部元素的背景扩展。



**图7** 顶部和底部UI元素未设置和设置expandSafeArea属性效果对比



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/iDbxyKWuSra_WwhU8a0q5Q/zh-cn_image_0000002596776319.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2519A3F1ACB7994D0C00552085161F3E7B6C162E330F15DF9B10D92D55A2B6AD)



```typescript
1. // xxx.ets
2. @Entry
3. @Component
4. struct Example {
5.  build() {
6.  Column() {
7.  Row() {
8.  Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
9.  }.backgroundColor('#2786d9')
10.  // 设置顶部绘制延伸到状态栏
11.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
12.
13.  Row() {
14.  Text('Display Content 2').fontSize(30)
15.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
16.
17.  Row() {
18.  Text('Display Content 3').fontSize(30)
19.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
20.
21.  Row() {
22.  Text('Display Content 4').fontSize(30)
23.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
24.
25.  Row() {
26.  Text('Display Content 5').fontSize(30)
27.  }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')
28.
29.  Row() {
30.  Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
31.  }.backgroundColor('#96dffa')
32.  // 设置底部绘制延伸到导航区域
33.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
34.  }
35.  .width('100%').height('100%')
36.  .alignItems(HorizontalAlign.Center)
37.  .backgroundColor('#d5d5d5')
38.  .justifyContent(FlexAlign.SpaceBetween)
39.  }
40. }

```



### 图文场景

当状态栏元素和底部导航区域元素不同时，无法单纯通过窗口背景色或者背景图组件延伸实现，此时需要对顶部元素和底部元素分别配置expandSafeArea属性，顶部元素配置expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.TOP])，底部元素配置expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM])。



![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/yuW7FXK-RVCmQPZyajlpbw/zh-cn_image_0000002566336640.png?HW-CC-KV=V1&amp;HW-CC-Date=20260508T070103Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B996470BD2BAA4811A851C6C70605D56E5C22E20441372C3C7031710033FE1B0)



```typescript
1. @Entry
2. @Component
3. struct Index {
4.  build() {
5.  Swiper() {
6.  Column() {
7.  Image($r('app.media.start'))
8.  .height('50%').width('100%')
9.  // 设置图片延伸到状态栏
10.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
11.  Column() {
12.  Text('HarmonyOS 第一课')
13.  .fontSize(32)
14.  .margin(30)
15.  Text('通过循序渐进的学习路径，无经验和有经验的开发者都可以掌握ArkTS语言声明式开发范式，体验更简洁、更友好的HarmonyOS应用开发旅程。')
16.  .fontSize(20).margin(20)
17.  }.height('50%').width('100%')
18.  .backgroundColor(Color.White)
19.  // 设置文本内容区背景延伸到导航栏
20.  .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
21.  }
22.  }
23.  .width('100%')
24.  .height('100%')
25.  // 关闭Swiper组件默认的裁剪效果以便子节点可以绘制在Swiper外。
26.  .clip(false)
27.  }
28. }

```
