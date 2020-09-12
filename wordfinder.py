"""Word Finder: finds random words from a dictionary."""
from random import randint

class WordFinder:
    ...
    def __init__(self, path):
        "Creates instance of WordFinder class and prints number of words in doc"
        txt_file = open(path)
        self.words = [word.strip() for word in txt_file]
        print(f"{len(self.words)} words read")

    def random(self):
        return self.words[randint(0, len(self.words))]

class SpecialWordFinder(WordFinder):

    def __init__(self, path):
        super().__init__(path)
        txt_file = open(path)
        self.words = [word.strip() for word in txt_file]

    def no_pound(self):
        return [word.strip() for word in self.words if not word.startswith('#') and word.strip()]
