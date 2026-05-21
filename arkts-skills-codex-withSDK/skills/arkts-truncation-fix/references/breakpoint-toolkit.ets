// 断点 + 安全区 + 折叠屏完整工具类
// 可直接复制到项目中使用

import window from '@ohos.window';
import display from '@ohos.display';
import { BusinessError } from '@kit.BasicServicesKit';

// ─────────────────────────────────────────
// 1. 断点常量
// ─────────────────────────────────────────

export class BreakpointConstants {
  static readonly BREAKPOINT_XS_VALUE: number = 320;
  static readonly BREAKPOINT_SM_VALUE: number = 600;
  static readonly BREAKPOINT_MD_VALUE: number = 840;
  static readonly BREAKPOINT_LG_VALUE: number = 1440;

  static readonly BREAKPOINT_XS: string = 'xs';
  static readonly BREAKPOINT_SM: string = 'sm';
  static readonly BREAKPOINT_MD: string = 'md';
  static readonly BREAKPOINT_LG: string = 'lg';
  static readonly BREAKPOINT_XL: string = 'xl';

  static readonly VERTICAL_BREAKPOINT_SM: number = 0.8;
  static readonly VERTICAL_BREAKPOINT_MD: number = 1.2;

  static readonly VERTICAL_SM: string = 'vertical_sm';
  static readonly VERTICAL_MD: string = 'vertical_md';
  static readonly VERTICAL_LG: string = 'vertical_lg';

  static readonly CURRENT_BREAKPOINT: string = 'currentBreakpoint';
  static readonly CURRENT_VERTICAL_BREAKPOINT: string = 'currentVerticalBreakpoint';
  static readonly WINDOW_WIDTH: string = 'windowWidth';
  static readonly WINDOW_HEIGHT: string = 'windowHeight';
  static readonly WINDOW_WIDTH_PX: string = 'windowWidthPx';
  static readonly SAFE_TOP_INSET: string = 'safeTopInset';
  static readonly SAFE_BOTTOM_INSET: string = 'safeBottomInset';
  static readonly KEYBOARD_INSET: string = 'keyboardInset';
  static readonly IS_FOLDABLE_DEVICE: string = 'isFoldableDevice';
  static readonly CURRENT_FOLD_STATUS: string = 'currentFoldStatus';
  static readonly CURRENT_FOLD_DISPLAY_MODE: string = 'currentFoldDisplayMode';
}

// ─────────────────────────────────────────
// 2. 按断点返回不同值的泛型工具
// ─────────────────────────────────────────

export class BreakpointType<T> {
  sm: T;
  md?: T;
  lg?: T;
  xl?: T;

  constructor(sm: T, md?: T, lg?: T, xl?: T) {
    this.sm = sm;
    this.md = md;
    this.lg = lg;
    this.xl = xl;
  }

  getValue(breakpoint: string): T {
    switch (breakpoint) {
      case 'xl':
        return this.xl ?? this.lg ?? this.md ?? this.sm;
      case 'lg':
        return this.lg ?? this.md ?? this.sm;
      case 'md':
        return this.md ?? this.sm;
      default:
        return this.sm;
    }
  }
}

// ─────────────────────────────────────────
// 3. 断点计算函数
// ─────────────────────────────────────────

export function getBreakpointByWidth(width: number): string {
  if (width < BreakpointConstants.BREAKPOINT_XS_VALUE) {
    return BreakpointConstants.BREAKPOINT_XS;
  } else if (width < BreakpointConstants.BREAKPOINT_SM_VALUE) {
    return BreakpointConstants.BREAKPOINT_SM;
  } else if (width < BreakpointConstants.BREAKPOINT_MD_VALUE) {
    return BreakpointConstants.BREAKPOINT_MD;
  } else if (width < BreakpointConstants.BREAKPOINT_LG_VALUE) {
    return BreakpointConstants.BREAKPOINT_LG;
  } else {
    return BreakpointConstants.BREAKPOINT_XL;
  }
}

