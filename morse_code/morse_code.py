# Author: Camby Abell
# Filename: morse_code.py
# URL: https://leetcode.com/problems/unique-morse-code-words/

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        morse_word = ""
        morse_words = []
        code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
                "....", "..", ".---", "-.-", ".-..", "--", "-.",
                "---", ".--.", "--.-", ".-.", "...", "-", "..-",
                "...-", ".--", "-..-", "-.--", "--.."]

        for word in words:
            for letter in word:
                value = ord(letter) - 97
                temp = code[value]
                morse_word = morse_word + temp
            morse_words.append(morse_word)
            morse_word = ""

        for item in morse_words:
            print(item)

        return len(set(morse_words))


if __name__  == "__main__":
    Solution.uniqueMorseRepresentations(Solution, ["gin", "zen", "gig", "msg"])
