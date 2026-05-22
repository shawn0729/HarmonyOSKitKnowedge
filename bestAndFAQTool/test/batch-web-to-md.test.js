import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";

import * as batchWebToMd from "../src/batch-web-to-md.js";

test("single URL input leaves title unset when no explicit title is provided", () => {
  const url = "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-5";

  assert.equal(typeof batchWebToMd.buildSingleUrlLink, "function");
  assert.deepEqual(batchWebToMd.buildSingleUrlLink({ input: url }), {
    title: undefined,
    url,
  });
});

test("normalizes Huawei document titles by removing site suffix", () => {
  assert.equal(
    batchWebToMd.normalizeTitle(
      "如何自定义Tabs页签导航栏及其对齐方式-方舟UI框架（ArkUI）-UI框架-应用框架开发-开发 - 华为HarmonyOS开发者",
    ),
    "如何自定义Tabs页签导航栏及其对齐方式",
  );
  assert.equal(
    batchWebToMd.normalizeTitle(
      "通过PixelMap_CreatePixelMap创建的对象，内存在ArkTS侧和Native侧是否共享-图片处理（Image）-拍照和图片-媒体开发-开发 - 华为HarmonyOS开发者",
    ),
    "通过PixelMap_CreatePixelMap创建的对象，内存在ArkTS侧和Native侧是否共享",
  );
});

test("builds batch markdown content without source link header", () => {
  assert.equal(typeof batchWebToMd.buildMarkdownContent, "function");

  const content = batchWebToMd.buildMarkdownContent({
    title: "图片获取与保存实践",
    markdown: "正文内容\n",
  });

  assert.equal(content, "# 图片获取与保存实践\n\n正文内容\n");
  assert.doesNotMatch(content, /原文链接|---/);
});

test("uses kit Chinese name as section output directory when available", () => {
  assert.equal(typeof batchWebToMd.outputDirNameForSection, "function");
  assert.equal(
    batchWebToMd.outputDirNameForSection({
      title: "3-Image-Kit（图片处理服务）最佳实践：",
      slug: "3-Image-Kit（图片处理服务）最佳实践：",
    }),
    "Image-Kit（图片处理服务）",
  );
  assert.equal(
    batchWebToMd.outputDirNameForSection({
      title: "3 最佳实践-程序包结构",
      slug: "3-最佳实践-程序包结构",
      kitChineseName: "Ability-Kit（程序框架服务）",
    }),
    "Ability-Kit（程序框架服务）",
  );
  assert.equal(
    batchWebToMd.outputDirNameForSection({
      title: "3 最佳实践-组件封装与复用",
      slug: "3-最佳实践-组件封装与复用",
    }),
    "3-最佳实践-组件封装与复用",
  );
});

test("builds flat section output paths grouped by kind and topic", () => {
  assert.equal(typeof batchWebToMd.buildSectionOutputContext, "function");

  assert.deepEqual(
    batchWebToMd.buildSectionOutputContext("extracted-docs", {
      title: "3 最佳实践-程序包结构",
      slug: "3-最佳实践-程序包结构",
      kitChineseName: "Ability-Kit（程序框架服务）",
    }),
    {
      sectionDir: path.join("extracted-docs", "Ability-Kit（程序框架服务）", "最佳实践-程序包结构"),
      assetsDir: path.join("extracted-docs", "Ability-Kit（程序框架服务）", "assets"),
    },
  );

  assert.deepEqual(
    batchWebToMd.buildSectionOutputContext("extracted-docs", {
      title: "4 FAQ",
      slug: "4-FAQ",
      kitChineseName: "ArkTS（方舟编程语言）",
    }),
    {
      sectionDir: path.join("extracted-docs", "ArkTS（方舟编程语言）", "FAQ-ArkTS（方舟编程语言）"),
      assetsDir: path.join("extracted-docs", "ArkTS（方舟编程语言）", "assets"),
    },
  );
});

test("builds audio and video section output paths under Media Kit", () => {
  assert.deepEqual(
    batchWebToMd.buildSectionOutputContext("extracted-docs", {
      title: "1 音频和视频最佳实践",
      slug: "1-音频和视频最佳实践",
      kitChineseName: "Media-Kit（媒体服务）",
    }),
    {
      sectionDir: path.join("extracted-docs", "Media-Kit（媒体服务）", "最佳实践-音频和视频"),
      assetsDir: path.join("extracted-docs", "Media-Kit（媒体服务）", "assets"),
    },
  );

  assert.deepEqual(
    batchWebToMd.buildSectionOutputContext("extracted-docs", {
      title: "2 音频和视频faq",
      slug: "2-音频和视频faq",
      kitChineseName: "Media-Kit（媒体服务）",
    }),
    {
      sectionDir: path.join("extracted-docs", "Media-Kit（媒体服务）", "FAQ-音频和视频"),
      assetsDir: path.join("extracted-docs", "Media-Kit（媒体服务）", "assets"),
    },
  );
});
