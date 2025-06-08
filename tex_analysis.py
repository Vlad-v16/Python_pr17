from collections import Counter

class TextStats:
    def __init__(self, text):
        self.text = text

    def count_words(self):
        return len(self.text.split())

    def most_common_letter(self):
        letters = [ch.lower() for ch in self.text if ch.isalpha()]
        if letters:
            return Counter(letters).most_common(1)[0]
        else:
            return None
