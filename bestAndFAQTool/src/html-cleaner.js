const DEFAULT_CONTENT_SELECTORS = [
  "article",
  "main",
  "[role='main']",
  ".markdown-body",
  ".doc-content",
  ".content",
  ".post-content",
  ".post-body",
  ".article-content",
  ".entry-content",
];

const JUNK_SELECTORS = [
  "script",
  "style",
  "noscript",
  "template",
  "svg",
  "canvas",
  "iframe",
  "header",
  "nav",
  "footer",
  "aside",
  "form",
  "button",
  "input",
  "select",
  "textarea",
  "[role='navigation']",
  "[role='banner']",
  "[role='contentinfo']",
  "[role='complementary']",
  "[aria-hidden='true']",
  "[hidden]",
  ".ad",
  ".ads",
  ".advert",
  ".advertisement",
  ".ad-banner",
  ".banner-ad",
  ".cookie",
  ".cookie-banner",
  ".modal",
  ".popup",
  ".sidebar",
  ".toc",
  ".breadcrumb",
  ".breadcrumbs",
  ".pagination",
  ".share",
  ".social",
  ".comments",
  ".related",
];

const CODE_TOOLBAR_LABELS = new Set(["收起", "自动换行", "深色代码主题", "复制"]);

export function cleanDocumentHtml(document, options = {}) {
  const selectors = options.selector
    ? [options.selector]
    : options.contentSelectors || DEFAULT_CONTENT_SELECTORS;
  const source = findContentRoot(document, selectors);
  const root = source.cloneNode(true);
  const baseUrl = document.baseURI || document.URL;

  removeJunk(root);
  removeHiddenElements(root);
  removeCodeToolbarLabels(root);
  removeEmptyContainers(root);
  absolutizeUrls(root, baseUrl);
  normalizeWhitespaceTextNodes(root);

  return root.innerHTML.trim();
}

export function findContentRoot(document, selectors = DEFAULT_CONTENT_SELECTORS) {
  for (const selector of selectors) {
    const element = document.querySelector(selector);
    if (element && textLength(element) > 0) {
      return element;
    }
  }

  const candidates = [...document.body.querySelectorAll("article, main, section, div")]
    .filter((element) => textLength(element) > 40)
    .sort((a, b) => scoreElement(b) - scoreElement(a));

  return candidates[0] || document.body;
}

function removeJunk(root) {
  root.querySelectorAll(JUNK_SELECTORS.join(",")).forEach((element) => element.remove());
}

function removeHiddenElements(root) {
  root.querySelectorAll("*").forEach((element) => {
    const style = element.getAttribute("style") || "";
    if (/display\s*:\s*none|visibility\s*:\s*hidden/i.test(style)) {
      element.remove();
    }
  });
}

function removeCodeToolbarLabels(root) {
  root.querySelectorAll("*").forEach((element) => {
    const text = normalizedText(element);
    if (CODE_TOOLBAR_LABELS.has(text)) {
      element.remove();
    }
  });
}

function removeEmptyContainers(root) {
  const candidates = [...root.querySelectorAll("div,span")].reverse();

  for (const element of candidates) {
    if (
      normalizedText(element) === "" &&
      element.querySelector("pre,code,img,video,audio,table,iframe") === null
    ) {
      element.remove();
    }
  }
}

function absolutizeUrls(root, baseUrl) {
  absolutizeAttribute(root, "a[href]", "href", baseUrl);
  absolutizeAttribute(root, "img[src]", "src", baseUrl);
  absolutizeAttribute(root, "video[src]", "src", baseUrl);
  absolutizeAttribute(root, "audio[src]", "src", baseUrl);
  absolutizeSrcset(root, "img[srcset], source[srcset]", baseUrl);
}

function absolutizeAttribute(root, selector, attribute, baseUrl) {
  root.querySelectorAll(selector).forEach((element) => {
    const value = element.getAttribute(attribute);
    if (!value || isSpecialUrl(value)) return;
    const url = toAbsoluteUrl(value, baseUrl);
    if (url) element.setAttribute(attribute, url);
  });
}

function absolutizeSrcset(root, selector, baseUrl) {
  root.querySelectorAll(selector).forEach((element) => {
    const value = element.getAttribute("srcset");
    if (!value) return;

    const absolute = value
      .split(",")
      .map((item) => {
        const [url, ...descriptor] = item.trim().split(/\s+/);
        if (!url || isSpecialUrl(url)) return item.trim();
        return [toAbsoluteUrl(url, baseUrl) || url, ...descriptor].join(" ");
      })
      .join(", ");

    element.setAttribute("srcset", absolute);
  });
}

function normalizeWhitespaceTextNodes(root) {
  const nodeFilter = root.ownerDocument.defaultView.NodeFilter;
  const walker = root.ownerDocument.createTreeWalker(root, nodeFilter.SHOW_TEXT);
  const nodes = [];

  while (walker.nextNode()) {
    nodes.push(walker.currentNode);
  }

  for (const node of nodes) {
    node.nodeValue = node.nodeValue.replace(/[ \t\f\v]+/g, " ");
  }
}

function scoreElement(element) {
  const paragraphs = element.querySelectorAll("p").length;
  const headings = element.querySelectorAll("h1,h2,h3").length;
  const links = element.querySelectorAll("a").length;

  return textLength(element) + paragraphs * 80 + headings * 60 - links * 20;
}

function textLength(element) {
  return (element.textContent || "").replace(/\s+/g, " ").trim().length;
}

function normalizedText(element) {
  return (element.textContent || "").replace(/\s+/g, " ").trim();
}

function isSpecialUrl(value) {
  return /^(#|mailto:|tel:|javascript:|data:)/i.test(value);
}

function toAbsoluteUrl(value, baseUrl) {
  try {
    return new URL(value, baseUrl).href;
  } catch {
    return null;
  }
}
