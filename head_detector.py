import cv2
import numpy as np


def _build_hog_detector():
    # Use default people detector and focus on head by cropping detections
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    return hog


_HOG = _build_hog_detector()


def detect_heads(image_bgr, resize_factor=1.0):
    frame = image_bgr
    scale = 1.0
    if resize_factor != 1.0:
        frame = cv2.resize(image_bgr, (0, 0), fx=resize_factor, fy=resize_factor)
        scale = 1.0 / resize_factor

    rects, _ = _HOG.detectMultiScale(frame, winStride=(8, 8), padding=(8, 8), scale=1.05)
    heads = []
    for (x, y, w, h) in rects:
        x = int(x * scale)
        y = int(y * scale)
        w = int(w * scale)
        h = int(h * scale)
        # Approximate head region as top quarter of detection
        head_h = int(h * 0.25)
        heads.append((x + w // 2, y + head_h // 2, w, head_h))
    return heads

def find_head_center_from_frame(frame_bgr, resize_factor=1.0):
    heads = detect_heads(frame_bgr, resize_factor=resize_factor)
    if not heads:
        return None
    # Choose largest detected head region
    heads.sort(key=lambda r: r[2] * r[3], reverse=True)
    x_center, y_center, _, _ = heads[0]
    return x_center, y_center
