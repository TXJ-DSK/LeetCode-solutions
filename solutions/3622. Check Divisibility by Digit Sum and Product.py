# O(logN) time, O(1) space
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        d_sum = 0
        d_product = 1
        num = n
        while num > 0:
            d = num % 10
            d_sum += d
            d_product *= d
            num = num // 10
        return n % (d_sum + d_product) == 0
