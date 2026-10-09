# O(N) time, O(N) space
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1, row2, row3 = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        d = dict()
        result = []
        for c in row1:
            d[c] = 1
        for c in row2:
            d[c] = 2
        for c in row3:
            d[c] = 3
        for word in words:
            lowercase = word.lower()
            typable = True
            row = d[lowercase[0]]
            for c in lowercase:
                if d[c] != row:
                    typable = False
                    break
            if typable:
                result.append(word)
        return result
