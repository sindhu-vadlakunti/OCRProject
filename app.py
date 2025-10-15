from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)
API_KEY = "K88147149888957"  # Replace with your OCR.space API key

# Serve HTML form for browser
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# OCR endpoint (works with Postman & browser form)
@app.route('/ocr', methods=['POST'])
def ocr_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    payload = {'isOverlayRequired': False, 'apikey': API_KEY, 'language': 'eng'}

    # Send file to OCR.space
    response = requests.post(
        'https://api.ocr.space/parse/image',
        files={'file': (file.filename, file, file.content_type)},
        data=payload
    )

    result = response.json()

    # Handle errors
    if result.get("OCRExitCode") != 1 or "ParsedResults" not in result:
        return jsonify({"error": "OCR failed", "details": result}), 400

    parsed_text = result['ParsedResults'][0]['ParsedText']
    return jsonify({"text": parsed_text})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
