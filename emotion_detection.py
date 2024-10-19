import requests

def emotion_detector(text_to_analyse):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    OBJ = { "raw_document": { "text": text_to_analyse } }

    try:
        res = requests.post(url=URL, json=OBJ, headers=HEADERS)
        res.raise_for_status() 
        data = res.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

