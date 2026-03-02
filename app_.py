
                

from flask import Flask, render_template, request
import cv2
import os
from ultralytics import YOLO
import requests
import folium

app_ = Flask(__name__)
upload_fold = "static/uploads"
app_.config["upload_fold"] = upload_fold

os.makedirs(upload_fold, exist_ok=True)

model = YOLO("yolov8n.pt")

NASA_API_KEY = "DEMO_KEY"
NASA_URL = "https://api.nasa.gov/planetary/earth/imagery"

def get_location_from_nasa():
    params = {
        "lat": 30.3753,
        "lon": 69.3451,
        "dim": 0.10,
        "api_key": NASA_API_KEY
    }
    requests.get(NASA_URL, params=params)
    return 30.3753, 69.3451

def detect_animals(image_path):
    results = model(image_path)
    detected = False

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            label = model.names[cls]
            if label in ["cow", "sheep", "horse", "dog", "cat", "elephant", "zebra", "giraffe"]:
                detected = True

    return detected, results[0].plot()

def create_map(lat, lon):
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker([lat, lon], popup="Animal Herd Detected 🚨").add_to(m)
    map_path = "static/map.html"
    m.save(map_path)
    return map_path

@app_.route("/", methods=["GET", "POST"])
def index():
    map_path = None
    result_image = None

    if request.method == "POST":
        file = request.files["image"]
        path = os.path.join(app_.config["upload_fold"], file.filename)
        file.save(path)

        detected, result_img_array = detect_animals(path)
        result_path = os.path.join(app_.config["upload_fold"], "result.jpg")
        cv2.imwrite(result_path, result_img_array)

        if detected:
            lat, lon = get_location_from_nasa()
            map_path = create_map(lat, lon)

        result_image = result_path

    return render_template("index.html", map_path=map_path, result_image=result_image)

if __name__ == "__main__":
    app_.run(debug=True)

