from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_detector():
	# Retrieve the text to analyze from the request arguments
	text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
	response = emotion_detector(text_to_analyze)

	# Extract the score from response
	anger_score = response['anger']
	disgust_score = response['disgust']
	fear_score = response['fear']
	joy_score = response['joy']
	sadness_score = response['sadness']
	dominant_emotion = response['dominant_emotion']

	return "For the given statement, the system response is 'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. The dominant emotion is <b>{}</b>.".format(anger_score, disgust_score, fear_score, joy_score, sadness_score, dominant_emotion)


@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)