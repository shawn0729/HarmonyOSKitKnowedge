#!/usr/bin/env node
import { mkdir, readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import {
  buildDocumentFilename,
  extractTargetSectionsFromMarkdown,
  isHttpUrl,
  kitChineseNameFromTitle,
  slugifyFilenamePart,
  urlSlug,
} from "./link-extractor.js";
import { localizeHtmlImageAssets } from "./asset-localizer.js";
import { convertHtmlToMarkdown, fetchCleanPage } from "./web-to-md.js";

const DEFAULT_OUT_DIR = "extracted-docs";
const DEFAULT_WAIT_MS = 3000;
const DEFAULT_TIMEOUT_MS = 60000;

async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (!args.input) {
    printUsage();
    process.exitCode = 1;
    return;
  }

  if (isHttpUrl(args.input)) {
    await convertSingleUrlInput(args);
    return;
  }

  await convertMarkdownNavigationInput(args);
}

async function convertSingleUrlInput(args) {
  await mkdir(args.out, { recursive: true });

  const result = await convertLink(
    buildSingleUrlLink(args),
    args,
    {
      assetsDir: path.join(args.out, "assets"),
      index: 1,
      markdownDir: args.out,
    },
  );
  const filename = buildDocumentFilename(1, {
    title: result.title,
    url: result.url,
  });
  const outputPath = path.join(args.out, filename);

  await writeOutput(outputPath, result.content, args);
  await writeManifest(args.out, [
    {
      title: result.title,
      url: result.url,
      output: outputPath,
    },
  ]);

  process.stderr.write(`Wrote ${outputPath}\n`);
}

export function buildSingleUrlLink(args) {
  return {
    title: args.title,
    url: args.input,
  };
}

async function convertMarkdownNavigationInput(args) {
  const markdown = await readFile(args.input, "utf8");
  const sections = extractTargetSectionsFromMarkdown(markdown);
  const manifest = [];
  let processed = 0;

  if (sections.length === 0) {
    throw new Error("未找到包含“最佳实践 / FAQ / 常见问题”的大类链接。");
  }

  for (const section of sections) {
    const outputContext = buildSectionOutputContext(args.out, section);
    const sectionDir = outputContext.sectionDir;
    await mkdir(sectionDir, { recursive: true });

    let sectionIndex = 0;
    for (const link of section.links) {
      if (args.limit && processed >= args.limit) {
        await writeManifest(args.out, manifest);
        return;
      }

      sectionIndex += 1;
      processed += 1;

      try {
        const result = await convertLink(link, args, {
          assetsDir: outputContext.assetsDir,
          index: sectionIndex,
          markdownDir: sectionDir,
        });
        const filename = buildDocumentFilename(sectionIndex, {
          title: result.title,
          url: result.url,
        });
        const outputPath = path.join(sectionDir, filename);
        await writeOutput(outputPath, result.content, args);
        manifest.push({
          section: section.title,
          title: result.title,
          url: result.url,
          output: outputPath,
          status: "ok",
        });
        process.stderr.write(`Wrote ${outputPath}\n`);
      } catch (error) {
        manifest.push({
          section: section.title,
          title: link.title,
          url: link.url,
          status: "failed",
          error: error.message,
        });
        process.stderr.write(`Failed ${link.url}: ${error.message}\n`);
      }
    }
  }

  await writeManifest(args.out, manifest);
}

async function convertLink(link, args, outputContext = {}) {
  const page = await fetchCleanPage({
    url: link.url,
    wait: args.wait,
    timeout: args.timeout,
    waitUntil: args.waitUntil,
    selector: args.selector,
  });
  const title = normalizeTitle(link.title || page.title || urlSlug(link.url));
  const documentBaseName = path.basename(
    buildDocumentFilename(outputContext.index || 1, {
      title,
      url: link.url,
    }),
    ".md",
  );
  const localized = await localizeHtmlImageAssets(page.html, {
    assetsDir: outputContext.assetsDir,
    markdownDir: outputContext.markdownDir,
    documentBaseName,
  });
  const markdown = await convertHtmlToMarkdown(localized.html, {
    command: args.converter,
    preprocess: false,
  });
  const content = buildMarkdownContent({ title, markdown });

  return {
    title,
    url: link.url,
    content,
  };
}

export function buildMarkdownContent({ title, markdown }) {
  return `# ${title}\n\n${markdown.trim()}\n`;
}

export function outputDirNameForSection(section) {
  return section.kitChineseName || kitChineseNameFromTitle(section.title) || slugifyFilenamePart(section.slug);
}

