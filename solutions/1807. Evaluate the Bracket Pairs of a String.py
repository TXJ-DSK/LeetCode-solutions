# O(N) time, O(N) space
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict()
        for key, val in knowledge:
            d[key] = val
        result = ""
        temp = ""
        inBracket = False
        for c in s:
            if c == '(':
                inBracket = True
            elif c == ')':
                inBracket = False
                if temp in d:
                    result += d[temp]
                else:
                    result += '?'
                temp = ""
            elif inBracket:
                temp += c
            else:
                result += c
        return result
