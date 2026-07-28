# O(N) time, O(N) space
from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        mid = ""
        front = ""
        cnt = Counter(s)
        for i in range(26):
            c = chr(ord('a')+i)
            front += c * (cnt[c] // 2)
            if cnt[c] % 2 == 1:
                mid += c
        return front + mid + front[::-1]
