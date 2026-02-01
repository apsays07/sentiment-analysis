from http.server import BaseHTTPRequestHandler
import json
import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model_pickle")

model = None  # lazy load

def load_model():
    global model
    if model is None:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
    return model

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            load_model()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({
                    "status": "success",
                    "message": "Model loaded successfully"
                }).encode()
            )
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(
                json.dumps({
                    "error": str(e)
                }).encode()
            )
