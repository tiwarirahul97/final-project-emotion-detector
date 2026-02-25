import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion detection API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    dominant_emotion = "anger"
    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    dominant_emotion_score = anger_score
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    if disgust_score>dominant_emotion_score:
        dominant_emotion = "disgust"
        dominant_emotion_score = disgust_score
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    if fear_score>dominant_emotion_score:
        dominant_emotion = "fear"
        dominant_emotion_score = fear_score
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    if joy_score>dominant_emotion_score:
        dominant_emotion = "joy"
        dominant_emotion_score = joy_score
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    if sadness_score>dominant_emotion_score:
        dominant_emotion = "sadness"
        dominant_emotion_score = sadness_score

    return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }