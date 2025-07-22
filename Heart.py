import streamlit as st
import pandas as pd
import joblib

# Title
st.title("💡 Machine Learning Project - Heart Disease Classification")

# Load model
model_path = 'model_heart.pt'  # Make sure this is the same file you trained and saved using joblib
model = None

try:
    model = joblib.load(model_path)
    st.success("✅ Model loaded successfully.")
except FileNotFoundError:
    st.error(f"❌ Model file not found at: {model_path}")
except PermissionError:
    st.error(f"❌ Permission denied while accessing: {model_path}")
except Exception as e:
    st.error(f"❌ Unexpected error loading model: {e}")

# File uploader
st.header("📁 Upload CSV File for Prediction")
file = st.file_uploader("Upload your CSV file (must have required features)", type='csv')

if file is not None:
    if model is not None:
        try:
            # Read uploaded CSV
            data = pd.read_csv(file)

            # Drop 'HeartDisease' column if it exists
            if 'HeartDisease' in data.columns:
                st.warning("⚠️ 'HeartDisease' column detected in uploaded file. It will be removed before prediction.")
                data = data.drop(columns=['HeartDisease'])

            # Show preview
            st.subheader("🔍 Uploaded Data Preview")
            st.write(data.head())

            # Make predictions
            st.subheader("✅ Prediction Results")
            prediction = model.predict(data)
            data['Predicted'] = prediction
            st.write(data)

        except Exception as e:
            st.error(f"❌ Error during prediction: {e}")
    else:
        st.warning("⚠️ Model could not be loaded. Please check the path or format.")
else:
    st.info("👆 Please upload a CSV file with the correct format (features only).")

