import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(
        message="Hello! My PaaS Application is Running on Render 🚀",
        status="ok",
    )


@app.get("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    # Use the platform-provided port when available (common on PaaS providers)
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)
