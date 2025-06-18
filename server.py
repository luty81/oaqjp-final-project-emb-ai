"""
    Emotion Detection API
"""
import json
from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector API")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detect():
    """
        Emotion Detector endpoint
    """
    text_to_analyse = request.args.get("textToAnalyse")
    result = json.loads(emotion_detector(text_to_analyse))
    dominant_emotion = result.pop("dominant_emotion")
    if dominant_emotion:
        return f"""
            For the given statement, the system response is {result}. 
            The dominant emotion is {dominant_emotion}.
        """

    return "Invalid text! Please try again!"

if __name__ == "__main__":
    app.run()
