import streamlit as st
import joblib
from PIL import Image
import numpy as np

# Load the trained model
model = joblib.load("croc_vs_aligator_model.pkl")

# Title
st.title("Crocodile vs Alligator Classifier 🐊🆚🐊")

# Instructions
st.write("Upload an image of a crocodile or an alligator. The model will predict which one it is.")

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Prediction logic
def prepare_image(image):
    img = image.resize((100, 100)).convert('RGB')
    img_array = np.array(img).flatten().reshape(1, -1)
    return img_array

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Prepare and predict
    img_data = prepare_image(image)
    prediction = model.predict(img_data)

    # Show prediction
    label = prediction[0]
    st.success(f"Predicted Label: **{label}**")
