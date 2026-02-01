from flask import Flask, request, jsonify
import pickle

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

    # Example prediction logic (replace with your own)
    result = "positive"

    return jsonify({
        "input": text,
        "sentiment": result
    })

if __name__ == "__main__":
    app.run()
