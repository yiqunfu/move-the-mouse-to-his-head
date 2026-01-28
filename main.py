import time
import cv2
import numpy as np
import pyautogui
from head_detector import find_head_center_from_frame

pyautogui.FAILSAFE = False

def move_mouse_to(point):
    x, y = point
    pyautogui.moveTo(x, y, duration=0.02)


def capture_screen(resize_factor=0.75):
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return frame, resize_factor


def main():
    print("Starting head aiming. Press Ctrl+C to stop.")
    time.sleep(1)
    try:
        while True:
            frame, resize_factor = capture_screen()
            head_center = find_head_center_from_frame(frame, resize_factor=resize_factor)
            if head_center:
                move_mouse_to(head_center)
            time.sleep(0.02)
    except KeyboardInterrupt:
        print("Stopped.")


if __name__ == "__main__":
    main()
