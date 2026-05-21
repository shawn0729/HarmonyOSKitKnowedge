# API与错误码

## 使用方式

- 当回答已经确定主主题，但需要补充 Image Kit API 参考入口时，读取本文件。

## API 总入口

- 2 Image Kit（图片处理服务）API参考：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/image-api
- 2.1 ArkTS API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/image-arkts
- 2.2 C API：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/image-c

## 主题到 API 的映射规则

### 图片处理 相关接口

- ArkTS API
  - 2.1.1 @ohos.multimedia.image (图片处理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image

### 元数据 / EXIF / Picture / AuxiliaryPicture

- ArkTS API
  - 2.1.1.3 Interface (AuxiliaryPicture)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-auxiliarypicture
  - 2.1.1.9 Interface (Metadata)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-metadata
  - 2.1.1.10 Interface (Picture)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-picture

### Image 相关接口

- ArkTS API
  - 2.1.1.4 Interface (Image)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image

- C API
  - 2.2.1.2 Image：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image

### 图片接收与生产

- ArkTS API
  - 2.1.1.5 Interface (ImageCreator)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagecreator
  - 2.1.1.7 Interface (ImageReceiver)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver

### 图片编码与打包

- ArkTS API
  - 2.1.1.6 Interface (ImagePacker)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker

### 图片解码与图片源

- ArkTS API
  - 2.1.1.8 Interface (ImageSource)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource

### 图片编辑和 PixelMap 操作

- ArkTS API
  - 2.1.1.11 Interface (PixelMap)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap

### 基于Sendable对象的图片处理 相关接口

- ArkTS API
  - 2.1.2 @ohos.multimedia.sendableImage (基于Sendable对象的图片处理)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage

### 图片增强 / 超分 / Processing

- ArkTS API
  - 2.1.3 @ohos.multimedia.videoProcessingEngine (视频处理引擎)：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-videoprocessingengine

- C API
  - 2.2.1.3 ImageEffect：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageeffect
  - 2.2.1.4 ImageProcessing：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing

### Image_NativeModule 相关接口

- C API
  - 2.2.1.1 Image_NativeModule：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule

### 错误码与异常定位

- 通用入口
  - 2.3 错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/image-arkts-errcode
  - 2.3.1 Image错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-image
  - 2.3.2 视频处理引擎错误码：
    - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-videoprocessingengine

## 直接映射

- `图片处理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-image
- `AuxiliaryPicture`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-auxiliarypicture
- `Image`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image
- `ImageCreator`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagecreator
- `ImagePacker`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagepacker
- `ImageReceiver`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagereceiver
- `ImageSource`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-imagesource
- `Metadata`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-metadata
- `Picture`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-picture
- `PixelMap`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-pixelmap
- `基于Sendable对象的图片处理`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendableimage
- `视频处理引擎`：
  - https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-videoprocessingengine

## 使用约束

- 本文件只负责 API 入口定位，不替代开发指南。
- 当开发指南已经能回答推荐实现方式时，API 参考只作为补充。
- 排障和经验问题优先结合 `best-practices-and-faq.md`。

## 路由提示

- 问 @ohos.multimedia.image、图片处理、AuxiliaryPicture、Image、ImageCreator 时，转到 `api-and-error-codes.md`
- 如果当前问题本质上是实现流程，先回到对应开发指南主题，再用本主题补接口细节。
- 如果当前问题是错误定位或适配异常，再补 `best-practices-and-faq.md`。
