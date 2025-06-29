from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import HTMLResponse, StreamingResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from video_handler import generate_frames
import shutil, os, csv
from pathlib import Path

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "static/uploads"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
app.state.current_video = None

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload_video")
async def upload_video(file: UploadFile = File(...)):
    video_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    app.state.current_video = video_path
    return RedirectResponse("/", status_code=303)

@app.get("/video_feed")
def video_feed():
    video_path = app.state.current_video
    if not video_path or not os.path.exists(video_path):
        return HTMLResponse(content="No video uploaded", status_code=400)

    return StreamingResponse(generate_frames(video_path), media_type="multipart/x-mixed-replace; boundary=frame")

@app.post("/submit_feedback")
async def submit_feedback(timestamp: str = Form(...), note: str = Form(...)):
    with open("feedback.csv", mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, note])
    return RedirectResponse("/", status_code=303)
