import requests, json, traceback
from requests.exceptions import HTTPError

RESPONSE_FIELDS = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]

def emotion_detector(text_to_analyse):
    response = requests.post(
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict",
        headers={
            "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
            "content-type": "application/json"
        },
        json={"raw_document": {"text": text_to_analyse}}
    )
    try:
        response.raise_for_status()
        data = json.loads(response.text)
        emotion_data = data.get("emotionPredictions")[0].get("emotion")

        sorted_emotions = sorted(emotion_data.items(), key=lambda x: x[1])
        return json.dumps(get_response_data(**emotion_data, dominant_emotion=emotion_data))
    except HTTPError as http_error:
        if response.status_code == 400:
            return json.dumps(get_response_data())

        raise http_error
    except Exception as ex:
        raise ex

def get_response_data(**kwargs):
    response = {}
    for f in RESPONSE_FIELDS:
        response[f] = kwargs.get(f, None)
    return response
