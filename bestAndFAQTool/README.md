# Web to Markdown

这是一个把网页正文转换为 Markdown 的 Node.js 工具。它使用 Playwright 打开并渲染页面，用 `jsdom` 清理正文 HTML，再调用 Rust 版 `html-to-markdown` CLI 生成 Markdown。

项目包含两个命令：

- `web-to-md`：转换单个网页，可输出到 stdout 或指定文件。
- `batch-web-to-md`：批量转换导航 Markdown 中的目标链接，或把单个 URL 写入结构化输出目录。

## 功能

- 渲染需要浏览器环境的网页内容。
- 自动识别正文区域，默认优先匹配 `article`、`main`、`.doc-content` 等选择器。
- 移除导航、页脚、广告、侧栏、表单、隐藏元素和常见代码工具栏文本。
- 自动把页面内相对链接、图片、音视频地址转换为绝对 URL。
- 批量转换时下载在线图片到输出根目录的 `assets/`，并在 Markdown 中写入相对路径。
- 支持通过 CSS selector 指定正文容器。
- 支持从导航 Markdown 中提取包含“最佳实践 / FAQ / 常见问题”的章节链接并批量转换。
- 批量输出时生成 `manifest.json`，记录每个链接的转换状态和输出路径。

## 环境要求

- Node.js 18 或更高版本。
- npm。
- Rust/Cargo，用于安装 `html-to-markdown-cli`。
- Playwright Chromium 浏览器。

## 安装

```bash
cargo install html-to-markdown-cli
npm install
npx playwright install chromium
```

确认转换器命令可用：

```bash
html-to-markdown --version
```

如果 `html-to-markdown` 不在 `PATH` 中，可以在运行命令时使用 `--converter <command>` 指定完整路径。

## 单页转换

打印 Markdown 到 stdout：

```bash
node src/web-to-md.js "https://example.com/docs/page"
```

写入文件：

```bash
node src/web-to-md.js "https://example.com/docs/page" --out output.md
```

指定正文选择器：

```bash
node src/web-to-md.js "https://example.com/docs/page" --selector ".doc-content"
```

禁用 `html-to-markdown` 预处理：

```bash
node src/web-to-md.js "https://example.com/docs/page" --no-preprocess
```

### `web-to-md` 参数

| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| `-o, --out <file>` | 写入 Markdown 文件；不传则输出到 stdout | 无 |
| `-s, --selector <selector>` | 指定正文容器 CSS selector | 自动识别 |
| `--wait <ms>` | 页面加载后额外等待时间 | `3000` |
| `--timeout <ms>` | `page.goto` 超时时间 | `60000` |
| `--wait-until <state>` | Playwright `goto` 的 `waitUntil` 状态 | `networkidle` |
| `--preset <level>` | `html-to-markdown --preprocess` preset | `aggressive` |
| `--no-preprocess` | 禁用 `html-to-markdown` 内置预处理 | 启用预处理 |
| `--converter <command>` | 指定 `html-to-markdown` 命令路径 | `html-to-markdown` |

## 批量转换

`batch-web-to-md` 支持两种输入：

- 一个 HTTP/HTTPS URL。
- 一个导航 Markdown 文件。

### 转换单个 URL 到输出目录

```bash
node src/batch-web-to-md.js "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-5" \
  --out extracted-docs \
  --title "如何自定义Tabs页签导航栏及其对齐方式"
```

输出示例：

```text
extracted-docs/
├── 0001-如何自定义Tabs页签导航栏及其对齐方式-faqs-arkui-5.md
└── manifest.json
```

### 从导航 Markdown 批量转换

```bash
node src/batch-web-to-md.js tabs.md --out extracted-docs --overwrite
```

导航 Markdown 中，标题包含“最佳实践 / FAQ / 常见问题”的章节会被视为目标章节；这些章节下的 HTTP/HTTPS 链接会被提取并转换。

示例输入：

```markdown
# 3 Image Kit（图片处理服务）最佳实践：

### 3.1.1 图片合成视频开发实践:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image-to-video-synthesis
### 3.1.2 图片获取与保存实践:https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-image_get_and_save

# 9 ArkUI Kit（方舟UI框架）FAQ

## 9.1 如何自定义Tabs页签导航栏:https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-5
```

