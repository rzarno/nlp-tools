import unittest
import json
from src.sentence_splitter.sentence_splitter import SentenceSplitter

class TestSentenceSplitter(unittest.TestCase):

    def test_split(self):
        data = [
            [
                'Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.',
                [
                    'Python is an easy to learn, powerful programming language.',
                    'It has efficient high-level data structures and a simple but effective approach to object-oriented programming.',
                    'Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.'
                ]
            ],
            [
                'This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature. Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style. After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library.',
                [
                    'This tutorial does not attempt to be comprehensive and cover every single feature, or even every commonly used feature.',
                    'Instead, it introduces many of Python’s most noteworthy features, and will give you a good idea of the language’s flavor and style.',
                    'After reading it, you will be able to read and write Python modules and programs, and you will be ready to learn more about the various Python library modules described in The Python Standard Library.'
                ]
            ]
        ]

        splitter = SentenceSplitter()

        for case in data:
            expected = case[1]
            text = case[0]
            actual = json.loads(splitter.split(text))
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
