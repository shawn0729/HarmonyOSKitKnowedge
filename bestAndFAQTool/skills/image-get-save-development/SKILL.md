---
name: image-get-save-development
description: Use when 生成、修改或排查 HarmonyOS 图片获取、相册选择、拍照、图片信息读取、EXIF 读取、PixelMap 处理、ImageSource、ImagePacker、图片编码、保存到应用文件目录或保存到系统相册相关 ArkTS 代码。
---

# 图片获取与保存开发

## 定位

用于实现 HarmonyOS 图片获取、读取、处理、编码和保存的端到端功能。该 Skill 关注跨 Kit 能力组合，而不是单个 API 查询。

## 适用场景

用户需求涉及：

- 从系统相册选择图片。
- 使用页面内嵌相册选择能力。
- 调用系统相机拍照。
- 读取图片基础信息或 EXIF 信息。
- 基于 URI/path 创建 `ImageSource`。
- 处理或保存 `PixelMap`。
- 使用 `ImagePacker` 编码图片。
- 保存图片到应用文件目录。
- 保存图片到系统相册。
- 处理媒体库授权、文件路径、异常和资源释放。

## 能力路由

- 相册选择、页面内嵌相册选择、拍照获取图片：
  读取 `capabilities/image-get-flow.md`

- 读取图片宽高、像素信息、EXIF 信息、创建 `ImageSource`：
  读取 `capabilities/image-read-flow.md`

- 保存 `PixelMap` 到文件目录、保存图片到系统相册、图片编码：
  读取 `capabilities/image-save-flow.md`

## 关键约束

- 图片获取阶段通常产出 URI，后续读取和保存流程都应围绕 URI/path 展开。
- 读取图片信息优先使用 `ImageSource`，不要直接假设 URI 一定可读。
- 保存 `PixelMap` 前必须先通过 `ImagePacker` 编码。
- 保存到应用目录和保存到系统相册是两个不同目标，不要混用。
- 保存到系统相册必须考虑媒体库授权或安全控件路径。
- 文件写入和图片编码必须包含异常处理和资源释放。

## 相关 Kit

- Image Kit：`@kit.ImageKit`
- Media Library Kit：`@kit.MediaLibraryKit`
- Camera Kit：`@kit.CameraKit`
- Core File Kit：`@kit.CoreFileKit`
- Basic Services Kit：错误处理、日志等基础能力
