export function buildFailedLinksMarkdown(failures) {
  const entries = failures.filter((failure) => failure.status === "failed");
  const lines = ["# 转换失败链接", ""];

  if (entries.length === 0) {
    lines.push("无失败链接。", "");
    return lines.join("\n");
  }

  let currentInput = null;
  for (const failure of entries) {
    if (failure.input !== currentInput) {
      currentInput = failure.input;
      lines.push(`## ${currentInput}`, "");
    }

    lines.push(`- 标题：${failure.title || "未命名"}`);
    if (failure.section) lines.push(`  - 章节：${failure.section}`);
    if (failure.url) lines.push(`  - 链接：${failure.url}`);
    lines.push(`  - 错误：${failure.error || "未知错误"}`);
    lines.push("");
  }

  return lines.join("\n");
}
