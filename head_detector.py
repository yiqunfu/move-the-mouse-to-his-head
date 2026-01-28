import cv2
import numpy as np

def _build_hog_detector():
    # Use default people detector and focus on head by cropping detections
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    return hog

def detect_heads(image_bgr):
    hog = _build_hog_detector()
    rects, _ = hog.detectMultiScale(image_bgr, winStride=(8, 8), padding=(8, 8), scale=1.05)
    heads = []
    for (x, y, w, h) in rects:
        # Approximate head region as top quarter of detection
        head_h = int(h * 0.25)
        heads.append((x + w // 2, y + head_h // 2, w, head_h))
    return heads

def find_head_center_from_frame(frame_bgr):
    heads = detect_heads(frame_bgr)
    if not heads:
        return None
    # Choose largest detected head region
    heads.sort(key=lambda r: r[2] * r[3], reverse=True)
    x_center, y_center, _, _ = heads[0]
    return x_center, y_center
