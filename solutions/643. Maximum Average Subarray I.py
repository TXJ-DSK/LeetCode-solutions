# O(N) time, O(1) space
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        currSum = sum(nums[0:k])
        maxSum = currSum
        for i in range(k, len(nums)):
            currSum -= nums[i - k]
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum/k
