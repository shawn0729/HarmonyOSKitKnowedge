import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { JSDOM } from "jsdom";

const IMAGE_EXTENSIONS = new Set([".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp"]);

export async function localizeHtmlImageAssets(html, options = {}) {
  const { assetsDir, markdownDir, documentBaseName } = options;
  if (!assetsDir || !markdownDir || !documentBaseName) {
    return { html, assets: [] };
  }

  const dom = new JSDOM(`<body>${html}</body>`);
  const document = dom.window.document;
  const images = [...document.querySelectorAll("img[src]")];
  const assets = [];
  let imageIndex = 0;

  for (const image of images) {
    const sourceUrl = image.getAttribute("src");
    if (!isHttpUrl(sourceUrl)) continue;

    imageIndex += 1;
    const asset = await downloadImageAsset(sourceUrl, {
      assetsDir,
      documentBaseName,
      imageIndex,
      fetchAsset: options.fetchAsset || globalThis.fetch,
    });
    const relativePath = toMarkdownRelativePath(markdownDir, asset.path);
    image.setAttribute("src", relativePath);
    assets.push(asset);
  }

  return {
    html: document.body.innerHTML,
    assets,
  };
}

async function downloadImageAsset(sourceUrl, options) {
  const { assetsDir, documentBaseName, imageIndex, fetchAsset } = options;
  if (typeof fetchAsset !== "function") {
    throw new Error("No fetch implementation is available for image assets.");
  }

  const response = await fetchAsset(sourceUrl);
  if (!response.ok) {
    throw new Error(`Failed to download image ${sourceUrl}: HTTP ${response.status}`);
  }

  const extension = extensionFromUrl(sourceUrl) || extensionFromContentType(response) || ".bin";
  const filename = `${documentBaseName}-image-${String(imageIndex).padStart(3, "0")}${extension}`;
  const outputPath = path.join(assetsDir, filename);
  const buffer = Buffer.from(await response.arrayBuffer());

  await mkdir(assetsDir, { recursive: true });
  await writeFile(outputPath, buffer);

  return {
    url: sourceUrl,
    path: outputPath,
  };
}

function extensionFromUrl(sourceUrl) {
  try {
    const parsed = new URL(sourceUrl);
    const extension = path.extname(parsed.pathname).toLowerCase();
    return IMAGE_EXTENSIONS.has(extension) ? extension : "";
  } catch {
    return "";
  }
}

function extensionFromContentType(response) {
  const contentType = response.headers?.get?.("content-type") || response.headers?.get?.("Content-Type") || "";
  if (/image\/png/i.test(contentType)) return ".png";
  if (/image\/jpe?g/i.test(contentType)) return ".jpg";
  if (/image\/gif/i.test(contentType)) return ".gif";
  if (/image\/webp/i.test(contentType)) return ".webp";
  if (/image\/svg\+xml/i.test(contentType)) return ".svg";
  if (/image\/bmp/i.test(contentType)) return ".bmp";
  return "";
}

function toMarkdownRelativePath(markdownDir, assetPath) {
  return path.relative(markdownDir, assetPath).split(path.sep).join("/");
}

function isHttpUrl(value) {
  try {
    const url = new URL(value);
    return url.protocol === "http:" || url.protocol === "https:";
  } catch {
    return false;
  }
}
