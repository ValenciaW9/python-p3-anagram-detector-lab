class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        result = []
        for word in word_list:
            if sorted(word.lower()) == sorted(self.word.lower()) and word.lower() != self.word.lower():
                result.append(word)
        return result