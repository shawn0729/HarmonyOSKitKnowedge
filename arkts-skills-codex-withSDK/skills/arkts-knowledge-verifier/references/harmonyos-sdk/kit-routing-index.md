# HarmonyOS Kit Routing Index

This file routes uncertain HarmonyOS Kit API, import, permission, version, and error-code questions to the correct `arkts-skills-codex` skill.

## Fused Kit Routes

| Scenario | Primary Skill | Kit Reference |
|---|---|---|
| ArkUI component, layout, list rendering, component reuse | `arkts-component-builder` | `references/harmonyos-sdk/arkui/` |
| ArkUI state decorator or UI refresh behavior | `arkts-state-manager` | `references/harmonyos-sdk/arkui/` |
| Navigation, NavPathStack, NavDestination | `arkts-navigation-builder` | `references/harmonyos-sdk/arkui/` |
| HTTP, WebSocket, Socket, network status | `arkts-data-layer` | `references/harmonyos-sdk/network-kit/` |
| Preferences, RDB, relationalStore | `arkts-data-layer` | `references/harmonyos-sdk/arkdata/` |
| JSON, XML, Buffer, container classes | `arkts-data-layer` or `arkts-knowledge-verifier` | `references/harmonyos-sdk/arkts/` |
| Download network behavior | `arkts-download-manager` | `references/harmonyos-sdk/network-kit/` |
| Download file path and storage capacity | `arkts-download-manager` | `references/harmonyos-sdk/core-file-kit/` |
| Stage model, EntryAbility, module configuration | `arkts-project-scaffolder` | `references/harmonyos-sdk/ability-kit/` |
| Ability lifecycle, permissions, ExtensionAbility | `arkts-system-capabilities` | `references/harmonyos-sdk/ability-kit/` |
| Sandbox path, file access, file sharing | `arkts-system-capabilities` | `references/harmonyos-sdk/core-file-kit/` |
| AVPlayer, SoundPool, recorder, transcoder | `arkts-media-playback` | `references/harmonyos-sdk/media-kit/` |
| PixelMap, ImageSource, ImagePacker, image processing | `arkts-system-capabilities` | `references/harmonyos-sdk/image-kit/` |
| Web component, JSBridge, Cookie, UserAgent | `arkts-webview-manager` | `references/harmonyos-sdk/arkweb/` |
| Crash, AppFreeze, resource leak, performance diagnosis | `arkts-codebase-debug` or `hmos-env-doctor` | `references/harmonyos-sdk/performance-analysis-kit/` |

## Independent Kit Routes

| Scenario | Skill |
|---|---|
| Ads, monetization, banner/native/rewarded/interstitial/splash ads | `ads-kit-development` |
| Common events, account, USB, process and thread communication | `basic-services-kit-development` |
| Encryption, decryption, key generation, certificate, signature | `crypto-architecture-kit-development` |
| Service widget, FormExtensionAbility, card refresh and interaction | `form-kit-development` |
| System share, share panel, Knock Share, Air Transfer | `share-kit-development` |

## Rule

This index points to the correct skill. It does not replace the target skill. After choosing a route, read that skill's `SKILL.md` and its Kit references.
