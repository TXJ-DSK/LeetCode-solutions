class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefixCount = 1
        prefixSum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                prefixCount += 1
                prefixSum += nums[i]
            else:
                break
        numSet = set(nums)
        for i in range(prefixSum, 2501):
            if i not in numSet:
                return i
        return 2501
