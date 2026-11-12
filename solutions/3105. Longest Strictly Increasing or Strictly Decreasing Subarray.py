# O(N) time, O(1) space
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxAsc, maxDesc = 1, 1
        currAsc, currDesc = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                currAsc += 1
                currDesc = 1
                maxAsc = max(maxAsc, currAsc)
            elif nums[i] < nums[i-1]:
                currAsc = 1
                currDesc += 1
                maxDesc = max(maxDesc, currDesc)
            else:
                currAsc, currDesc = 1, 1
        return max(maxAsc, maxDesc)
