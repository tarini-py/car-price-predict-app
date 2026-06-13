from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, welcome"

@app.route("/<username>", methods = ["GET"])
def index(username):
    return f"Hello {username}, welcome"

# Load model once at startup
with open("models/xgb_car_price_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST","GET"])
def predict():
    if request.method == "GET":
        return jsonify({
            "Instruction": "Send a POST request using this exact JSON format",
            "Note": "fuel_type can be Petrol/Diesel/Electric",
            
            "required_format": 
            {
                "km_driven": 45000,
                "mileage": 18,
                "age": 5,
                "fuel_type": "Petrol"
            }
        })
    
    data = request.json

    # Extract inputs
    km_driven = data["km_driven"]
    mileage = data["mileage"]
    age = data["age"]
    fuel_type = data["fuel_type"]

    # One-hot encoding
    fuel_encoding = {
        "Petrol": [1, 0, 0],
        "Diesel": [0, 1, 0],
        "Electric": [0, 0, 1]
    }

    petrol, diesel, electric = fuel_encoding[fuel_type]

    input_df = pd.DataFrame(
        [[km_driven, mileage, age, petrol, diesel, electric]],
        columns=["km_driven", "mileage", "age", "Petrol", "Diesel", "Electric"]
    )

    prediction = model.predict(input_df)[0]

    return jsonify({
        "predicted_price": float(prediction)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


# {
#     "km_driven": 45000,
#     "mileage": 18,
#     "age": 5,
#     "fuel_type": "Petrol"
# }