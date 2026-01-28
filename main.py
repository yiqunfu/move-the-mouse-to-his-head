import os
import time
import cv2
import numpy as np
import pyautogui
from head_detector import find_head_center_from_frame

# Fail-safe can interrupt automation unexpectedly. Keep disabled, but allow override via env.
pyautogui.FAILSAFE = os.getenv("MTM_FAILSAFE", "0") == "1"

DEFAULT_RESIZE = float(os.getenv("MTM_RESIZE", "0.75"))
DEFAULT_SLEEP = float(os.getenv("MTM_SLEEP", "0.02"))
DEFAULT_MOVE_DURATION = float(os.getenv("MTM_MOVE_DURATION", "0.02"))


def move_mouse_to(point):
    x, y = point
    pyautogui.moveTo(x, y, duration=DEFAULT_MOVE_DURATION)


def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return frame


def main():
    print("Starting head aiming. Press Ctrl+C to stop.")
    time.sleep(1)
    try:
        while True:
            frame = capture_screen()
            head_center = find_head_center_from_frame(frame, resize_factor=DEFAULT_RESIZE)
            if head_center:
                move_mouse_to(head_center)
            time.sleep(DEFAULT_SLEEP)
    except KeyboardInterrupt:
        print("Stopped.")


if __name__ == "__main__":
    main()
