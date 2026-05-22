# 如何获取系统支持的编解码能力

提供两种方法来获取音视频编解码能力实例：



方式一：通过OH_AVCodec_GetCapability获取系统推荐的音视频编解码器能力实例。该接口的推荐策略与OH_XXX_CreateByMime系列接口一致。



```cpp
1. // Obtain an example of the recommended audio AAC decoder capability from the system
2. OH_AVCapability *capability = OH_AVCodec_GetCapability(OH_AVCODEC_MIMETYPE_AUDIO_AAC, false);

```


[GetCapability.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/AudioKit/entry/src/main/ets/pages/GetCapability.cpp#L5-L6)



方式二：通过OH_AVCodec_GetCapabilityByCategory获取指定软件或硬件的编解码能力实例



```cpp
1. // Obtain an instance of video AVC encoder capability for the specified hardware
2. OH_AVCapability *capability = OH_AVCodec_GetCapabilityByCategory(OH_AVCODEC_MIMETYPE_VIDEO_AVC, true, HARDWARE);

```


[GetCapability.cpp](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AudioKit/entry/src/main/ets/pages/GetCapability.cpp#L10-L11)



获取能力实例成功后，可继续执行。系统会自动回收OH_AVCapability实例，开发者无需关注。



**参考链接**



[获取支持的编解码能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-supported-codecs)
