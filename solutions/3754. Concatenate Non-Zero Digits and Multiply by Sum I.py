# O(logN) Time, O(logN) Space
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nonzero = ""
        for c in str(n):
            if c == '0':
                continue
            nonzero += c
        if len(nonzero) == 0:
            return 0
        dsum = 0
        for c in nonzero:
            dsum += int(c)
        return int(nonzero) * dsum
