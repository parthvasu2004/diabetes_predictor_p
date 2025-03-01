from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data for all 8 features
    pregnancies = float(request.form['pregnancies'])
    glucose = float(request.form['glucose'])
    blood_pressure = float(request.form['blood_pressure'])
    skin_thickness = float(request.form['skin_thickness'])
    insulin = float(request.form['insulin'])
    bmi = float(request.form['bmi'])
    diabetes_pedigree_function = float(request.form['diabetes_pedigree_function'])
    age = float(request.form['age'])

    # Create input data array with all 8 features
    input_data = (pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age)
    input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)
    
    # Standardize the input data
    std_data = scaler.transform(input_data_as_numpy_array)
    
    # Make prediction
    prediction = model.predict(std_data)
    
    # Determine the result
    result = 'not diabetic' if prediction[0] == 0 else 'diabetic'
    
    return render_template('result.html', prediction_text=f'The person is {result}')

if __name__ == "__main__":
    app.run(debug=True)
