import requests, json, traceback

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
        print(data)
        emotion_data = data.get("emotionPredictions")[0].get("emotion")

        sorted_emotions = sorted(emotion_data.items(), key=lambda x: x[1])
        return json.dumps({
            "anger": emotion_data.get("anger"),
            "disgust": emotion_data.get("disgust"),
            "fear": emotion_data.get("fear"),
            "joy": emotion_data.get("joy"),
            "sadness": emotion_data.get("sadness"),
            "dominant_emotion": sorted_emotions[-1][0]
        })
    except Exception as ex:
        raise ex