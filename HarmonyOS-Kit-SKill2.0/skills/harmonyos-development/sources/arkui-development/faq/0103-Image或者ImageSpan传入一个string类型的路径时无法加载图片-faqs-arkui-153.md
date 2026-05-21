# Image或者ImageSpan传入一个string类型的路径时无法加载图片

---

目前规格上只支持常量，需要把string提取出来用$r( )包裹。例如：



```ini
1. localImageName = $r( 'app.media.icon' )

```


[ImageStrPath.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImageStrPath.ets#L6-L6)
