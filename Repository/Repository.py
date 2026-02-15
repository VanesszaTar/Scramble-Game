import random

class SentenceRepository:
    def __init__(self, filename):
        self.filename = filename
        self.sentences = self.loadSentences()

    def loadSentences(self):
        with open(self.filename, "r") as f:
            lines = [line.strip() for line in f.readlines()]
        return [line for line in lines if line and not line.startswith("scramble")]

    def getRandomSentence(self):
        return random.choice(self.sentences)