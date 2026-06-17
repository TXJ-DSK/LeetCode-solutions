# O(logN) Time
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        elif n == 1:
            return x
        elif n < 0:
            return 1.0 / self.myPow(x, -1 * n)
        
        half = self.myPow(x, n//2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x
  
