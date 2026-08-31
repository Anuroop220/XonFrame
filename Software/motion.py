import cv2


def detect_motion(old_frame, new_frame, threshold=500):
    """ it will show True when camera frames show some movements"""
    difference = cv2.absdiff(old_frame, new_frame)
    gray_difference = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray_difference, (5, 5), 0)

    _, changed_pixels = cv2.threshold(
        blurred, 20, 255, cv2.THRESH_BINARY
    )

    contours, _ = cv2.findContours(
        changed_pixels,
        cv2.RETR_TREE,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    changed_area = sum(cv2.contourArea(contour) for contour in contours)
    return changed_area > threshold