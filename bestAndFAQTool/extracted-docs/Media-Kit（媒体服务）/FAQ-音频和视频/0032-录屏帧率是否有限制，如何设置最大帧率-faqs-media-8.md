# 录屏帧率是否有限制，如何设置最大帧率

可以调用OH_AVScreenCapture_SetMaxVideoFrameRate()设置录屏时的最大帧率，实际帧率受限于设备能力，具体规格可参考[设置录屏时的最大帧率](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-h#oh_avscreencapture_setmaxvideoframerate)。录屏的帧率需同时满足编解码的规格，请参考[设置正确的视频帧率](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/obtain-supported-codecs#%E8%AE%BE%E7%BD%AE%E6%AD%A3%E7%A1%AE%E7%9A%84%E8%A7%86%E9%A2%91%E5%B8%A7%E7%8E%87)。
