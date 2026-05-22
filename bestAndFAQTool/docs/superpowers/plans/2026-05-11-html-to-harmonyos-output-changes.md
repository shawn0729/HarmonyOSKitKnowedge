# HTML to HarmonyOS Output Changes Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Store remote images under a shared `assets/` directory, remove source-link headers from generated Markdown, and group batch output by Kit Chinese name.

**Architecture:** Add a small asset-localization module that rewrites HTML image URLs before Markdown conversion. Keep batch orchestration in `src/batch-web-to-md.js`, and keep navigation/title parsing in `src/link-extractor.js`.

**Tech Stack:** Node.js ESM, `node:test`, `jsdom`, Playwright, external `html-to-markdown` CLI.

---

### Task 1: Image Asset Localization

**Files:**
- Create: `src/asset-localizer.js`
- Test: `test/asset-localizer.test.js`
- Modify: `src/batch-web-to-md.js`

- [ ] Write failing tests for downloading HTTP images into `assets/` and rewriting HTML image references to paths relative to the Markdown file.
- [ ] Run `npm test -- test/asset-localizer.test.js` and confirm the new tests fail because the module is missing.
- [ ] Implement `localizeHtmlImageAssets(html, options)` with injectable fetch behavior for tests.
- [ ] Wire `convertLink()` so batch conversion localizes images before calling `convertHtmlToMarkdown()`.

### Task 2: Markdown Header and Kit Directory Names

**Files:**
- Modify: `src/batch-web-to-md.js`
- Modify: `src/link-extractor.js`
- Test: `test/batch-web-to-md.test.js`
- Test: `test/link-extractor.test.js`

- [ ] Write failing tests for Markdown content without `原文链接` and section directory names like `图片处理服务`.
- [ ] Run targeted tests and confirm they fail under current implementation.
- [ ] Add `kitChineseName` extraction from titles like `Image Kit（图片处理服务）`.
- [ ] Use the extracted Chinese name for navigation batch section output directory; fall back to the existing slug when absent.
- [ ] Remove the source-link header and separator from generated Markdown.

### Task 3: Verification and Docs

**Files:**
- Modify: `README.md`

- [ ] Update README output examples and behavior notes.
- [ ] Run `npm test`.
- [ ] Since this directory is not a Git repository, skip commit steps and report that explicitly.