export function getVerticalBreakpoint(width: number, height: number): string {
  const ratio = height / Math.max(width, 1);
  if (ratio < BreakpointConstants.VERTICAL_BREAKPOINT_SM) {
    return BreakpointConstants.VERTICAL_SM;
  } else if (ratio < BreakpointConstants.VERTICAL_BREAKPOINT_MD) {
    return BreakpointConstants.VERTICAL_MD;
  } else {
    return BreakpointConstants.VERTICAL_LG;
  }
}

export function isLargeBreakpoint(breakpoint: string): boolean {
  return breakpoint === BreakpointConstants.BREAKPOINT_LG ||
         breakpoint === BreakpointConstants.BREAKPOINT_XL;
}

export function getMaxContentWidth(breakpoint: string): number {
  if (breakpoint === BreakpointConstants.BREAKPOINT_XL) return 1280;
  if (breakpoint === BreakpointConstants.BREAKPOINT_LG) return 980;
  return 10000;
}

// ─────────────────────────────────────────
// 4. 综合窗口观察者（断点 + 安全区 + 折叠屏）
// ─────────────────────────────────────────

export class AdaptiveWindowObserver {
  private static currentWindow?: window.Window;
  private static initialized: boolean = false;

  private static readonly onWindowSizeChange: Callback<window.Size> = (size: window.Size): void => {
    AdaptiveWindowObserver.updateWindowMetrics(size.width, size.height);
  };

  private static readonly onAvoidAreaChange: Callback<window.AvoidAreaOptions> = (): void => {
    AdaptiveWindowObserver.updateAvoidAreas();
  };

  private static readonly onFoldStatusChange: Callback<number> = (status: number): void => {
    AdaptiveWindowObserver.setStorageValue(BreakpointConstants.CURRENT_FOLD_STATUS, status);
  };

  private static readonly onFoldDisplayModeChange: Callback<number> = (mode: number): void => {
    AdaptiveWindowObserver.setStorageValue(BreakpointConstants.CURRENT_FOLD_DISPLAY_MODE, mode);
  };

  static async init(context: Context): Promise<void> {
    if (AdaptiveWindowObserver.initialized) return;
    AdaptiveWindowObserver.initDefaults();
    try {
      const win = await window.getLastWindow(context);
      AdaptiveWindowObserver.bindWindow(win);
    } catch (error) {
      console.error('AdaptiveWindowObserver init failed:', JSON.stringify(error));
    }
  }

  static destroy(): void {
    if (!AdaptiveWindowObserver.currentWindow) return;
    AdaptiveWindowObserver.currentWindow.off('windowSizeChange', AdaptiveWindowObserver.onWindowSizeChange);
    AdaptiveWindowObserver.currentWindow.off('avoidAreaChange', AdaptiveWindowObserver.onAvoidAreaChange);
    try {
      display.off('foldStatusChange', AdaptiveWindowObserver.onFoldStatusChange);
      display.off('foldDisplayModeChange', AdaptiveWindowObserver.onFoldDisplayModeChange);
    } catch (_) {}
    AdaptiveWindowObserver.currentWindow = undefined;
    AdaptiveWindowObserver.initialized = false;
  }

  private static initDefaults(): void {
    AppStorage.setOrCreate(BreakpointConstants.CURRENT_BREAKPOINT, BreakpointConstants.BREAKPOINT_SM);
    AppStorage.setOrCreate(BreakpointConstants.CURRENT_VERTICAL_BREAKPOINT, BreakpointConstants.VERTICAL_LG);
    AppStorage.setOrCreate(BreakpointConstants.WINDOW_WIDTH, 0);
    AppStorage.setOrCreate(BreakpointConstants.WINDOW_HEIGHT, 0);
    AppStorage.setOrCreate(BreakpointConstants.WINDOW_WIDTH_PX, 0);
    AppStorage.setOrCreate(BreakpointConstants.SAFE_TOP_INSET, 0);
    AppStorage.setOrCreate(BreakpointConstants.SAFE_BOTTOM_INSET, 0);
    AppStorage.setOrCreate(BreakpointConstants.KEYBOARD_INSET, 0);
    AppStorage.setOrCreate(BreakpointConstants.IS_FOLDABLE_DEVICE, false);
    AppStorage.setOrCreate(BreakpointConstants.CURRENT_FOLD_STATUS, 0);
    AppStorage.setOrCreate(BreakpointConstants.CURRENT_FOLD_DISPLAY_MODE, 0);
  }

