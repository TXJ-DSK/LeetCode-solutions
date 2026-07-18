# simple math, O(N) time, O(1) space
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a, b):
            if a <= 1 or b % a == 0:
                return a
            return gcd(b%a, a)
        return gcd(min(nums), max(nums))
