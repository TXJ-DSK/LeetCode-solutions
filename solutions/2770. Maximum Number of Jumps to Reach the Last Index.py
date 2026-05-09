# DP, O(n^2)
class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n #stores the maximum number of jumps to each index
        dp[0] = 0
        for i in range(n-1):
            for j in range(i+1, n):
                if dp[i] != -1 and abs(nums[i] - nums[j]) <= target:
                    dp[j] = max(dp[j], dp[i]+1)
        return dp[n-1]
