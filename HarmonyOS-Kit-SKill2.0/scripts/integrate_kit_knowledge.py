#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "harmonyos-development"
SOURCES_ROOT = SKILL_ROOT / "sources"
REFERENCES_ROOT = SKILL_ROOT / "references"
ASSETS_ROOT = SOURCES_ROOT / "_assets" / "images"


@dataclass(frozen=True)
class Domain:
    source_dir: str
    slug: str
    label: str


NEW_MEDIA_SOURCE_DIR = "/media/wxjshr/wxj/zxy/code/bestAndFAQTool/extracted-docs/Media-Kit（媒体服务）"
OBSOLETE_DOMAIN_SLUGS = {"audio-development"}


@dataclass(frozen=True)
class RouteSection:
    slug: str
    label: str
    keywords: tuple[str, ...]


DOMAINS = [
    Domain("Account-Kit（华为账号服务）", "account-authentication", "账号与登录"),
    Domain("Ads-Kit（广告服务）", "ads-monetization", "广告与流量变现"),
    Domain("AppGallery-Kit（应用市场服务）", "appgallery-services", "应用市场服务"),
    Domain("Ability-Kit（程序框架服务）", "ability-framework", "Ability/程序框架"),
    Domain("ArkData（方舟数据管理）", "data-management", "数据管理"),
    Domain("ArkTS（方舟编程语言）", "arkts-language", "ArkTS 编程语言"),
    Domain("ArkUI Kit", "arkui-development", "ArkUI 开发"),
    Domain("ArkWeb（方舟Web）", "web-development", "Web 开发"),
    Domain("Background-Tasks-Kit（后台任务开发服务）", "background-tasks", "后台任务"),
    Domain("Basic-Services-Kit（基础服务）", "basic-services", "基础服务"),
    Domain("Camera Kit", "camera-development", "相机开发"),
    Domain("Core-File-Kit（文件基础服务）", "file-management", "文件管理"),
    Domain("Crypto-Architecture-Kit（加解密算法框架服务）", "crypto-architecture", "加解密算法框架"),
    Domain("Form-Kit（卡片开发服务）", "form-development", "卡片开发"),
    Domain("IAP-Kit（应用内支付服务）", "in-app-purchases", "应用内支付"),
    Domain("Image Kit", "image-processing", "图片处理"),
    Domain(NEW_MEDIA_SOURCE_DIR, "media-development", "媒体开发（音频和视频）"),
    Domain("Media-Library-Kit（媒体文件管理服务）", "media-library", "媒体文件管理"),
    Domain("Network-Kit（网络服务）", "network-development", "网络开发"),
    Domain("Notification-Kit（用户通知服务）", "notification-development", "用户通知"),
    Domain("Performance-Analysis-Kit", "performance-analysis", "性能分析"),
    Domain("Scan-Kit（统一扫码服务）", "scan-code", "扫码服务"),
    Domain("Sensor-Service-Kit（传感器服务）", "sensor-service", "传感器服务"),
    Domain("Share-Kit（分享服务）", "share-service", "分享服务"),
    Domain("Telephony-Kit（蜂窝通信服务）", "telephony-service", "蜂窝通信"),
]


MARKDOWN_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\n]+)\)")
HTML_IMG_RE = re.compile(r'(<img\b[^>]*?\bsrc=["\'])([^"\']+)(["\'][^>]*>)', re.IGNORECASE)
REMOTE_RE = re.compile(r"^[a-z][a-z0-9+.-]*://", re.IGNORECASE)
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".svg"}
STRIP_ORIGINAL_LINK_DOMAINS = {"arkui-development", "camera-development", "image-processing"}
ORIGINAL_LINK_RE = re.compile(r"^原文链接[:：].*$\n?", re.MULTILINE)
TITLE_SEPARATOR_SPACING_RE = re.compile(r"(\A# [^\n]+\n)\n{2,}(---\n)", re.MULTILINE)


