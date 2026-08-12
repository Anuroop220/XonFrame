from ultralytics import YOLO

model = YOLO("yolo11n.pt")
CONFIDENCE_THRESHOLD = 0.5


def detect_objects(frame):
    """Run YOLO on a single frame (numpy BGR array) and return unique labels."""
    results = model(frame, verbose=False)
    detections = []
    for r in results:
        for box in r.boxes:
            label = model.names[int(box.cls)]
            conf = float(box.conf)
            if conf > CONFIDENCE_THRESHOLD:
                detections.append(label)
    return list(set(detections))
