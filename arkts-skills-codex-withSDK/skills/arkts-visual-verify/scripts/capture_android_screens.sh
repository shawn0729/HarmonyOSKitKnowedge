#!/bin/bash
# capture_android_screens.sh
# 按功能粒度在 Android 模拟器上逐功能导航并截图
#
# 用法:
#   bash capture_android_screens.sh \
#     --package com.example.app \
#     --features spec/visual-verify/feature_screenshot_list.json \
#     --output spec/visual-verify/screenshots/android
#
# features JSON 格式:
# [
#   {
#     "feature_id": "F-001",
#     "feature_name": "音频播放",
#     "activity": "com.example.app.PlayerActivity",
#     "wait_seconds": 3,
#     "launch_params": {}
#   },
#   ...
# ]

set -euo pipefail

PACKAGE=""
FEATURES_FILE=""
OUTPUT_DIR=""
WAIT_DEFAULT=3

while [[ $# -gt 0 ]]; do
  case $1 in
    --package)   PACKAGE="$2"; shift 2 ;;
    --features)  FEATURES_FILE="$2"; shift 2 ;;
    --output)    OUTPUT_DIR="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

if [[ -z "$PACKAGE" || -z "$FEATURES_FILE" || -z "$OUTPUT_DIR" ]]; then
  echo "Usage: capture_android_screens.sh --package PKG --features JSON --output DIR"
  exit 1
fi

if ! command -v adb &>/dev/null; then
  echo "ERROR: adb not found in PATH"
  exit 1
fi

DEVICES=$(adb devices | grep -v "List" | grep -v "^$" | wc -l | tr -d ' ')
if [[ "$DEVICES" == "0" ]]; then
  echo "ERROR: No Android device/emulator connected"
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

TOTAL=$(python3 -c "import json; print(len(json.load(open('$FEATURES_FILE'))))")
CURRENT=0
SUCCESS=0
FAILED=0
SKIPPED=0

echo "=== Android Screenshot Capture ==="
echo "Package: $PACKAGE"
echo "Features: $TOTAL"
echo "Output: $OUTPUT_DIR"
echo ""

while IFS= read -r line; do
  FEATURE_ID=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['feature_id'])")
  FEATURE_NAME=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['feature_name'])")
  ACTIVITY=$(echo "$line" | python3 -c "import sys,json; print(json.load(sys.stdin)['activity'])")
  WAIT=$(echo "$line" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('wait_seconds', $WAIT_DEFAULT))")
  PARAMS=$(echo "$line" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('launch_params', {}))")

  CURRENT=$((CURRENT + 1))
  echo "[$CURRENT/$TOTAL] $FEATURE_ID: $FEATURE_NAME"
  echo "  Activity: $ACTIVITY"

  OUTPUT_FILE="$OUTPUT_DIR/${FEATURE_ID}.png"
  TEMP_FILE="/sdcard/visual_verify_${FEATURE_ID}.png"

  COMPONENT="$PACKAGE/$ACTIVITY"

  if [[ "$PARAMS" != "{}" ]]; then
    EXTRA_ARGS=$(echo "$PARAMS" | python3 -c "
import sys, json
params = json.load(sys.stdin)
args = []
for k, v in params.items():
    if isinstance(v, str):
        args.append(f'--es {k} \"{v}\"')
    elif isinstance(v, int):
        args.append(f'--ei {k} {v}')
    elif isinstance(v, bool):
        args.append(f'--ez {k} {\"true\" if v else \"false\"}')
print(' '.join(args))
")
    LAUNCH_CMD="adb shell am start -n $COMPONENT -W $EXTRA_ARGS"
  else
    LAUNCH_CMD="adb shell am start -n $COMPONENT -W"
  fi

  echo "  Launching..."

  if ! $LAUNCH_CMD &>/dev/null; then
    echo "  ⚠️ Launch failed, trying with package only..."
    adb shell am start -a android.intent.action.MAIN -n "$PACKAGE/.MainActivity" -W &>/dev/null || true
    sleep 2
  fi

  echo "  Waiting ${WAIT}s for page to render..."
  sleep "$WAIT"

  echo "  Capturing screenshot..."
  if adb shell screencap -p "$TEMP_FILE" 2>/dev/null; then
    if adb pull "$TEMP_FILE" "$OUTPUT_FILE" 2>/dev/null; then
      FILE_SIZE=$(stat -f%z "$OUTPUT_FILE" 2>/dev/null || stat -c%s "$OUTPUT_FILE" 2>/dev/null || echo "0")
      if [[ "$FILE_SIZE" -gt 10240 ]]; then
        echo "  ✅ Captured (${FILE_SIZE} bytes)"
        SUCCESS=$((SUCCESS + 1))
      else
        echo "  ⚠️ Screenshot too small (${FILE_SIZE} bytes), likely blank"
        rm -f "$OUTPUT_FILE"
        FAILED=$((FAILED + 1))
      fi
    else
      echo "  ❌ Failed to pull screenshot"
      FAILED=$((FAILED + 1))
    fi
    adb shell rm -f "$TEMP_FILE" 2>/dev/null || true
  else
    echo "  ❌ Failed to capture screenshot"
    FAILED=$((FAILED + 1))
  fi

  echo ""
done < <(python3 -c "
import json
features = json.load(open('$FEATURES_FILE'))
for f in features:
  print(json.dumps(f))
")

echo "=== Android Screenshot Summary ==="
echo "Total: $TOTAL"
echo "Success: $SUCCESS"
echo "Failed: $FAILED"
echo "Output: $OUTPUT_DIR"

if [[ "$FAILED" -gt 0 ]]; then
  exit 1
fi
