# Import necessary libraries
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('Saved_Trip_price.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the function to predict trip price
def predict_price(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, trip_distance, tolls_amount, fare_amount, year, month, day, time):
    features = np.array([[pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, trip_distance, tolls_amount, fare_amount, year, month, day, time]])
    price = model.predict(features)
    return price[0]

# Streamlit app
def main():
    # Set title and description
    st.title('Trip Price Prediction')
    st.write('This app predicts the price of a trip based on various features.')

    # Add input fields
    pickup_longitude = st.number_input('Pickup Longitude')
    pickup_latitude = st.number_input('Pickup Latitude')
    dropoff_longitude = st.number_input('Dropoff Longitude')
    dropoff_latitude = st.number_input('Dropoff Latitude')
    passenger_count = st.slider('Passenger Count', min_value=1, max_value=10, value=1)
    trip_distance = st.number_input('Trip Distance (miles)')
    tolls_amount = st.number_input('Tolls Amount ($)')
    fare_amount = st.number_input('Fare Amount ($)')
    year = st.number_input('Year', min_value=2009, max_value=2025, value=2021)
    month = st.slider('Month', min_value=1, max_value=12, value=6)
    day = st.slider('Day', min_value=1, max_value=31, value=15)
    time = st.slider('Time (24-hour format)', min_value=0, max_value=23, value=12)

    # Predict price on button click
    if st.button('Predict Price'):
        price = predict_price(pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count, trip_distance, tolls_amount, fare_amount, year, month, day, time)
        st.success(f'The estimated price for the trip is ${price:.2f}')

if __name__ == '__main__':
    main()
