from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('Saved_Trip_price.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define a route for predicting trip price
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Return prediction as JSON response
        return jsonify({'prediction': 'Your total amount is $' + str(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
