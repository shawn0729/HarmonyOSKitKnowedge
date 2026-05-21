# SoundPool与AudioSession焦点策略适配

- 推荐优先使用[SoundPool](https://developer.huawei.com/consumer/cn/doc/harmonyos-references-V5/js-apis-inner-multimedia-soundpool-V5)，若应用使用SoundPool开发音频播放功能，且StreamUsage指定为Music、Movie、AudioBook等类型，播放短音，则其申请焦点时默认为并发模式，不会影响其他音频。
- 若应用不希望使用SoundPool，并且当前使用的流类型会打断其他音频播放，推荐使用[AudioSession](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/audio-playback-concurrency-V5#%E4%BD%BF%E7%94%A8audiosession%E7%AE%A1%E7%90%86%E9%9F%B3%E9%A2%91%E7%84%A6%E7%82%B9)相关接口，指定为MIX_WITH_OTHERS策略。
