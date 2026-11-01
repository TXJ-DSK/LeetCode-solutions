# O(N) time, O(1) space
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minNum = min(nums)
        result = 0
        for n in nums:
            result += (n - minNum)
        return result
