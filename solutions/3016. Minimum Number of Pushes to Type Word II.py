# O(N) time, O(1) space, capable of handling non-distinct cases
from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        occurences = list(cnt.items())
        occurences.sort(key= lambda x: x[1], reverse=True)
        cost = 1
        key = 2
        result = 0
        for c, occ in occurences:
            if key == 10:
                cost += 1
                key = 2
            result += cost * occ
            key += 1
        return result