SPLIT_ROUTE_SECTIONS: dict[tuple[str, str], tuple[RouteSection, ...]] = {
    ("arkui-development", "faq"): (
        RouteSection("tabs-navigation", "Tabs 与导航", ("Tabs", "Tab", "tab", "页签", "导航", "Navigation", "Router", "路由")),
        RouteSection("list-scroll-grid", "列表、滚动与网格", ("List", "Scroll", "Scroller", "Grid", "Swiper", "WaterFlow", "滚动", "列表", "网格", "滑动", "懒加载")),
        RouteSection("gesture-event", "手势与事件", ("Gesture", "手势", "点击", "拖拽", "滑动事件", "事件", "Touch", "onClick", "onTouch", "键鼠")),
        RouteSection("keyboard-input-focus", "键盘、输入与焦点", ("TextInput", "TextArea", "Search", "输入", "键盘", "焦点", "Focus", "光标", "输入框")),
        RouteSection("dialog-window-system", "弹窗、窗口与系统能力", ("弹窗", "Dialog", "窗口", "Window", "安全区", "状态栏", "导航栏", "沉浸式", "全屏", "菜单", "菜单栏")),
        RouteSection("layout-style", "布局与样式", ("布局", "样式", "宽高", "尺寸", "位置", "居中", "对齐", "边距", "圆角", "阴影", "颜色", "背景", "适配", "Flex", "Column", "Row", "RelativeContainer", "Blank")),
        RouteSection("image-text-rich", "图片、文本与富文本", ("Image", "图片", "Text", "文本", "字体", "Span", "富文本", "WebView", "像素", "图标")),
        RouteSection("component-state", "组件状态与刷新", ("组件", "状态", "刷新", "ForEach", "LazyForEach", "@State", "@Link", "@Prop", "@Builder", "生命周期", "渲染", "复用")),
        RouteSection("animation-canvas-web", "动画、Canvas 与 Web", ("动画", "转场", "animate", "Canvas", "Web", "Video", "XComponent")),
        RouteSection("other", "其他问题", ()),
    ),
    ("arkts-language", "faq"): (
        RouteSection("concurrency-threading", "线程与并发", ("线程", "多线程", "并发", "Worker", "TaskPool", "Sendable", "共享内存", "主线程", "子线程", "优先级", "await", "异步", "I/O", "IO", "synchronized")),
        RouteSection("napi-native-aop", "NAPI、Native 与 AOP", ("NAPI", "napi", "C++", "pthread", "libstd", "AOP", "插桩", "替换")),
        RouteSection("types-collections-json", "类型、对象、集合与 JSON", ("JSON", "对象", "类型", "Array", "ArrayBuffer", "String", "Uint8Array", "Map", "HashMap", "Record", "UUID", "uuid", "base64", "正则", "解构", "深拷贝", "浅拷贝", "序列化", "反序列化", "number", "大整数", "key", "类名")),
        RouteSection("module-build-runtime", "模块、编译与运行时", ("模块", "编译", ".abc", "AOT", "ap、an、ai", "HAR", "HSP", "SO", "动态加载", "import", "globalThis", "js引擎", "JIT", "AST", "混淆", "环境变量", "CPU", "rawfile", ".ets", ".ts", "后缀")),
        RouteSection("language-oop-functions", "语言特性、类与函数", ("类", "方法", "静态", "重载", "继承", "反射", "注解", "装饰器", "闭包", "callback", "this", "接口", "匿名内部类", "setter", "getter")),
        RouteSection("other", "其他问题", ()),
    ),
    ("ability-framework", "faq"): (
        RouteSection("ability-lifecycle-context", "Ability、生命周期与 Context", ("Ability", "UIAbility", "Extension", "AbilityStage", "Context", "UIContext", "生命周期", "进程", "前台", "后台", "启动", "退出", "跳转", "拉起", "页面", "EventHub", "emitter", "屏幕", "窗口", "权限")),
        RouteSection("package-module", "程序包、模块与安装", ("HAP", "HAR", "HSP", "App", "Bundle", "包", "模块", "安装", "卸载", "打包", "证书", "签名", "依赖", "SharedLibrary", "rawfile", "资源", "快捷方式", "Debug", "Release", "bundle", "hap")),
        RouteSection("background-form-ipc", "后台任务、卡片与 IPC", ("后台任务", "后台", "WorkScheduler", "长时任务", "短时任务", "延迟任务", "卡片", "Form", "IPC", "跨进程")),
        RouteSection("other", "其他问题", ()),
    ),
}


