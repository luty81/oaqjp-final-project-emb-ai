import json, unittest
from parameterized import parameterized
from EmotionDetection import emotion_detector, get_response_data

class TestEmotionDetection(unittest.TestCase):

    EXPECTED_FIELDS = ["anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"]


    @parameterized.expand([
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ])
    def test_emotion_detection(self, statement, expected_dominant_emotion):
        result = json.loads(emotion_detector(statement))

        self.assertEqual(result.get("dominant_emotion"), expected_dominant_emotion)

    def test_emotion_detection_when_bad_request_is_returned(self):
        empty_response = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None,
            "dominant_emotion": None
        }

        result = json.loads(emotion_detector(""))

        self.assertEqual(result, empty_response)


    def test_should_return_the_response_with_all_properties_as_none(self):
        result = get_response_data()

        self.assertEqual([f for f in result.keys()], self.EXPECTED_FIELDS)
        for key, value in result.items():
            self.assertIsNone(value)

    def test_get_response_data(self):
        response_sample = {
            "anger": 0.2, "disgust": 0.23, "fear": 0.12, "joy": 0.90, "sadness": 0.19, "not_expected_field": ""
        }

        result = get_response_data(**response_sample, dominant_emotion="joy")

        self.assertFalse("not_expected_field" in result.keys())
        self.assertEqual([f for f in result.keys()], self.EXPECTED_FIELDS)
        response_sample.pop("not_expected_field")
        response_sample["dominant_emotion"] = "joy"
        self.assertEqual(result, response_sample)

        
