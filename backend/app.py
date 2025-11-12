from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io
from PIL import Image

app = FastAPI()

# Izinkan frontend mengakses backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

import os
from keras.models import load_model

path_model = r"C:\Users\Administrator\Documents\Project\Python\backend\model\model_tembakau.keras"
model = load_model(path_model)
class_names = ["alternaria alternata", "cercospora nicotianae","no cercospora nicotianae or alternaria alternata present"]  # ganti sesuai dataset kamu

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    img_bytes = await file.read()
    img = Image.open(io.BytesIO(img_bytes)).resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction, axis=1)[0]
    confidence = float(np.max(prediction))

    return {
        "predicted_class": class_names[class_idx],
        "confidence": round(confidence * 100, 2)
    }
