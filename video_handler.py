import cv2
from model_handler import predict_objects

def generate_frames(video_path):
    cap = cv2.VideoCapture(video_path)

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Gọi model dự đoán
        detections = predict_objects(frame)

        # Vẽ kết quả lên khung hình
        for det in detections:
            x1, y1, x2, y2 = det["box"]
            conf = det["conf"]
            det_label = det["det_label"]
            cls_label = det["cls_label"]

            label = f"D{det_label} | C{cls_label} | {conf:.2f}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")

    cap.release()
