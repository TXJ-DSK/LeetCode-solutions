import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [sys.maxsize, sys.maxsize] # smallest valid nums[i] and nums[j]
        for i in range(len(nums)):
            if nums[i] < dp[0]:
                dp[0] = nums[i]
            if nums[i] > dp[0] and nums[i] < dp[1]:
                dp[1] = nums[i]
            if nums[i] > dp[1]:
                return True
        return False
