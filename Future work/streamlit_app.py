
import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('Saved_Trip_price.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define function to predict trip price
def predict_trip_price(features):
    features_arr = np.array(features).reshape(1, -1)
    prediction = model.predict(features_arr)
    return prediction[0]

# Define the main function for Streamlit app
def main():
    st.title('Trip Price Prediction')

    st.write('Enter the following details to predict trip price:')

    # Input fields for features
    pickup_longitude = st.number_input('Pickup Longitude:')
    pickup_latitude = st.number_input('Pickup Latitude:')
    dropoff_longitude = st.number_input('Dropoff Longitude:')
    dropoff_latitude = st.number_input('Dropoff Latitude:')
    passenger_count = st.number_input('Number of Passengers:')
    trip_distance = st.number_input('Trip Distance:')
    tolls_amount = st.number_input('Tolls Amount:')
    fare_amount = st.number_input('Fare Amount:')
    year = st.number_input('Year:')
    month = st.number_input('Month:')
    day = st.number_input('Day:')
    time = st.number_input('Time:')

    # Predict trip price when 'Predict' button is clicked
    if st.button('Predict'):
        features = [pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count,
                    trip_distance, tolls_amount, fare_amount, year, month, day, time]
        prediction = predict_trip_price(features)
        st.success(f'Your total amount is ${prediction:.2f}')

if __name__ == '__main__':
    main()
