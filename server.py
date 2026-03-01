from flask import Flask, request, jsonify
import json
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    # Get text from URL query parameter
    text_to_analyze = request.args.get("textToAnalyze")

    # Handle empty input
    if not text_to_analyze:
        return jsonify({
            "error": "No text provided"
        }), 400

    # Call your emotion detector function
    response = emotion_detector(text_to_analyze)

    # Convert response string to dictionary
    data = json.loads(response)

    # Return JSON response
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
