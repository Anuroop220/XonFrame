from ultralytics import YOLO
import cv2

model = YOLO("yolo11n.pt")

def detect_objects(frame):
    results = model(frame, verbose=False)
    detections = []
    for r in results:
        for box in r.boxes:
            label = model.names[int(box.cls)]
            conf = float(box.conf)
            if conf > 0.5:
                detections.append(label)
    return list(set(detections))