export function buildSectionOutputContext(outDir, section) {
  const kitDir = path.join(outDir, outputDirNameForSection(section));
  const sectionDirName = slugifyFilenamePart(`${sectionKindDirName(section)}-${sectionTopicDirName(section)}`);
  return {
    sectionDir: path.join(kitDir, sectionDirName),
    assetsDir: path.join(kitDir, "assets"),
  };
}

function sectionKindDirName(section) {
  return /FAQ|常见问题/i.test(section.title) ? "FAQ" : "最佳实践";
}

function sectionTopicDirName(section) {
  const withoutOrder = String(section.title)
    .replace(/^\d+(?:\.\d+)*[\s-]*/, "")
    .trim();
  const withoutKitName = withoutOrder
    .replace(/[A-Za-z][A-Za-z\s-]*Kit\s*（[^）]+）/gi, "")
    .trim();
  const topic = withoutKitName
    .replace(/^(最佳实践|FAQ|常见问题)\s*[-：:]?\s*/i, "")
    .replace(/\s*(最佳实践|FAQ|常见问题)\s*[-：:]?\s*$/i, "")
    .trim();

  return slugifyFilenamePart(topic || section.kitChineseName || section.slug);
}

async function writeOutput(outputPath, content, args) {
  if (!args.overwrite) {
    try {
      await readFile(outputPath);
      throw new Error(`文件已存在，使用 --overwrite 覆盖：${outputPath}`);
    } catch (error) {
      if (error.code !== "ENOENT") throw error;
    }
  }

  await mkdir(path.dirname(outputPath), { recursive: true });
  await writeFile(outputPath, content, "utf8");
}

async function writeManifest(outDir, manifest) {
  await mkdir(outDir, { recursive: true });
  await writeFile(
    path.join(outDir, "manifest.json"),
    `${JSON.stringify(manifest, null, 2)}\n`,
    "utf8",
  );
}

function parseArgs(argv) {
  const args = {
    out: DEFAULT_OUT_DIR,
    wait: DEFAULT_WAIT_MS,
    timeout: DEFAULT_TIMEOUT_MS,
    waitUntil: "networkidle",
    converter: "html-to-markdown",
    overwrite: false,
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];

    if (arg === "--out" || arg === "-o") {
      args.out = readValue(argv, ++index, arg);
    } else if (arg === "--limit") {
      args.limit = Number(readValue(argv, ++index, arg));
    } else if (arg === "--wait") {
      args.wait = Number(readValue(argv, ++index, arg));
    } else if (arg === "--timeout") {
      args.timeout = Number(readValue(argv, ++index, arg));
    } else if (arg === "--wait-until") {
      args.waitUntil = readValue(argv, ++index, arg);
    } else if (arg === "--selector" || arg === "-s") {
      args.selector = readValue(argv, ++index, arg);
    } else if (arg === "--converter") {
      args.converter = readValue(argv, ++index, arg);
    } else if (arg === "--title") {
      args.title = readValue(argv, ++index, arg);
    } else if (arg === "--overwrite") {
      args.overwrite = true;
    } else if (arg === "--help" || arg === "-h") {
      args.help = true;
    } else if (!args.input) {
      args.input = arg;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (args.help) {
    printUsage();
    process.exit(0);
  }

  if (args.limit !== undefined && (!Number.isFinite(args.limit) || args.limit < 1)) {
    throw new Error("--limit must be a positive number");
  }

  if (!Number.isFinite(args.wait) || args.wait < 0) {
    throw new Error("--wait must be a non-negative number");
  }

  if (!Number.isFinite(args.timeout) || args.timeout <= 0) {
    throw new Error("--timeout must be a positive number");
  }

  return args;
}

function readValue(argv, index, option) {
  const value = argv[index];
  if (!value) {
    throw new Error(`${option} requires a value`);
  }
  return value;
}

export function normalizeTitle(title) {
  const normalized = title
    .replace(/\s+/g, " ")
    .replace(/-[^-]+（[^）]+）(?:-[^-]+)*\s+-\s+华为HarmonyOS开发者$/, "")
    .trim();
  return normalized || "未命名文档";
}

function printUsage() {
  process.stderr.write(`Usage: batch-web-to-md <input-md-or-url> [options]

Options:
  -o, --out <dir>          Output directory, default ${DEFAULT_OUT_DIR}
      --limit <n>          Convert at most n links
      --overwrite          Overwrite existing output files
      --wait <ms>          Extra wait after page load, default ${DEFAULT_WAIT_MS}
      --timeout <ms>       Page load timeout, default ${DEFAULT_TIMEOUT_MS}
      --wait-until <state> Playwright goto waitUntil state, default networkidle
  -s, --selector <selector> Use a custom content selector
      --title <title>      Title for single URL input
      --converter <cmd>    html-to-markdown command path
`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main().catch((error) => {
    process.stderr.write(`${error.message}\n`);
    process.exitCode = 1;
  });
}
