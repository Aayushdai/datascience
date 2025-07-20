import streamlit as st 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import joblib  # Add this import
from sklearn.preprocessing import LabelEncoder 

# Load the model 
model = joblib.load('taxi_fare.pkl')

# Encode dataset 
def encode(data): 
    encoder = LabelEncoder()
    cat_cols = data.select_dtypes('object')
    for col in cat_cols: 
        data[col] = encoder.fit_transform(data[col])
    
    return data 

# Create Streamlit frontend 
st.title("Taxi Fare Prediction")
file = st.file_uploader("Choose your CSV file", type=['csv'])

try:
    if file is not None: 
        df = pd.read_csv(file)
        df_r = encode(df)
        
        # Make prediction
        df['trip_fare'] = model.predict(df_r)  # Use df instead of undefined 'data'
        st.write(df)

    else: 
        st.write("File cannot be read")
except Exception as e: 
    st.write(f"Exception {e} occurred")