def doc_kind(domain: Domain, path: Path) -> str | None:
    parts = path.parts
    if any("最佳实践" in part for part in parts):
        return "best-practices"
    if any("FAQ" in part for part in parts):
        return "faq"
    if domain.slug == "arkui-development":
        return "best-practices"
    return None


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def copy_asset(source: Path) -> str:
    data = source.read_bytes()
    digest = hashlib.sha256(data).hexdigest()[:24]
    suffix = source.suffix.lower()
    dest = ASSETS_ROOT / f"{digest}{suffix}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        dest.write_bytes(data)
    return dest.name


def split_markdown_target(raw: str) -> tuple[str, str]:
    stripped = raw.strip()
    if stripped.startswith("<") and ">" in stripped:
        end = stripped.find(">")
        return stripped[1:end], stripped[end + 1 :]
    if " " not in stripped and "\t" not in stripped:
        return stripped, ""
    target, suffix = stripped.split(None, 1)
    return target, " " + suffix


def rewrite_markdown_images(text: str, src_file: Path, dest_file: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        alt, raw_target = match.group(1), match.group(2)
        target, suffix = split_markdown_target(raw_target)
        if REMOTE_RE.match(target) or target.startswith("#"):
            return match.group(0)
        asset = (src_file.parent / target).resolve()
        if not asset.exists() or asset.suffix.lower() not in IMAGE_SUFFIXES:
            return match.group(0)
        asset_name = copy_asset(asset)
        rel = Path(os.path.relpath(ASSETS_ROOT / asset_name, dest_file.parent)).as_posix()
        return f"![{alt}]({rel}{suffix})"

    return MARKDOWN_IMAGE_RE.sub(replace, text)


def rewrite_html_images(text: str, src_file: Path, dest_file: Path) -> str:
    def replace(match: re.Match[str]) -> str:
        prefix, target, suffix = match.group(1), match.group(2), match.group(3)
        if REMOTE_RE.match(target) or target.startswith("#"):
            return match.group(0)
        asset = (src_file.parent / target).resolve()
        if not asset.exists() or asset.suffix.lower() not in IMAGE_SUFFIXES:
            return match.group(0)
        asset_name = copy_asset(asset)
        rel = Path(os.path.relpath(ASSETS_ROOT / asset_name, dest_file.parent)).as_posix()
        return f"{prefix}{rel}{suffix}"

    return HTML_IMG_RE.sub(replace, text)


def strip_original_links(domain: Domain, text: str) -> str:
    if domain.slug not in STRIP_ORIGINAL_LINK_DOMAINS:
        return text
    text = ORIGINAL_LINK_RE.sub("", text)
    return TITLE_SEPARATOR_SPACING_RE.sub(r"\1\n\2", text, count=1)


def materialize_domain(domain: Domain) -> dict[str, list[tuple[str, Path]]]:
    source_root = Path(domain.source_dir)
    if not source_root.is_absolute():
        source_root = ROOT / source_root
    routes: dict[str, list[tuple[str, Path]]] = {"best-practices": [], "faq": []}
    if not source_root.exists():
        raise FileNotFoundError(source_root)

    for src_file in sorted(source_root.rglob("*.md")):
        kind = doc_kind(domain, src_file.relative_to(source_root))
        if kind is None:
            continue
        dest_dir = SOURCES_ROOT / domain.slug / kind
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_file = dest_dir / src_file.name
        text = src_file.read_text(encoding="utf-8")
        text = strip_original_links(domain, text)
        text = rewrite_markdown_images(text, src_file, dest_file)
        text = rewrite_html_images(text, src_file, dest_file)
        dest_file.write_text(text, encoding="utf-8")
        routes[kind].append((first_heading(dest_file), dest_file.relative_to(SKILL_ROOT)))

    return routes


def kind_label(kind: str) -> str:
    if kind.startswith("best-practices"):
        suffix = kind.removeprefix("best-practices")
        return f"最佳实践{suffix}"
    if kind.startswith("faq"):
        suffix = kind.removeprefix("faq")
        return f"FAQ{suffix}"
    return "最佳实践" if kind == "best-practices" else "FAQ"


def route_lines(domain: Domain, kind: str, entries: list[tuple[str, Path]]) -> list[str]:
    lines = [
        f"# {domain.label} {kind_label(kind)} 标题路由",
        "",
        "本文件只使用 Markdown 一级标题作为路由关键词。命中后必须读取对应 sources/ 原文。",
        "",
    ]
    for title, source_path in entries:
        lines.append(f"- 关键词：{title}")
        lines.append(f"  - 读取：{source_path.as_posix()}")
    return lines


def pick_section(title: str, sections: tuple[RouteSection, ...]) -> RouteSection:
    fallback = sections[-1]
    for section in sections:
        if not section.keywords:
            fallback = section
            continue
        if any(keyword in title for keyword in section.keywords):
            return section
    return fallback


def write_split_routing_file(domain: Domain, kind: str, entries: list[tuple[str, Path]], sections: tuple[RouteSection, ...]) -> int:
    ref_dir = REFERENCES_ROOT / domain.slug
    child_dir = ref_dir / kind
    child_dir.mkdir(parents=True, exist_ok=True)

    buckets: dict[str, list[tuple[str, Path]]] = {section.slug: [] for section in sections}
    for entry in entries:
        section = pick_section(entry[0], sections)
        buckets[section.slug].append(entry)

    written_sections = [section for section in sections if buckets[section.slug]]
    lines = [
        f"# {domain.label} {kind_label(kind)} 标题路由",
        "",
        "本文件是子路由入口。先按主题读取子路由；子路由仍只使用 Markdown 一级标题作为路由关键词。",
        "",
    ]
    for section in written_sections:
        child_path = f"{kind}/{section.slug}-routing.md"
        lines.append(f"- 主题：{section.label}")
        lines.append(f"  - 读取：{child_path}")
    (ref_dir / f"{kind}-routing.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    for section in written_sections:
        child_path = child_dir / f"{section.slug}-routing.md"
        child_lines = route_lines(domain, f"{kind}（{section.label}）", buckets[section.slug])
        child_path.write_text("\n".join(child_lines) + "\n", encoding="utf-8")

    return 1 + len(written_sections)


def write_routing_file(domain: Domain, kind: str, entries: list[tuple[str, Path]]) -> int:
    if not entries:
        return 0
    split_sections = SPLIT_ROUTE_SECTIONS.get((domain.slug, kind))
    if split_sections is not None:
        return write_split_routing_file(domain, kind, entries, split_sections)

    ref_dir = REFERENCES_ROOT / domain.slug
    ref_dir.mkdir(parents=True, exist_ok=True)
    path = ref_dir / f"{kind}-routing.md"
    lines = route_lines(domain, kind, entries)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 1


def main() -> None:
    total_docs = 0
    total_routes = 0
    for slug in OBSOLETE_DOMAIN_SLUGS:
        shutil.rmtree(SOURCES_ROOT / slug, ignore_errors=True)
        shutil.rmtree(REFERENCES_ROOT / slug, ignore_errors=True)
    for domain in DOMAINS:
        shutil.rmtree(SOURCES_ROOT / domain.slug, ignore_errors=True)
        shutil.rmtree(REFERENCES_ROOT / domain.slug, ignore_errors=True)
        routes = materialize_domain(domain)
        domain_docs = sum(len(entries) for entries in routes.values())
        total_docs += domain_docs
        for kind, entries in routes.items():
            total_routes += write_routing_file(domain, kind, entries)
        print(f"{domain.slug}: {domain_docs}")
    print(f"docs={total_docs} route_files={total_routes}")


if __name__ == "__main__":
    main()