  private static updateWindowMetrics(widthPx: number, heightPx: number): void {
    const w = px2vp(widthPx);
    const h = px2vp(heightPx);
    AdaptiveWindowObserver.setStorageValue(BreakpointConstants.WINDOW_WIDTH, w);
    AdaptiveWindowObserver.setStorageValue(BreakpointConstants.WINDOW_HEIGHT, h);
    AdaptiveWindowObserver.setStorageValue(BreakpointConstants.WINDOW_WIDTH_PX, widthPx);
    AdaptiveWindowObserver.setStorageValue(BreakpointConstants.CURRENT_BREAKPOINT, getBreakpointByWidth(w));
    AdaptiveWindowObserver.setStorageValue(BreakpointConstants.CURRENT_VERTICAL_BREAKPOINT, getVerticalBreakpoint(w, h));
  }

  private static updateAvoidAreas(): void {
    if (!AdaptiveWindowObserver.currentWindow) return;
    try {
      const win = AdaptiveWindowObserver.currentWindow;
      const sysArea = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
      const cutArea = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_CUTOUT);
      const navArea = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
      const kbArea = win.getWindowAvoidArea(window.AvoidAreaType.TYPE_KEYBOARD);

      const safeTop = Math.max(sysArea.topRect.top + sysArea.topRect.height, cutArea.topRect.top + cutArea.topRect.height, 0);
      const safeBottom = Math.max(navArea.bottomRect.height, 0);
      const kbBottom = Math.max(kbArea.bottomRect.height, 0);

      AdaptiveWindowObserver.setStorageValue(BreakpointConstants.SAFE_TOP_INSET, px2vp(safeTop));
      AdaptiveWindowObserver.setStorageValue(BreakpointConstants.SAFE_BOTTOM_INSET, px2vp(safeBottom));
      AdaptiveWindowObserver.setStorageValue(BreakpointConstants.KEYBOARD_INSET, px2vp(kbBottom));
    } catch (error) {
      console.error('updateAvoidAreas failed:', JSON.stringify(error));
    }
  }

  private static updateFoldMetrics(): void {
    try {
      const foldable = display.isFoldable();
      if (foldable) {
        AdaptiveWindowObserver.setStorageValue(BreakpointConstants.IS_FOLDABLE_DEVICE, true);
        AdaptiveWindowObserver.setStorageValue(BreakpointConstants.CURRENT_FOLD_STATUS, display.getFoldStatus() as number);
        AdaptiveWindowObserver.setStorageValue(BreakpointConstants.CURRENT_FOLD_DISPLAY_MODE, display.getFoldDisplayMode() as number);
      }
    } catch (_) {}
  }

  private static setStorageValue(key: string, value: number | string | boolean): void {
    if (!AppStorage.set(key, value)) {
      AppStorage.setOrCreate(key, value);
    }
  }

  private static bindWindow(win: window.Window): void {
    AdaptiveWindowObserver.currentWindow = win;
    const props = win.getWindowProperties();
    AdaptiveWindowObserver.updateWindowMetrics(props.windowRect.width, props.windowRect.height);
    AdaptiveWindowObserver.updateAvoidAreas();
    AdaptiveWindowObserver.updateFoldMetrics();
    win.on('windowSizeChange', AdaptiveWindowObserver.onWindowSizeChange);
    win.on('avoidAreaChange', AdaptiveWindowObserver.onAvoidAreaChange);
    try {
      display.on('foldStatusChange', AdaptiveWindowObserver.onFoldStatusChange);
      display.on('foldDisplayModeChange', AdaptiveWindowObserver.onFoldDisplayModeChange);
    } catch (_) {}
    AdaptiveWindowObserver.initialized = true;
  }
}
