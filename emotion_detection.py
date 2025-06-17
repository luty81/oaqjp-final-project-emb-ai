import requests

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
        return response.text
    except:
        print(response.text)