# O(N) time, O(1) space
class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        result = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
                result = max(result, current)
            else:
                current = 1
        return result
