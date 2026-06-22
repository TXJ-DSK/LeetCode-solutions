# O(N) Time, O(1) Space (only 26 chars)
from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        return min(cnt['b'], cnt['a'], cnt['l']//2, cnt['o']//2, cnt['n'])
                
