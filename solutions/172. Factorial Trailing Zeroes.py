# O(logN) Time, O(1) Space
class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        fivepow = 5
        while fivepow <= n:
            result += n // fivepow
            fivepow *= 5
        return result
