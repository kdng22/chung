from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEBHOOK_URL = "https://script.google.com/macros/s/YOUR_SCRIPT_ID/exec"

@app.route("/", methods=["POST"])
def forward_to_webhook():
    try:
        data = request.get_json()
        data["author"] = data.get("author", "이모")
        resp = requests.post(WEBHOOK_URL, json=data)
        return jsonify({"status": "ok"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def hello():
    return "중계 서버 작동 중입니다!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

