from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load model once at startup
with open("model_pickle", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Sentiment Analysis API running"})

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    # TODO: replace this with real model prediction
    result = "positive"

    return jsonify({
        "input": text,
        "sentiment": result
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
