# O(N) time, O(1) space
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = Counter(t) - Counter(s)
        return list(diff.elements())[0]
