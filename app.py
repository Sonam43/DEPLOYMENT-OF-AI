from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Diabetes Prediction API is live!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
