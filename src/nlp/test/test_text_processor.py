import unittest
from src.nlp.text_processor import TextProcessor

class TestPurposeIndustryCodeClassificationPredict(unittest.TestCase):

    def test_normalize(self):
        normalized = TextProcessor().normalize('Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.')
        self.assertEqual('python easy learn, powerful programming language. efficient high-level data structure simple effective approach object-oriented programming. python’s elegant syntax dynamic typing, together interpreted nature, make ideal language scripting rapid application development many area platforms.', normalized)

if __name__ == '__main__':
    unittest.main()