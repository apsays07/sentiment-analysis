from http.server import BaseHTTPRequestHandler
import json
import pickle
import os
from model_logic import predict_sentiment  # example import

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model_pickle")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        data = json.loads(body)

        text = data.get("text", "")

        result = "positive"  # replace with your model call
        # result = predict_sentiment(text)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {"sentiment": result}
        self.wfile.write(json.dumps(response).encode())
