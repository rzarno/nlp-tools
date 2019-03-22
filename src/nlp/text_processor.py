from src.nlp.util.lemmatizer import Lemmatizer
from src.nlp.util.punctuation_remover import PunctuationRemover
from src.nlp.util.numeric_remover import NumericRemover
from src.nlp.util.lowercase_applier import LowercaseApplier
from src.nlp.util.stop_word_remover import StopWordRemover
# from src.nlp.util.rare_word_remover import RareWordRemover
# from src.nlp.util.frequent_word_remover import FrequentWordRemover

class TextProcessor:

    punctuationRemover = None
    numericRemover = None
    lowercaseApplier = None
    stopWordRemover = None
    rareWordRemover = None
    frequentWordRemover = None
    lemmatizer = None

    def __init__(self):
        self.punctuationRemover = PunctuationRemover()
        self.numericRemover = NumericRemover()
        self.lowercaseApplier = LowercaseApplier()
        self.stopWordRemover = StopWordRemover()
        # self.rareWordRemover = RareWordRemover()
        # self.frequentWordRemover = FrequentWordRemover()
        self.lemmatizer = Lemmatizer()

    def normalize(self, data):
        data = self.numericRemover.process(data)
        data = self.punctuationRemover.process(data)
        data = self.lowercaseApplier.process(data)
        data = self.stopWordRemover.process(data)
        # data = self.frequentWordRemover.process(data)
        # data = self.rareWordRemover.process(data)
        data = self.lemmatizer.process(data)
        return data
