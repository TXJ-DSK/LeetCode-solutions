import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c <= 2:
            return True
        # let a <= b
        # maximum of b, b^2 < c
        max_b = math.floor(math.sqrt(c))
        a, b = 0, max_b
        while a <= b:
            result = a*a + b*b
            if result == c:
                return True
            if result < c:
                a += 1
            else:
                b -= 1
        return False
                
        
