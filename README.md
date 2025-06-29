# 📹 Dispatch AI Monitoring

A real-time web application for monitoring dispatch scenarios using YOLOv8-based object detection and classification.  
The system allows uploading videos, live prediction, feedback collection, and user-friendly interface – all in one!

---

## ✨ Features

- 🎥 **Upload Video**: Upload your own dispatch video for analysis
- 🧠 **YOLOv8 Inference**: Predict with your own trained detection & classification models
- 🖥 **Live Stream Visualization**: See frame-by-frame results directly on the web
- 📝 **Feedback System**: Provide human annotation via timestamp-based feedback
- 🎨 **Modern UI**: Responsive design with styled components (HTML + CSS + JS)

---

## 🗂 Folder Structure

```
realtime_dispatch_monitoring/
├── app.py                        # Main FastAPI app
├── model_handler.py              # Model loading & prediction
├── video_handler.py              # Frame processing & visualization
├── static/
│   ├── styles.css                # UI styling
│   ├── scripts.js                # JS logic for uploads & feedback
│   └── uploads/                  # Uploaded videos (ignored via .gitignore)
├── templates/
│   └── index.html                # HTML template
├── models/                       # Your YOLOv8 models (.pt files)
│   ├── detection_model.pt
│   └── classification_model.pt
├── feedback.csv                  # Stores submitted feedback
├── requirements.txt              # Python dependencies
└── .gitignore                    # Ignore heavy files, logs, models...
```

---

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
uvicorn app:app --reload
```

Open in your browser: [http://localhost:8000](http://localhost:8000)

---

## 📁 Notes

- Place your models inside `models/` folder:
  - Detection model (e.g., `detection_model_yolov8s.pt`)
  - Classification model (e.g., `classification_model_yolov8s-cls.pt`)
- Upload video directly via browser UI

---

## 📮 Feedback & Contributions

This project supports timestamp-based human feedback. Contributions or suggestions are welcome!  
Please [open an issue](https://github.com/ngocdung1512/dispatch-ai-monitoring/issues) if you'd like to help.

---

## 📜 License

MIT License © 2025  
Ngọc Dũng – [GitHub](https://github.com/ngocdung1512)
