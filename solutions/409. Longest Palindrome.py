# O(N) time, O(1) space
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        oddCount = 0
        cnt = Counter(s)
        for key in cnt:
            result += cnt[key] // 2
            oddCount += cnt[key] % 2
        if oddCount > 0:
            return result * 2 + 1
        else:
            return result * 2
