# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 Media Kit API 参考入口时，读取本文件。

## API 总入口

- 2 Media Kit（媒体服务）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/media-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/media-arkts
- 2.2 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/media-c

## 主题到 API 的映射规则

### 媒体服务 相关接口

- ArkTS API
  - 2.1.1 @ohos.multimedia.media (媒体服务)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media

### AVImageGenerator 相关接口

- ArkTS API
  - 2.1.1.3 Interface (AVImageGenerator)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avimagegenerator

- C API
  - 2.2.1.1 AVImageGenerator：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimagegenerator

### 元数据 / EXIF / Picture / AuxiliaryPicture

- ArkTS API
  - 2.1.1.4 Interface (AVMetadataExtractor)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avmetadataextractor

- C API
  - 2.2.1.2 AVMetadataExtractor：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor

### AVPlayer 相关接口

- ArkTS API
  - 2.1.1.5 Interface (AVPlayer)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer

- C API
  - 2.2.1.3 AVPlayer：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer

### AVRecorder 相关接口

- ArkTS API
  - 2.1.1.6 Interface (AVRecorder)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder

- C API
  - 2.2.1.4 AVRecorder：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder

### AVScreenCaptureRecorder 相关接口

- ArkTS API
  - 2.1.1.7 Interface (AVScreenCaptureRecorder)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder

### AVTranscoder 相关接口

- ArkTS API
  - 2.1.1.8 Interface (AVTranscoder)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avtranscoder

- C API
  - 2.2.1.5 AVTranscoder：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder

### 图片解码与图片源

- ArkTS API
  - 2.1.1.9 Interface (MediaSource)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-mediasource
  - 2.1.1.10 Interface (MediaSourceLoadingRequest)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-mediasourceloadingrequest

### AudioPlayer, deprecated 相关接口

- ArkTS API
  - 2.1.1.14 废弃的Interface (AudioPlayer, deprecated)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audioplayer

### AudioRecorder, deprecated 相关接口

- ArkTS API
  - 2.1.1.15 废弃的Interface (AudioRecorder, deprecated)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audiorecorder

### VideoPlayer, deprecated 相关接口

- ArkTS API
  - 2.1.1.16 废弃的Interface (VideoPlayer, deprecated)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-videoplayer

### multimedia 相关接口

- 通用入口
  - 2.1.2 multimedia：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/media-multimedia-arkts

### 音频池 相关接口

- ArkTS API
  - 2.1.2.1 SoundPool (音频池)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-soundpool

### AVScreenCapture 相关接口

- C API
  - 2.2.1.6 AVScreenCapture：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture

### AVSinkBase 相关接口

- C API
  - 2.2.1.7 AVSinkBase：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avsinkbase

### LowPowerAudioSink 相关接口

- C API
  - 2.2.1.8 LowPowerAudioSink：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpoweraudiosink

### LowPowerVideoSink 相关接口

- C API
  - 2.2.1.9 LowPowerVideoSink：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpowervideosink

### 图片增强 / 超分 / Processing

- C API
  - 2.2.1.10 VideoProcessing：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing
  - 2.2.3.41 NativeWindow：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-videoprocessing-nativewindow

### MediaKeySession 相关接口

- C API
  - 2.2.3.3 MediaKeySession：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-mediakeysession

### AVPlayerCallback 相关接口

- C API
  - 2.2.3.5 AVPlayerCallback：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer-avplayercallback

### 错误码与异常定位

- 通用入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/media-arkts-errcode
  - 2.3.1 Media错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media

## 直接映射

- `媒体服务`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-media
- `AVImageGenerator`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avimagegenerator
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avimagegenerator
- `AVMetadataExtractor`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avmetadataextractor
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor
- `AVPlayer`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avplayer
- `AVRecorder`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder
- `AVScreenCaptureRecorder`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avscreencapturerecorder
- `AVTranscoder`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avtranscoder
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avtranscoder
- `MediaSource`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-mediasource
- `MediaSourceLoadingRequest`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-mediasourceloadingrequest
- `AudioPlayer, deprecated`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audioplayer
- `AudioRecorder, deprecated`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audiorecorder
- `VideoPlayer, deprecated`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-videoplayer

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 Media Kit（媒体服务）、@ohos.multimedia.media、媒体服务、AVImageGenerator、AVMetadataExtractor 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
