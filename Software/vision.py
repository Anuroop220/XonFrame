from ultralytics import YOLO

model = YOLO("yolo11n.pt")
CONFIDENCE_THRESHOLD = 0.5


def detect_objects(frame):
    """Run YOLO and return detected object names."""
    results = model(frame, verbose=False)
    detections = []

    for r in results:
        for box in r.boxes:
            label = model.names[int(box.cls)]
            confidence = float(box.conf)

            if confidence > CONFIDENCE_THRESHOLD:
                detections.append(label)

    return list(set(detections))