import streamlit as st
import pickle
import numpy as np

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🏠 California House Price Predictor")
st.write("Enter the details below to predict the house price:")

MedInc = st.slider("Median Income (in 10k USD)", 0.5, 15.0, 3.0)
HouseAge = st.slider("House Age (years)", 1, 52, 20)
AveRooms = st.slider("Average Rooms", 1.0, 10.0, 5.0)
AveBedrms = st.slider("Average Bedrooms", 1.0, 5.0, 1.0)
Population = st.slider("Population", 3, 35000, 1000)
AveOccup = st.slider("Average Occupants per House", 1.0, 10.0, 3.0)
Latitude = st.slider("Latitude", 32.0, 42.0, 36.0)
Longitude = st.slider("Longitude", -124.0, -114.0, -119.0)

if st.button("Predict Price"):
    features = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                          Population, AveOccup, Latitude, Longitude]])
    prediction = model.predict(features)
    st.success(f"Predicted House Price: ${prediction[0]*100000:,.2f}")
