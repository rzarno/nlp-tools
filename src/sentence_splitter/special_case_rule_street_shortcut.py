from src.sentence_splitter.special_case_rule import SpecialCaseRule
import re

class SpecialCaseRuleStreetShortcut(SpecialCaseRule):

    def apply(self, sentences: list) -> list:
        length = len(sentences)
        rewrited = []
        for idx, sentence in enumerate(sentences):
            if re.search(r'[a-z]+str\.$', sentence, re.I) and length > idx + 1:
                sentences[idx + 1] = sentence + ' ' + sentences[idx + 1]
            else:
                rewrited.append(sentence)
        return rewrited
