import math
class Solution:
    def myAtoi(self, s: str) -> int:
        lowerbound = int(-1 * math.pow(2, 31))
        upperbound = int(math.pow(2, 31) - 1)
        isPos = True
        result = 0
        s = s.strip()
        if len(s) == 0:
            return 0
        
        if s[0] == '-':
            isPos = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        
        for c in s:
            if not c.isdigit():
                break
            result *= 10
            result += int(c)
        
        if isPos:
            return min(result, upperbound)
        else:
            return max(-1 * result, lowerbound)
        
