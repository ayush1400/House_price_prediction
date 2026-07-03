from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
model = pickle.load(
    open("house_price_model.pkl", "rb")
)

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    features = np.array(
        data['features']
    ).reshape(1, -1)

    prediction = model.predict(features)

    return jsonify({
        "predicted_price":
        float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)