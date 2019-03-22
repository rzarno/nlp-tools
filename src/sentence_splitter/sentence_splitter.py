import json
import nltk
from src.sentence_splitter.special_case_rule_street_shortcut import SpecialCaseRuleStreetShortcut

nltk.download('punkt')


class SentenceSplitter:

    __specialCaseRules = []

    def __init__(self):
        self.__specialCaseRules = [
            SpecialCaseRuleStreetShortcut()
        ]

    def split(self, data: str) -> str:
        split = nltk.tokenize.sent_tokenize(data, 'english')
        split = self.__applySpecialCaseRules(split)
        return json.dumps(split)

    def __applySpecialCaseRules(self, split: list) -> list:
        for rule in self.__specialCaseRules:
            return rule.apply(split)
