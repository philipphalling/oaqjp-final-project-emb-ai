import requests

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    OBJ = { "raw_document": { "text": text_to_analyse } }

    res = requests.post(url=URL, json=OBJ, headers=HEADERS)

    if res.status_code == 200:
        
        data = res.json()
        scores = data['emotionPredictions'][0]['emotion']

        apiReturn = {
                'anger': scores['anger'],
                'disgust': scores['disgust'],
                'fear': scores['fear'],
                'joy': scores['joy'],
                'sadness': scores['sadness'],
                'dominant_emotion': max(scores, key=scores.get),
        }
        return apiReturn

    elif res.status_code == 400:

        apiReturn = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }
        return apiReturn

