from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    id = data['id']

    # Predict using the loaded model
    prediction = model.predict([[id]])[0]

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
