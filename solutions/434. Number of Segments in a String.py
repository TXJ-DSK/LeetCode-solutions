# O(N) time, O(1) space
class Solution:
    def countSegments(self, s: str) -> int:
        result = 0
        prevSpace = True
        for i in range(len(s)):
            if s[i] == ' ':
                prevSpace = True
            else:
                if prevSpace:
                    result += 1
                    prevSpace = False
        return result
