# O(logN) time, O(1) space
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n+10):
            if i % 10 == 0:
                return i
            product = i % 10
            num = i // 10
            while num > 0:
                product *= (num%10)
                num = num // 10
            if product % t == 0:
                return i
        return -1
