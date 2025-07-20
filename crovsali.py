import joblib
from PIL import Image
import numpy as np

# Load the trained model
model = joblib.load("croc_vs_aligator_model.pkl")

# Image preprocessing function (must match training)
def prepare_image(img_path):
    img = Image.open(img_path).resize((100, 100)).convert('RGB')
    img_array = np.array(img).flatten().reshape(1, -1)  # Flatten and reshape
    return img_array

# Predict on a new image
test_img_path = r"E:\datascience\crovsali\aligator\test3.png"  # <-- Change this path

# Prepare image and predict
image_data = prepare_image(test_img_path)
prediction = model.predict(image_data)

print("Predicted label:", prediction[0])
