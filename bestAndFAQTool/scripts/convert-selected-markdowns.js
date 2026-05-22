#!/usr/bin/env node
import { mkdir, readdir, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";

import {
  extractTargetSectionsFromMarkdown,
} from "../src/link-extractor.js";
import {
  outputDirNameForSection,
} from "../src/batch-web-to-md.js";
import { buildFailedLinksMarkdown } from "../src/failure-report.js";

const DEFAULT_INPUT_DIR = "/media/wxjshr/wxj/zxy/code/HarmonyOS-Kit-Skill";
const DEFAULT_OUT_DIR = "extracted-docs";
const EXCLUDED_FILES = new Set([
  "Ability Kit.md",
  "ArkUI.md",
  "Camera Kit.md",
  "Image Kit.md",
  "mdSkillgenerate.md",
]);

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const inputs = await findInputs(args.inputDir);
  const failures = [];
  const allManifest = [];

  await mkdir(args.out, { recursive: true });
  await writeFile(path.join(args.out, "failed-links.md"), buildFailedLinksMarkdown([]), "utf8");

  for (const inputPath of inputs) {
    const inputName = path.basename(inputPath);
    process.stderr.write(`\n=== ${inputName} ===\n`);

    const sections = await readTargetSections(inputPath);
    if (sections.length === 0) {
      failures.push({
        input: inputName,
        title: inputName,
        status: "failed",
        error: "未找到包含“最佳实践 / FAQ / 常见问题”的大类链接。",
      });
      await writeFailureReport(args.out, failures);
      continue;
    }

    for (const dirName of new Set(sections.map(outputDirNameForSection))) {
      await rm(path.join(args.out, dirName), { recursive: true, force: true });
    }

    const exitCode = await runBatch(inputPath, args);
    if (exitCode !== 0) {
      failures.push({
        input: inputName,
        title: inputName,
        status: "failed",
        error: `batch-web-to-md exited with ${exitCode}`,
      });
      await writeFailureReport(args.out, failures);
      continue;
    }

    const manifest = await readManifest(args.out);
    for (const entry of manifest) {
      const enriched = { ...entry, input: inputName };
      allManifest.push(enriched);
      if (entry.status === "failed") failures.push(enriched);
    }
    await writeFailureReport(args.out, failures);
  }

  await writeFile(
    path.join(args.out, "manifest-all.json"),
    `${JSON.stringify(allManifest, null, 2)}\n`,
    "utf8",
  );
  await writeFailureReport(args.out, failures);
}

async function findInputs(inputDir) {
  const entries = await readdir(inputDir, { withFileTypes: true });
  return entries
    .filter((entry) => entry.isFile())
    .map((entry) => entry.name)
    .filter((name) => /\.md$/i.test(name))
    .filter((name) => !EXCLUDED_FILES.has(name))
    .sort((a, b) => a.localeCompare(b, "en"))
    .map((name) => path.join(inputDir, name));
}

async function readTargetSections(inputPath) {
  const markdown = await readFile(inputPath, "utf8");
  return extractTargetSectionsFromMarkdown(markdown);
}

function runBatch(inputPath, args) {
  const scriptPath = fileURLToPath(new URL("../src/batch-web-to-md.js", import.meta.url));
  const childArgs = [
    scriptPath,
    inputPath,
    "--out",
    args.out,
    "--overwrite",
    "--wait-until",
    args.waitUntil,
    "--wait",
    String(args.wait),
  ];

  return new Promise((resolve) => {
    const child = spawn(process.execPath, childArgs, {
      stdio: "inherit",
    });
    child.on("close", resolve);
  });
}

async function readManifest(outDir) {
  try {
    return JSON.parse(await readFile(path.join(outDir, "manifest.json"), "utf8"));
  } catch {
    return [];
  }
}

async function writeFailureReport(outDir, failures) {
  await writeFile(
    path.join(outDir, "failed-links.md"),
    buildFailedLinksMarkdown(failures),
    "utf8",
  );
}

function parseArgs(argv) {
  const args = {
    inputDir: DEFAULT_INPUT_DIR,
    out: DEFAULT_OUT_DIR,
    waitUntil: "domcontentloaded",
    wait: 1000,
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--input-dir") {
      args.inputDir = readValue(argv, ++index, arg);
    } else if (arg === "--out") {
      args.out = readValue(argv, ++index, arg);
    } else if (arg === "--wait-until") {
      args.waitUntil = readValue(argv, ++index, arg);
    } else if (arg === "--wait") {
      args.wait = Number(readValue(argv, ++index, arg));
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
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

main().catch((error) => {
  process.stderr.write(`${error.message}\n`);
  process.exitCode = 1;
});
