class NumericRemover:
    def process(self, data):
        return " ".join(x for x in data.split() if not x.isnumeric())