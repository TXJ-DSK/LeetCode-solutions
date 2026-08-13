# O(N) time, O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)
