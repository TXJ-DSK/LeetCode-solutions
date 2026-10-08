# O(N) time, O(N) space
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        layer = 0
        for c in s:
            if c == '(':
                layer += 1
                if layer > 1:
                    result += c
            else:
                layer -= 1
                if layer > 0:
                    result += c
        return result
