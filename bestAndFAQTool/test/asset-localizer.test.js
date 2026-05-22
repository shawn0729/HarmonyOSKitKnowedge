import assert from "node:assert/strict";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

import { localizeHtmlImageAssets } from "../src/asset-localizer.js";

test("downloads remote images into shared assets directory and rewrites src relative to markdown file", async () => {
  const tmpDir = await mkdtemp(path.join(os.tmpdir(), "asset-localizer-"));
  const assetsDir = path.join(tmpDir, "assets");
  const markdownDir = path.join(tmpDir, "图片处理服务");

  try {
    const result = await localizeHtmlImageAssets(
      `<main><p>示例</p><img src="https://example.com/docs/images/a.png?token=1" alt="图"></main>`,
      {
        assetsDir,
        markdownDir,
        documentBaseName: "0001-图片获取",
        fetchAsset: async (url) => ({
          ok: true,
          status: 200,
          headers: { get: () => "image/png" },
          arrayBuffer: async () => Buffer.from(`image:${url}`),
        }),
      },
    );

    assert.match(result.html, /src="\.\.\/assets\/0001-图片获取-image-001\.png"/);
    assert.equal(result.assets.length, 1);
    assert.equal(
      await readFile(path.join(assetsDir, "0001-图片获取-image-001.png"), "utf8"),
      "image:https://example.com/docs/images/a.png?token=1",
    );
  } finally {
    await rm(tmpDir, { recursive: true, force: true });
  }
});
