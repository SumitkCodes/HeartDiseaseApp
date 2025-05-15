from flask import Flask, request, jsonify
import pickle
import numpy as np

model = pickle.load(open('model1.pkl','rb'))

try:
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except:
    scaler = None

app = Flask(__name__)

@app.route('/')
def home():
    return "Heart Disease Prediction App"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        cp = float(request.form.get('cp', 0))
        thalach = float(request.form.get('thalach', 0))
        slope = float(request.form.get('slope', 0))
        restecg = float(request.form.get('restecg', 0))
        chol = float(request.form.get('chol', 0))
        trestbps = float(request.form.get('trestbps', 0))
        fbs = float(request.form.get('fbs', 0))
        oldpeak = float(request.form.get('oldpeak', 0))

        input_query = np.array([[cp, thalach, slope, restecg, chol, trestbps, fbs, oldpeak]])

        if scaler:
            input_query = scaler.transform(input_query)

        result = model.predict(input_query)[0]
        return jsonify({'target': str(result)})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
