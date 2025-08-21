import streamlit as st
import joblib
from joblib import load
import numpy as np

model = load('linear_regression_model.joblib')
user_input = st.number_input('Enter house size:', min_value=100, max_value=10000, step=50)
input_array = np.array([user_input]).reshape(-1, 1)
if st.button('Predict Price'):
    predicted_price = model.predict(input_array)
    st.write(f"The predicted house price is: ${predicted_price[0]:.2f}")