输出示例：

```text
extracted-docs/
├── 图片处理服务/
│   ├── 最佳实践-综合/
│   │   ├── 0001-图片合成视频开发实践-bpta-image-to-video-synthesis.md
│   │   └── 0002-图片获取与保存实践-bpta-image_get_and_save.md
│   └── assets/
│       └── 0001-图片合成视频开发实践-bpta-image-to-video-synthesis-image-001.png
├── 方舟UI框架/
│   └── FAQ-综合/
│       └── 0001-如何自定义Tabs页签导航栏-faqs-arkui-5.md
└── manifest.json
```

每个生成的 Markdown 文件包含文档标题和清理并转换后的正文 Markdown，不再写入原文链接。导航批量模式下，同一 Kit 下会按章节生成并列目录，例如 `最佳实践-程序包结构`、`最佳实践-程序框架`、`FAQ-程序包结构`、`FAQ-程序框架`。在线图片会下载到 Kit 目录下与这些章节目录同级的 `assets/`，文档内引用会改写成从当前 Markdown 文件出发的相对路径。

导航批量模式下，如果导航文件顶部或目标章节标题包含 Kit 中文名，例如 `Image Kit（图片处理服务）`，输出目录会命名为 `图片处理服务`；如果无法提取中文名，则沿用原章节标题生成的安全目录名。

导航批量模式下，`manifest.json` 会记录 `section`、`title`、`url`、`output`、`status`，失败项还会包含 `error`。单 URL 模式下，`manifest.json` 记录 `title`、`url` 和 `output`。

### `batch-web-to-md` 参数

| 参数 | 说明 | 默认值 |
| --- | --- | --- |
| `-o, --out <dir>` | 输出目录 | `extracted-docs` |
| `--limit <n>` | 最多转换 n 个链接，便于试跑 | 无限制 |
| `--overwrite` | 覆盖已存在的输出文件 | 不覆盖 |
| `--wait <ms>` | 页面加载后额外等待时间 | `3000` |
| `--timeout <ms>` | `page.goto` 超时时间 | `60000` |
| `--wait-until <state>` | Playwright `goto` 的 `waitUntil` 状态 | `networkidle` |
| `-s, --selector <selector>` | 指定正文容器 CSS selector | 自动识别 |
| `--title <title>` | 单 URL 输入时指定输出文档标题 | 页面标题或 URL slug |
| `--converter <cmd>` | 指定 `html-to-markdown` 命令路径 | `html-to-markdown` |

## 实用命令

试跑前 3 个链接：

```bash
node src/batch-web-to-md.js tabs.md --out extracted-docs-test --limit 3 --overwrite
```

页面内容加载较慢时增加等待时间：

```bash
node src/web-to-md.js "https://example.com/docs/page" --wait 8000
```

页面一直等不到 `networkidle` 时改用 `domcontentloaded`：

```bash
node src/web-to-md.js "https://example.com/docs/page" --wait-until domcontentloaded --wait 3000
```

指定转换器完整路径：

```bash
node src/web-to-md.js "https://example.com/docs/page" --converter "$HOME/.cargo/bin/html-to-markdown"
```

## 测试

```bash
npm test
```

当前测试覆盖：

- 导航 Markdown 中目标章节的链接提取。
- 重复链接去重。
- 输出文件名清理与排序编号。
- 单 URL 批量输入结构。
- 华为 HarmonyOS 文档标题后缀清理。

## 常见问题

### 找不到 `html-to-markdown`

先确认命令是否在 `PATH` 中：

```bash
html-to-markdown --version
```

如果不可用，重新安装：

```bash
cargo install html-to-markdown-cli
```

或者通过 `--converter` 指定二进制路径。

### 输出内容不完整

优先尝试指定正文选择器：

```bash
node src/web-to-md.js "https://example.com/docs/page" --selector ".doc-content"
```

如果页面由脚本延迟渲染，可以增加 `--wait`。

### 批量转换提示文件已存在

默认不会覆盖已有文件。确认需要重跑时添加：

```bash
node src/batch-web-to-md.js tabs.md --out extracted-docs --overwrite
```
