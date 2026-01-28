# move-the-mouse-to-his-head

快速识别屏幕上出现的人形物体头部并将鼠标移动到头部中央的简单示例。

## 依赖

```bash
pip install -r requirements.txt
```

## 运行

```bash
python main.py
```

程序会持续截屏（默认缩放 0.75 提升速度），检测头部（使用 HOG 行人检测并截取上部分近似头部）并将鼠标移动到检测到的最大头部中心。若目标消失则自动锁定下一个；无头部时不移动。按 `Ctrl+C` 结束。

## 可视化界面

```bash
python gui.py
```

弹出控制台，点击 Start 启动检测，Stop 停止，Exit 退出。可通过 PyInstaller 打包为 exe：`pyinstaller --onefile --windowed gui.py`

可选环境变量：
- `MTM_RESIZE`：截屏缩放比例，默认 `0.75`（1.0 为原尺寸）
- `MTM_SLEEP`：循环休眠时间，默认 `0.02` 秒
- `MTM_MOVE_DURATION`：鼠标移动耗时，默认 `0.02` 秒
- `MTM_FAILSAFE`: 设置为 `1` 启用 pyautogui failsafe

注意：GUI 的 Start/Stop 已加防抖和安全停止，避免多次启动和线程未退出导致的异常。
