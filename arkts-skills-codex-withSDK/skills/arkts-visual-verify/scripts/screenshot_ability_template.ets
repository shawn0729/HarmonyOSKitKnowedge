import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit'
import { window } from '@kit.ArkUI'
import { fileIo } from '@kit.CoreFileKit'

// ScreenshotAbility — 视觉验证专用导航能力
// 注意：字段名不能叫 launchWant，与基类 UIAbility.launchWant 冲突
export default class ScreenshotAbility extends UIAbility {
  private savedWant: Want = {}

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    this.savedWant = want
    console.info('[ScreenshotAbility] onCreate')
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    console.info('[ScreenshotAbility] onWindowStageCreate')

    let targetPage: string = ''

    // 方案 A: 从 want parameters 读取目标页面
    // 启动命令: hdc shell aa start -a ScreenshotAbility -b {bundle} -m entry --ps targetPage pages/XxxPage
    const params = this.savedWant.parameters
    if (params) {
      const paramPage = params['targetPage']
      if (typeof paramPage === 'string' && paramPage.length > 0) {
        targetPage = paramPage
        console.info(`[ScreenshotAbility] Got targetPage from parameters: ${targetPage}`)
      }
    }

    // 方案 B: 从临时文件读取目标页面（aa start 不支持 --ps 时的降级方案）
    // 写入命令: hdc shell "echo 'pages/XxxPage' > /data/local/tmp/visual_verify_target_page.txt"
    if (!targetPage) {
      try {
        const tempFilePath = '/data/local/tmp/visual_verify_target_page.txt'
        if (fileIo.accessSync(tempFilePath)) {
          const file = fileIo.openSync(tempFilePath, fileIo.OpenMode.READ_ONLY)
          const buf = new ArrayBuffer(256)
          fileIo.readSync(file.fd, buf)
          fileIo.closeSync(file)
          const decoder = new util.TextDecoder('utf-8')
          targetPage = decoder.decodeWithStream(new Uint8Array(buf)).trim().replace(/\0/g, '')
          console.info(`[ScreenshotAbility] Got targetPage from file: ${targetPage}`)
          fileIo.unlinkSync(tempFilePath)
        }
      } catch (e) {
        console.info(`[ScreenshotAbility] Failed to read target file: ${e}`)
      }
    }

    // 加载目标页面
    if (targetPage) {
      console.info(`[ScreenshotAbility] Loading: ${targetPage}`)
      windowStage.loadContent(targetPage, (err) => {
        if (err.code) {
          console.error(`[ScreenshotAbility] Failed to load ${targetPage}: ${JSON.stringify(err)}`)
          windowStage.loadContent('pages/Index')
        } else {
          console.info(`[ScreenshotAbility] Loaded: ${targetPage}`)
        }
      })
    } else {
      console.info('[ScreenshotAbility] No target page specified, loading Index')
      windowStage.loadContent('pages/Index')
    }
  }

  onDestroy(): void {
    console.info('[ScreenshotAbility] onDestroy')
  }
}
