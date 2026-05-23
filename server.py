from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():

    text_to_analyze = request.args.get(
        'textToAnalyze'
    )

    response = emotion_detector(
        text_to_analyze
    )

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, "
        f"the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is "
        f"{response['dominant_emotion']}."
    )


@app.route("/")
def render_index_page():
    return "Emotion Detection Application"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
