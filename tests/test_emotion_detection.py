import json, unittest
from parameterized import parameterized
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    @parameterized.expand([
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ])
    def test_emotion_detection(self, statement, expected_dominant_emotion):
        result = json.loads(emotion_detector(statement))

        self.assertEqual(result.get("dominan_emotion"), expected_dominant_emotion)