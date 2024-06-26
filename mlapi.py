from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from PIL import Image
import torch
from transformers import AutoImageProcessor, AutoModelForImageClassification
from io import BytesIO

app = FastAPI()

# Load the pre-trained model and processor
processor = AutoImageProcessor.from_pretrained("dima806/deepfake_vs_real_image_detection")
model = AutoModelForImageClassification.from_pretrained("dima806/deepfake_vs_real_image_detection")

class ImagePrediction(BaseModel):
    isReal: bool

def preprocess_image(image_file):
    image = Image.open(BytesIO(image_file)).convert("RGB")
    with torch.no_grad():
        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        return predicted_class == 0  # Return True if predicted as real, False otherwise

@app.post('/')
async def predictImage(image: UploadFile):
    is_real = preprocess_image(await image.read())
    return ImagePrediction(isReal=is_real)
