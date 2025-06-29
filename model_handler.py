from ultralytics import YOLO
import cv2

# Load detection model (YOLOv8 - object detection)
detection_model = YOLO("models/detection_model_yolov8s_best_100_gpu_27062025.pt")

# Load classification model (YOLOv8-cls - image classification)
classification_model = YOLO("models/classification_model_yolov8s-cls_best_100_gpu_28062025.pt")


def predict_objects(frame):
    results = detection_model(frame)[0]
    detections = []

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        conf = float(box.conf[0])
        det_cls = int(box.cls[0])
        cropped = frame[y1:y2, x1:x2]

        # Nếu vùng crop không rỗng thì chạy phân loại
        if cropped.size != 0:
            cls_result = classification_model(cropped)[0]
            pred_cls = int(cls_result.probs.top1)
        else:
            pred_cls = -1

        detections.append({
            "box": (x1, y1, x2, y2),
            "conf": conf,
            "det_label": det_cls,
            "cls_label": pred_cls
        })

    return detections
