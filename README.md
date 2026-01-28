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

程序将持续截屏，检测头部（使用 HOG 行人检测并截取上部分近似头部）并将鼠标移动到检测到的最大头部中心。按 `Ctrl+C` 结束。
