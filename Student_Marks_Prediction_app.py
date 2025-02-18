import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib
import os

# Set up the Flask app and template folder
app = Flask(__name__, template_folder='C:/Users/Jan Saida/OneDrive/Documents/Students Marks Prediction Project/templates')

# Load the trained model
model = joblib.load(r"C:/Users/Jan Saida/OneDrive/Documents/Students Marks Prediction Project/student_mark_predictor.pkl")

# Create an empty DataFrame for saving prediction data
df = pd.DataFrame()

# Define the home route
@app.route('/')
def home():
    return render_template("index.html")

# Define the predict route
@app.route('/predict', methods=['POST'])
def predict():
    global df
    
    # Collect input data from the form
    input_features = [int(x) for x in request.form.values()]
    features_value = np.array(input_features)
    
    # Validate the input hours
    if input_features[0] < 0 or input_features[0] > 24:
        return render_template('index.html', prediction_text='Please enter valid hours between 1 and 24 if you live on the Earth')
    
    # Predict the output based on the input features
    output = model.predict([features_value])[0][0].round(2)
    
    # Save the input data and predicted output into the DataFrame
    df = pd.concat([df, pd.DataFrame({'Study Hours': input_features, 'Predicted Output': [output]})], ignore_index=True)
    
    # Print and save the DataFrame to a CSV file
    print(df)
    df.to_csv('smp_data_from_app.csv')
    
    # Render the result back to the user
    return render_template("index.html", prediction_text=f'You will get [{output}%] marks, when you study [{input_features[0]}] hours per day')

# Run the Flask app
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
