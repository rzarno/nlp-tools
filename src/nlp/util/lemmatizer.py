from textblob import Word

class Lemmatizer:
    def process(self, data):
        return " ".join([Word(word).lemmatize() for word in data.split()])