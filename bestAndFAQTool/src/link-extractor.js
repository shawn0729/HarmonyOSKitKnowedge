const TARGET_SECTION_PATTERN = /(最佳实践|FAQ|常见问题)/i;
const HEADING_PATTERN = /^\uFEFF?(#{1,6})\s+(.+?)\s*$/;
const URL_PATTERN = /https?:\/\/[^\s)）>"'，。；、]+/g;
const MARKDOWN_LINK_PATTERN = /\[([^\]]+)]\((https?:\/\/[^)\s]+)\)/g;

export function extractTargetSectionsFromMarkdown(markdown) {
  const sections = [];
  const seenUrls = new Set();
  let activeSection = null;
  let documentKitChineseName = null;

  for (const line of markdown.split(/\r?\n/)) {
    const heading = parseHeading(line);

    if (heading) {
      if (activeSection && heading.level <= activeSection.level) {
        activeSection = null;
      }

      const titleUrl = extractTitleAndUrl(heading.text);
      const categoryTitle = titleUrl.title.trim();
      const linkTitle = stripLeadingNumber(titleUrl.title);
      const headingKitChineseName = kitChineseNameFromTitle(categoryTitle);

      if (TARGET_SECTION_PATTERN.test(categoryTitle)) {
        activeSection = {
          title: categoryTitle,
          level: heading.level,
          slug: slugifyFilenamePart(categoryTitle),
          kitChineseName: headingKitChineseName || specialKitNameFromTitle(categoryTitle) || documentKitChineseName,
          links: [],
        };
        sections.push(activeSection);
        continue;
      }

      if (heading.level === 1 && !documentKitChineseName) {
        documentKitChineseName = headingKitChineseName || productNameFromTopHeading(categoryTitle);
      }

      if (activeSection && titleUrl.url && !seenUrls.has(titleUrl.url)) {
        activeSection.links.push({
          title: linkTitle,
          url: titleUrl.url,
        });
        seenUrls.add(titleUrl.url);
      }

      continue;
    }

    if (!activeSection) continue;

    for (const link of extractLinksFromLine(line)) {
      if (seenUrls.has(link.url)) continue;
      activeSection.links.push(link);
      seenUrls.add(link.url);
    }
  }

  return sections.filter((section) => section.links.length > 0);
}

export function extractLinksFromLine(line) {
  const links = [];
  const consumedUrls = new Set();

  for (const match of line.matchAll(MARKDOWN_LINK_PATTERN)) {
    const [, title, url] = match;
    links.push({
      title: stripLeadingNumber(title.trim()),
      url,
    });
    consumedUrls.add(url);
  }

  for (const match of line.matchAll(URL_PATTERN)) {
    const [url] = match;
    if (consumedUrls.has(url)) continue;

    const before = line.slice(0, match.index).trim();
    const title = stripLeadingNumber(before.replace(/[:：-]\s*$/, "").trim()) || urlSlug(url);
    links.push({ title, url });
  }

  return links;
}

export function parseHeading(line) {
  const match = line.match(HEADING_PATTERN);
  if (!match) return null;

  return {
    level: match[1].length,
    text: match[2].trim(),
  };
}

export function extractTitleAndUrl(text) {
  const urls = [...text.matchAll(URL_PATTERN)];
  if (urls.length === 0) {
    return { title: text.trim(), url: null };
  }

  const url = urls[0][0];
  const title = text.slice(0, urls[0].index).replace(/[:：-]\s*$/, "").trim();
  return {
    title: title || urlSlug(url),
    url,
  };
}

export function buildDocumentFilename(index, link) {
  const order = String(index).padStart(4, "0");
  const title = slugifyFilenamePart(link.title || "untitled");
  const slug = slugifyFilenamePart(urlSlug(link.url));
  const base = trimFilenamePart(`${order}-${title}-${slug}`, 150);
  return `${base}.md`;
}

export function kitChineseNameFromTitle(title) {
  const match = String(title).match(/([A-Za-z][A-Za-z0-9\s-]*Kit)\s*（([^）]+)）/i);
  return match ? slugifyFilenamePart(`${match[1].trim()}（${match[2].trim()}）`) : null;
}

function productNameFromTopHeading(title) {
  const name = stripLeadingNumber(title)
    .replace(/开发指南$/i, "")
    .trim();
  return slugifyFilenamePart(name) || null;
}

function specialKitNameFromTitle(title) {
  return /音频和视频/i.test(String(title)) ? "Media-Kit（媒体服务）" : null;
}

export function slugifyFilenamePart(value) {
  return String(value)
    .replace(/[\\/:*?"<>|]/g, "-")
    .replace(/[\u0000-\u001f]/g, "")
    .replace(/\s+/g, "-")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "")
    .trim();
}

export function isHttpUrl(value) {
  try {
    const url = new URL(value);
    return url.protocol === "http:" || url.protocol === "https:";
  } catch {
    return false;
  }
}

export function urlSlug(url) {
  try {
    const parsed = new URL(url);
    const parts = parsed.pathname.split("/").filter(Boolean);
    return parts.at(-1) || parsed.hostname;
  } catch {
    return "document";
  }
}

function stripLeadingNumber(value) {
  return value.replace(/^\d+(?:\.\d+)*\s*/, "").trim();
}

function trimFilenamePart(value, maxLength) {
  if (value.length <= maxLength) return value;
  return value.slice(0, maxLength).replace(/-+[^-]*$/, "");
}
