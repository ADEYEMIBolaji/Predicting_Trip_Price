# Machine Learning Prediction of Trip Price

This repository contains code for predicting the price of trips using machine learning techniques. The data used for training and prediction was downloaded from BigQuery during Google Cloud Platform (GCP) training.

## Dataset Description

The dataset consists of 10 columns:

1. `pickup_datetime`: Date and time of trip pickup
2. `pickup_longitude`: Longitude of pickup location
3. `pickup_latitude`: Latitude of pickup location
4. `dropoff_longitude`: Longitude of drop-off location
5. `dropoff_latitude`: Latitude of drop-off location
6. `passenger_count`: Number of passengers
7. `trip_distance`: Distance of the trip
8. `tolls_amount`: Amount of tolls paid during the trip
9. `fare_amount`: Fare amount
10. `total_amount`: Total amount paid

## Feature Engineering

Feature engineering was performed by splitting the pickup datetime into years, months, days, and an approximation of the hour of the day.

## Exploratory Data Analysis (EDA)

EDA was conducted to understand the relationship between various features and the target variable (`total_amount`). Below are some key insights:

### Average Total Amount by Year
![Screenshot of Average Trip Price per year](https://imgur.com/zNNWHEh.png)


### Average Total Amount by Month
![Screenshot of Average Trip Price per Month](https://imgur.com/vaPKfc5.png)


## Model Development

Baseline models including Decision Tree, Random Forest, XGBoost, and Linear Regression were trained. Random Forest outperformed others, and hyperparameter tuning was performed using Grid Search.

### Results
- **Mean Squared Error**: 24.0179
- **Mean Absolute Error**: 2.14788
- **Root Mean Squared Error**: 4.90081
- **R-squared Score**: 0.812162

The MAE of 2.14788 indicates that, on average, the model's prediction is off by approximately $2.15, while the RMSE of 4.90081 indicates that, on average, the model's predictions are off by approximately $4.90.

## Model Deployment

The best estimator (saved as `saved_trip_price.pkl`) was deployed using Gradio. The local URL for accessing the deployed model is [http://127.0.0.1:7874] try this ( https://93790c939dfc9f9eb6.gradio.live).
![Screenshot of Web interface Preview](https://imgur.com/klgz7a9.png)

Example of Input
1. Pickup Longitude: -73.9857
2. Pickup Latitude: 40.7484
3. Dropoff Longitude: -74.0060
4. Dropoff Latitude: 40.7128
5. Passenger Count: 3
6. Trip Distance: 5.2 miles
7. Month: May
8. Day: 10
9. Time: 15 (indicating 3pm)

### Requirements
- Gradio installed
- New York dataset imported

## Future Work

Future work includes deploying the model using Streamlit or Flask for wider accessibility and scalability.
