# O(logN) Time, O(1) Space
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        d_sum = 0
        while n > 0:
            d_sum += n % k
            n = n // k
        return d_sum
