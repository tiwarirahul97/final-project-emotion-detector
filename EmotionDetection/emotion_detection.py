import json
import requests

def emotion_detector(text_to_analyse):
    """
    Analyzes the emotion of the provided text using the Watson NLP service.
    """
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = {"raw_document": {"text": text_to_analyse}}

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the values from the response
    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        anger_score = emotions["anger"]
        disgust_score = emotions["disgust"]
        fear_score = emotions["fear"]
        joy_score = emotions["joy"]
        sadness_score = emotions["sadness"]

        # Determine dominant emotion
        dominant_emotion = "anger"
        dominant_emotion_score = anger_score

        if disgust_score > dominant_emotion_score:
            dominant_emotion = "disgust"
            dominant_emotion_score = disgust_score
        if fear_score > dominant_emotion_score:
            dominant_emotion = "fear"
            dominant_emotion_score = fear_score
        if joy_score > dominant_emotion_score:
            dominant_emotion = "joy"
            dominant_emotion_score = joy_score
        if sadness_score > dominant_emotion_score:
            dominant_emotion = "sadness"
            dominant_emotion_score = sadness_score

    # If the response status code is 400, set all to None
    elif response.status_code == 400:
        anger_score = None
        disgust_score = None
        fear_score = None
        joy_score = None
        sadness_score = None
        dominant_emotion = None

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }