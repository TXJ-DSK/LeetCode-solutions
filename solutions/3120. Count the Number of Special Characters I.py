# O(N) Time, O(1) Space
from collections import Counter
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = Counter(word)
        result = 0
        for c in cnt:
            if c.islower() and c.upper() in cnt:
                result += 1
        return result
