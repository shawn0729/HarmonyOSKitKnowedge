#!/usr/bin/env node
import { spawn } from "node:child_process";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { JSDOM } from "jsdom";
import { chromium } from "playwright";

import { cleanDocumentHtml } from "./html-cleaner.js";

const DEFAULT_WAIT_MS = 3000;
const DEFAULT_TIMEOUT_MS = 60000;

export async function main() {
  const args = parseArgs(process.argv.slice(2));

  if (!args.url) {
    printUsage();
    process.exitCode = 1;
    return;
  }

  const html = await fetchCleanHtml(args);
  const markdown = await convertHtmlToMarkdown(html, {
    command: args.converter,
    preprocess: args.preprocess,
    preset: args.preset,
  });

  if (args.out) {
    await mkdir(path.dirname(path.resolve(args.out)), { recursive: true });
    await writeFile(args.out, markdown, "utf8");
    return;
  }

  process.stdout.write(markdown);
}

export async function fetchCleanPage(args) {
  const browser = await chromium.launch({ headless: true });

  try {
    const page = await browser.newPage({
      userAgent:
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 " +
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    });

    await page.goto(args.url, {
      waitUntil: args.waitUntil,
      timeout: args.timeout,
    });

    if (args.wait > 0) {
      await page.waitForTimeout(args.wait);
    }

    const renderedHtml = await page.content();
    const dom = new JSDOM(renderedHtml, { url: page.url() });
    return {
      html: cleanDocumentHtml(dom.window.document, { selector: args.selector }),
      title: (await page.title()).trim(),
      url: page.url(),
    };
  } finally {
    await browser.close();
  }
}

export async function fetchCleanHtml(args) {
  const page = await fetchCleanPage(args);
  return page.html;
}

export async function convertHtmlToMarkdown(html, options = {}) {
  const command = options.command || "html-to-markdown";
  const args = ["-"];

  if (options.preprocess) {
    args.push("--preprocess", "--preset", options.preset || "standard");
  }

  return await runCommand(command, args, html);
}

export function runCommand(command, args, input) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, {
      stdio: ["pipe", "pipe", "pipe"],
    });

    let stdout = "";
    let stderr = "";

    child.stdout.setEncoding("utf8");
    child.stderr.setEncoding("utf8");
    child.stdout.on("data", (chunk) => {
      stdout += chunk;
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk;
    });
    child.on("error", reject);
    child.on("close", (code) => {
      if (code === 0) {
        resolve(stdout);
        return;
      }

      reject(new Error(`${command} exited with ${code}: ${stderr.trim()}`));
    });

    child.stdin.end(input);
  });
}

export function parseArgs(argv) {
  const args = {
    wait: DEFAULT_WAIT_MS,
    timeout: DEFAULT_TIMEOUT_MS,
    waitUntil: "networkidle",
    preprocess: true,
    preset: "aggressive",
    converter: "html-to-markdown",
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];

    if (arg === "--out" || arg === "-o") {
      args.out = readValue(argv, ++index, arg);
    } else if (arg === "--selector" || arg === "-s") {
      args.selector = readValue(argv, ++index, arg);
    } else if (arg === "--wait") {
      args.wait = Number(readValue(argv, ++index, arg));
    } else if (arg === "--timeout") {
      args.timeout = Number(readValue(argv, ++index, arg));
    } else if (arg === "--wait-until") {
      args.waitUntil = readValue(argv, ++index, arg);
    } else if (arg === "--preset") {
      args.preset = readValue(argv, ++index, arg);
    } else if (arg === "--converter") {
      args.converter = readValue(argv, ++index, arg);
    } else if (arg === "--no-preprocess") {
      args.preprocess = false;
    } else if (arg === "--help" || arg === "-h") {
      args.help = true;
    } else if (!args.url) {
      args.url = arg;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  if (args.help) {
    printUsage();
    process.exit(0);
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

function printUsage() {
  process.stderr.write(`Usage: web-to-md <url> [options]

Options:
  -o, --out <file>          Write Markdown to a file instead of stdout
  -s, --selector <selector> Use a custom content selector
      --wait <ms>           Extra wait after network idle, default ${DEFAULT_WAIT_MS}
      --timeout <ms>        Page load timeout, default ${DEFAULT_TIMEOUT_MS}
      --wait-until <state>  Playwright goto waitUntil state, default networkidle
      --preset <level>      html-to-markdown preprocess preset, default aggressive
      --no-preprocess       Disable html-to-markdown built-in preprocessing
      --converter <command> html-to-markdown command path, default html-to-markdown
`);
}

if (process.argv[1] === fileURLToPath(import.meta.url)) {
  main().catch((error) => {
    process.stderr.write(`${error.message}\n`);
    process.exitCode = 1;
  });
}
