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
![Screenshot of Loan Approval Prediction Web Interface](https://imgur.com/zNNWHEh.png)
