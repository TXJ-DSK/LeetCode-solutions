# O(N) time, O(1) space
class Solution:
    def checkString(self, s: str) -> bool:
        foundB = False
        for c in s:
            if c == 'b':
                foundB = True
            else:
                if foundB:
                    return False
        return True
