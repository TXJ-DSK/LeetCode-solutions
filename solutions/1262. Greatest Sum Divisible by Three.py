# DP, O(n) time, O(1) space
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0] # maximum sum with remainder 0, 1, 2
        for num in nums:
            remainder = num % 3
            newdp = [0, 0, 0]
            for i in range(3):
                if dp[i] == 0:
                    continue
                # add num to existing path
                newdp[(i+remainder)%3] = max(dp[(i+remainder)%3], dp[i] + num) 
                # not add num
                newdp[i] = max(newdp[i], dp[i])
            # start a new path
            newdp[remainder] = max(newdp[remainder], num)
            dp = newdp
        return dp[0]
