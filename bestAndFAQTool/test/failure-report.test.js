import assert from "node:assert/strict";
import test from "node:test";

import { buildFailedLinksMarkdown } from "../src/failure-report.js";

test("builds a unified failed links markdown report", () => {
  const markdown = buildFailedLinksMarkdown([
    {
      input: "Account Kit.md",
      section: "3 FAQ-账号",
      title: "无法打开页面",
      url: "https://developer.huawei.com/broken",
      status: "failed",
      error: "Timeout 60000ms exceeded",
    },
    {
      input: "Audio Kit.md",
      section: "4 FAQ-音频",
      title: "已转换页面",
      url: "https://developer.huawei.com/ok",
      status: "ok",
    },
  ]);

  assert.match(markdown, /^# 转换失败链接/);
  assert.match(markdown, /## Account Kit\.md/);
  assert.match(markdown, /标题：无法打开页面/);
  assert.match(markdown, /链接：https:\/\/developer\.huawei\.com\/broken/);
  assert.match(markdown, /错误：Timeout 60000ms exceeded/);
  assert.doesNotMatch(markdown, /Audio Kit\.md/);
});

test("reports when there are no failed links", () => {
  assert.equal(buildFailedLinksMarkdown([]), "# 转换失败链接\n\n无失败链接。\n");
});
