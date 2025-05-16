import unittest
import json

from emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_1(self):
        text = "I am glad this happened."
        response = emotion_detector(text)
        
    def test_2(self):
        text = "I am really mad about this."
        response = emotion_detector(text)

    def test_3(self):
        text = "I feel disgusted just hearing about this."
        response = emotion_detector(text)

    def test_4(self):
        text = "I am so sad about this."
        response = emotion_detector(text)

    def test_5(self):
        text = "I am really afraid that this will happpen."
        response = emotion_detector(text)

if __name__ == '__main__':
    unittest.main()