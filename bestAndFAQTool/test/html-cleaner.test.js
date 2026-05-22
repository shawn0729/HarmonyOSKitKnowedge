import assert from "node:assert/strict";
import test from "node:test";
import { JSDOM } from "jsdom";

import { cleanDocumentHtml } from "../src/html-cleaner.js";

test("keeps main article content and removes page chrome", () => {
  const dom = new JSDOM(
    `<!doctype html>
    <html>
      <body>
        <header>Site header</header>
        <nav>Navigation</nav>
        <main>
          <article>
            <h1>Title</h1>
            <p>Useful <a href="/docs/page">content</a>.</p>
            <img src="/images/a.png" alt="diagram">
            <aside>Related posts</aside>
            <div class="ad-banner">Advertisement</div>
            <script>window.noise = true</script>
          </article>
        </main>
        <footer>Footer</footer>
      </body>
    </html>`,
    { url: "https://example.com/base/" },
  );

  const html = cleanDocumentHtml(dom.window.document);

  assert.match(html, /<h1>Title<\/h1>/);
  assert.match(html, /Useful/);
  assert.match(html, /href="https:\/\/example.com\/docs\/page"/);
  assert.match(html, /src="https:\/\/example.com\/images\/a.png"/);
  assert.doesNotMatch(html, /Site header|Navigation|Footer|Advertisement|Related posts/);
  assert.doesNotMatch(html, /<script/);
});

test("falls back to the largest content-like block", () => {
  const dom = new JSDOM(
    `<!doctype html>
    <html>
      <body>
        <div class="menu">Menu</div>
        <section class="post-body">
          <h2>Fallback body</h2>
          <p>This block is the article content.</p>
        </section>
      </body>
    </html>`,
    { url: "https://example.com/" },
  );

  const html = cleanDocumentHtml(dom.window.document);

  assert.match(html, /Fallback body/);
  assert.doesNotMatch(html, /Menu/);
});

test("keeps relative urls when the document base cannot resolve them", () => {
  const dom = new JSDOM(
    `<!doctype html>
    <html>
      <body>
        <main><p><a href="/relative">Relative link</a></p></main>
      </body>
    </html>`,
    { url: "data:text/html,<main></main>" },
  );

  const html = cleanDocumentHtml(dom.window.document);

  assert.match(html, /href="\/relative"/);
});

test("removes Huawei code block toolbar labels while keeping code", () => {
  const dom = new JSDOM(
    `<!doctype html>
    <html>
      <body>
        <main>
          <p>具体操作可参考代码：</p>
          <div class="code-block">
            <div class="toolbar">
              <span>收起</span>
              <span>自动换行</span>
              <span>深色代码主题</span>
              <span>复制</span>
            </div>
            <pre><code>Text('content')</code></pre>
          </div>
        </main>
      </body>
    </html>`,
    { url: "https://developer.huawei.com/" },
  );

  const html = cleanDocumentHtml(dom.window.document);

  assert.match(html, /具体操作可参考代码/);
  assert.match(html, /Text\('content'\)/);
  assert.doesNotMatch(html, /收起|自动换行|深色代码主题|复制/);
});
