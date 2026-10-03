# O(logN) time, O(1) space
class Solution:
    def findComplement(self, num: int) -> int:
        pow2 = 1
        result = 0
        while num > 0:
            if num % 2 == 0:
                result += pow2
            pow2 *= 2
            num = num // 2
        return result
