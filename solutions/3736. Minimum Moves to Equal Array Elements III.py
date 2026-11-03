# O(N) time, O(1) space
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        result = 0
        maxNum = max(nums)
        for n in nums:
            result += (maxNum - n)
        return result
