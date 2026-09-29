# O(N) time, O(1) space
class Solution:
    def maxDepth(self, s: str) -> int:
        maxd, d = 0, 0
        for c in s:
            if c == '(':
                d += 1
                maxd = max(maxd, d)
            elif c == ')':
                d -= 1
        return maxd
