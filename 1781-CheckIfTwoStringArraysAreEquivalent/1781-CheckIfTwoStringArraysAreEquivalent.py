# Last updated: 1/2/2026, 12:17:34 PM
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        a = ""
        b = ""
        for s in word1:
            a += s  # Concatenate the strings in word1
        for s in word2:
            b += s  # Concatenate the strings in word2
        return a == b #return the boolean expression
