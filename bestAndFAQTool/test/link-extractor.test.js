import assert from "node:assert/strict";
import test from "node:test";

import {
  buildDocumentFilename,
  extractTargetSectionsFromMarkdown,
  kitChineseNameFromTitle,
  isHttpUrl,
  slugifyFilenamePart,
} from "../src/link-extractor.js";

test("extracts links under multiple best-practice and FAQ sections", () => {
  const markdown = `# 1 开发指南:https://developer.huawei.com/guide

## 1.1 普通指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/a

# 3 最佳实践-组件封装与复用

### 3.1.1 组件动态创建:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ui-dynamic-operations
### 3.1.2 组件封装:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-ui-component-encapsulation

# 4 最佳实践-布局与弹窗

### 4.1.1 文本展开折叠:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-text-expand-collapse

# 8 其他

### 8.1 非目标:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/not-target

# 9 ArkUI FAQ:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-kit

## 9.1 如何自定义Tabs页签导航栏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-5
`;

  const sections = extractTargetSectionsFromMarkdown(markdown);

  assert.deepEqual(
    sections.map((section) => ({
      title: section.title,
      links: section.links.map((link) => link.title),
    })),
    [
      {
        title: "3 最佳实践-组件封装与复用",
        links: ["组件动态创建", "组件封装"],
      },
      {
        title: "4 最佳实践-布局与弹窗",
        links: ["文本展开折叠"],
      },
      {
        title: "9 ArkUI FAQ",
        links: ["如何自定义Tabs页签导航栏"],
      },
    ],
  );
});

test("deduplicates links within target sections", () => {
  const markdown = `# 3 最佳实践-示例

### 3.1 A:https://developer.huawei.com/a
### 3.2 A duplicate:https://developer.huawei.com/a
`;

  const sections = extractTargetSectionsFromMarkdown(markdown);

  assert.equal(sections.length, 1);
  assert.equal(sections[0].links.length, 1);
  assert.equal(sections[0].links[0].title, "A");
});

test("creates safe filenames with order, title, and URL slug", () => {
  const filename = buildDocumentFilename(7, {
    title: '如何自定义Tabs页签导航栏及其对齐方式?',
    url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-5",
  });

  assert.equal(filename, "0007-如何自定义Tabs页签导航栏及其对齐方式-faqs-arkui-5.md");
});

test("slugifies unsafe filename characters and detects HTTP URLs", () => {
  assert.equal(slugifyFilenamePart('A/B:C*D?"E<F>G|'), "A-B-C-D-E-F-G");
  assert.equal(isHttpUrl("https://developer.huawei.com"), true);
  assert.equal(isHttpUrl("/tmp/file.md"), false);
});

test("extracts kit Chinese name from target section titles", () => {
  assert.equal(
    kitChineseNameFromTitle("3 Image Kit（图片处理服务）最佳实践："),
    "Image-Kit（图片处理服务）",
  );
  assert.equal(
    kitChineseNameFromTitle("4-Camera-Kit（相机服务）FAQ："),
    "Camera-Kit（相机服务）",
  );
  assert.equal(kitChineseNameFromTitle("1 ArkTS（方舟编程语言）开发指南"), null);
  assert.equal(kitChineseNameFromTitle("3 最佳实践-组件封装与复用"), null);
});

test("uses document kit Chinese name for target sections without kit name", () => {
  const markdown = `\uFEFF# 1 Ability Kit（程序框架服务）开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-kit

# 3 最佳实践-程序包结构

### 3.1 桌面快捷方式:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-desktop-shortcuts

# 4 FAQ-程序框架

### 4.1 程序框架（Ability）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-kit
`;

  const sections = extractTargetSectionsFromMarkdown(markdown);

  assert.deepEqual(
    sections.map((section) => section.kitChineseName),
    ["Ability-Kit（程序框架服务）", "Ability-Kit（程序框架服务）"],
  );
});

test("keeps original document product name from the top heading instead of nested headings", () => {
  const markdown = `# 1 IAP Kit（应用内支付服务）开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-kit-guide

## 1.3 接入Skill（可选）:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-skill--introduction

## 1.10 IAP Kit常见问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq

### 1.10.1 证书问题:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-faq-2
`;

  const sections = extractTargetSectionsFromMarkdown(markdown);

  assert.equal(sections[0].kitChineseName, "IAP-Kit（应用内支付服务）");
});

test("falls back to top heading product name when no Chinese product name exists", () => {
  const markdown = `# 1 Performance Analysis Kit开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/performance-analysis-kit

## 1.2.7 App Killed（应用终止）检测:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appkilled-guidelines

# 2 Performance Analysis Kit API参考:https://developer.huawei.com/consumer/cn/doc/harmonyos-references/performance-analysis-kit

## 3 最佳实践-性能

### 3.1 性能概览:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-guide-reading
`;

  const sections = extractTargetSectionsFromMarkdown(markdown);

  assert.equal(sections[0].kitChineseName, "Performance-Analysis-Kit");
});

test("keeps original non-Kit top heading product names with Chinese display names", () => {
  const markdown = `# 1 ArkTS（方舟编程语言）开发指南:https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts

## 3 最佳实践

### 3.1 ArkTS高性能编程:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-high-performance

## 4 FAQ

### 4.1 方舟编程语言（ArkTS）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-kit
`;

  const sections = extractTargetSectionsFromMarkdown(markdown);

  assert.deepEqual(
    sections.map((section) => section.kitChineseName),
    ["ArkTS（方舟编程语言）", "ArkTS（方舟编程语言）"],
  );
});

test("groups audio and video best practices and FAQ under Media Kit", () => {
  const markdown = `# 1 音频和视频最佳实践:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-and-video

## 1.1 基于AVPlayer播放视频系列开发实践:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-avplayer-video-practices

# 2 音频和视频faq:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-video

## 2.1 音频（Audio）:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-kit
`;

  const sections = extractTargetSectionsFromMarkdown(markdown);

  assert.deepEqual(
    sections.map((section) => section.kitChineseName),
    ["Media-Kit（媒体服务）", "Media-Kit（媒体服务）"],
  );
});
