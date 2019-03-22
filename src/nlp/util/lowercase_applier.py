class LowercaseApplier:
    def process(self, data):
        return " ".join(x.lower() for x in data.split())