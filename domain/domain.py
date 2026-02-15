import random
import copy

class ScrambleGame:
    def __init__(self, sentence):
        self.original = sentence.split()
        self.scrambled = self.scrambleWords(self.original)
        self.history = []
        self.score = 15

    def scrambleWord(self, word):
        if len(word) <= 3:
            return word
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + "".join(middle) + word[-1]

    def scrambleWords(self, words):
        new_sentence = []
        for w in words:
            scrambled = self.scrambleWord(w)
            new_sentence.append(scrambled)
        return new_sentence

    def swap(self, wi1, li1, wi2, li2):
        # Validate word indices
        if wi1 < 0 or wi1 >= len(self.scrambled) or wi2 < 0 or wi2 >= len(self.scrambled):
            print("Invalid word index.")
            return False

        # Prevent using end letters
        w1 = self.scrambled[wi1]
        w2 = self.scrambled[wi2]

        if li1 <= 0 or li1 >= len(w1) - 1:
            print("Cannot swap first or last letter of a word.")
            return False
        if li2 <= 0 or li2 >= len(w2) - 1:
            print("Cannot swap first or last letter of a word.")
            return False

        # STORE HISTORY (for undo)
        self.history.append(copy.deepcopy(self.scrambled))

        # Case 1: swapping inside the same word
        if wi1 == wi2:
            chars = list(self.scrambled[wi1])
            chars[li1], chars[li2] = chars[li2], chars[li1]
            self.scrambled[wi1] = "".join(chars)

        # Case 2: swapping across two different words
        else:
            w1_list = list(self.scrambled[wi1])
            w2_list = list(self.scrambled[wi2])
            w1_list[li1], w2_list[li2] = w2_list[li2], w1_list[li1]
            self.scrambled[wi1] = "".join(w1_list)
            self.scrambled[wi2] = "".join(w2_list)

        self.score -= 1
        return True

    def undo(self):
        if not self.history:
            print("Nothing to undo!")
            return
        self.scrambled = self.history.pop()

    def is_solved(self):
        return self.scrambled == self.original