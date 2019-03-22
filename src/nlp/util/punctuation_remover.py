class PunctuationRemover:
    def process(self, data):
        return data.replace('[^\w\s]', '')