# 如何监听音频输出设备变更信息以作为应用处理自动暂停的依据

**问题现象**



使用audioRoutingManager.on('deviceChange')监听设备连接状态变化，导致正常播放时，应用无故自动暂停。



**问题原因**



错误使用监听音频输出设备变化的接口，audioRoutingManager.on('deviceChange')监听的是全局输入和输出设备的连接状态变化，不与音频流绑定。因此，不建议作为应用处理自动暂停的依据。



**解决措施**



开发者可使用[audioRenderer.on('outputDeviceChangeWithInfo')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiorenderer#onoutputdevicechangewithinfo11)，用于监听该音频流输出设备变化及原因。当系统出现音频输出设备的上下线、用户强选、设备抢占或设备选择策略变更等情况，导致音频流输出设备变更时，系统将通过该接口通知应用当前音频流设备变更信息，包含当前音频流输出设备信息和设备变更原因。应用可根据变更原因做相应业务处理，具体详情参考[音频流输出设备变更原因](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-change#%E9%9F%B3%E9%A2%91%E6%B5%81%E8%BE%93%E5%87%BA%E8%AE%BE%E5%A4%87%E5%8F%98%E6%9B%B4%E5%8E%9F%E5%9B%A0)。
