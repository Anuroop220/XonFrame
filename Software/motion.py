import cv2


def detect_motion(frame1, frame2, threshold=500):
    """Frame-diff motion detector. Works on any two BGR frames of the same
    size — originally fed by a local webcam, now fed by consecutive JPEG
    frames decoded from the glasses' WebSocket stream (see main.py)."""
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    motion = sum(cv2.contourArea(c) for c in contours)
    return motion > threshold
