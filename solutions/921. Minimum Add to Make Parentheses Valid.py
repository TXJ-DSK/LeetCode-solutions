# 1 swipe, O(N) time, O(1) space
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left, result = 0, 0
        for c in s:
            if c == '(':
                left += 1
            elif c == ')':
                if left > 0:
                    left -= 1
                else:
                    result += 1
        return left + result
