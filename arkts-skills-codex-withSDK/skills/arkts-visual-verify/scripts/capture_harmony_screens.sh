#!/bin/bash
# capture_harmony_screens.sh
# 按功能粒度在 HarmonyOS 模拟器上逐功能导航并截图
#
# 用法:
#   bash capture_harmony_screens.sh \
#     --bundle com.example.app \
#     --module entry \
#     --features spec/visual-verify/feature_screenshot_list.json \
#     --output spec/visual-verify/screenshots/harmony
#
# features JSON 格式:
# [
#   {
#     "feature_id": "F-001",
#     "feature_name": "音频播放",
#     "harmony_page": "pages/AudioPlayerPage",
#     "wait_seconds": 3
#   },
#   ...
# ]

set -euo pipefail

BUNDLE=""
MODULE="entry"
FEATURES_FILE=""
OUTPUT_DIR=""
WAIT_DEFAULT=4
TEMP_TARGET_FILE="/data/local/tmp/visual_verify_target_page.txt"

while [[ $# -gt 0 ]]; do
  case $1 in
    --bundle)    BUNDLE="$2"; shift 2 ;;
    --module)    MODULE="$2"; shift 2 ;;
    --features)  FEATURES_FILE="$2"; shift 2 ;;
    --output)    OUTPUT_DIR="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

if [[ -z "$BUNDLE" || -z "$FEATURES_FILE" || -z "$OUTPUT_DIR" ]]; then
  echo "Usage: capture_harmony_screens.sh --bundle BUNDLE --features JSON --output DIR"
  exit 1
fi

if ! command -v hdc &>/dev/null; then
  echo "ERROR: hdc not found in PATH"
  exit 1
fi

TARGETS=$(hdc list targets 2>/dev/null | grep -v "^\[Empty\]" | wc -l | tr -d ' ')
if [[ "$TARGETS" == "0" ]]; then
  echo "ERROR: No HarmonyOS device/emulator connected"
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

TOTAL=$(python3 -c "import json; print(len(json.load(open('$FEATURES_FILE'))))")
CURRENT=0
SUCCESS=0
FAILED=0

echo "=== HarmonyOS Screenshot Capture ==="
echo "Bundle: $BUNDLE"
echo "Module: $MODULE"
echo "Features: $TOTAL"
echo "Output: $OUTPUT_DIR"
echo ""

while IFS= read -r line; do
  FEATURE_ID=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['feature_id'])")
  FEATURE_NAME=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['feature_name'])")
  HARMONY_PAGE=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['harmony_page'])")
  WAIT=$(echo "$line" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('wait_seconds', $WAIT_DEFAULT))")

  CURRENT=$((CURRENT + 1))
  echo "[$CURRENT/$TOTAL] $FEATURE_ID: $FEATURE_NAME"
  echo "  Page: $HARMONY_PAGE"

  OUTPUT_FILE="$OUTPUT_DIR/${FEATURE_ID}.png"
  TEMP_FILE="/data/local/tmp/visual_verify_${FEATURE_ID}.png"

  NAVIGATED=false

  echo "  Navigating to page..."

  # 方案 A: 通过 aa start 传递 -e 参数
  if hdc shell aa start -a ScreenshotAbility -b "$BUNDLE" -m "$MODULE" \
       -e targetPage "$HARMONY_PAGE" 2>/dev/null; then
    NAVIGATED=true
  fi

  # 方案 B: 通过临时文件传递目标页面
  if [[ "$NAVIGATED" != "true" ]]; then
    echo "  Trying fallback: file-based navigation..."
    hdc shell "echo '$HARMONY_PAGE' > $TEMP_TARGET_FILE" 2>/dev/null || true
    if hdc shell aa start -a ScreenshotAbility -b "$BUNDLE" -m "$MODULE" 2>/dev/null; then
      NAVIGATED=true
    fi
  fi

  # 方案 C: 直接启动主 Ability（降级，截首页）
  if [[ "$NAVIGATED" != "true" ]]; then
    echo "  ⚠️ ScreenshotAbility not available, launching main Ability..."
    hdc shell aa start -a EntryAbility -b "$BUNDLE" -m "$MODULE" 2>/dev/null || true
  fi

  echo "  Waiting ${WAIT}s for page to render..."
  sleep "$WAIT"

  echo "  Capturing screenshot..."

  # 尝试 snapshot_display
  if hdc shell snapshot_display -f "$TEMP_FILE" 2>/dev/null; then
    if hdc file recv "$TEMP_FILE" "$OUTPUT_FILE" 2>/dev/null; then
      FILE_SIZE=$(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE" 2>/dev/null || echo "0")
      if [[ "$FILE_SIZE" -gt 10240 ]]; then
        echo "  ✅ Captured (${FILE_SIZE} bytes)"
        SUCCESS=$((SUCCESS + 1))
      else
        echo "  ⚠️ Screenshot too small (${FILE_SIZE} bytes)"
        rm -f "$OUTPUT_FILE"
        FAILED=$((FAILED + 1))
      fi
    else
      echo "  ❌ Failed to receive screenshot"
      FAILED=$((FAILED + 1))
    fi
    hdc shell rm -f "$TEMP_FILE" 2>/dev/null || true
  else
    echo "  ❌ snapshot_display failed, trying screencap..."
    if hdc shell "snapshot_display" 2>/dev/null | \
       python3 -c "
import sys
data = sys.stdin.buffer.read()
if len(data) > 10240:
    with open('$OUTPUT_FILE', 'wb') as f:
        f.write(data)
    print('ok')
else:
    print('too_small')
" 2>/dev/null | grep -q "ok"; then
      echo "  ✅ Captured via screencap"
      SUCCESS=$((SUCCESS + 1))
    else
      echo "  ❌ All capture methods failed"
      FAILED=$((FAILED + 1))
    fi
  fi

  hdc shell rm -f "$TEMP_TARGET_FILE" 2>/dev/null || true
  echo ""
done < <(python3 -c "
import json
features = json.load(open('$FEATURES_FILE'))
for f in features:
  print(json.dumps(f))
")

echo "=== HarmonyOS Screenshot Summary ==="
echo "Total: $TOTAL"
echo "Success: $SUCCESS"
echo "Failed: $FAILED"
echo "Output: $OUTPUT_DIR"

if [[ "$FAILED" -gt 0 ]]; then
  exit 1
fi
