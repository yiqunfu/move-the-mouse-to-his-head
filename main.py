import time
import cv2
import numpy as np
import pyautogui
from head_detector import find_head_center_from_frame

def move_mouse_to(point):
    x, y = point
    pyautogui.moveTo(x, y, duration=0.05)

def capture_screen():
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    return frame

def main():
    print("Starting head aiming. Press Ctrl+C to stop.")
    time.sleep(2)
    try:
        while True:
            frame = capture_screen()
            head_center = find_head_center_from_frame(frame)
            if head_center:
                move_mouse_to(head_center)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Stopped.")

if __name__ == "__main__":
    main()
