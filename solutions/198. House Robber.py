class Solution:
    # 10 1 1 10
    def rob(self, nums: List[int]) -> int:
        outcome = [nums[0], 0] # [rob, not rob] maximum outcome along the street
        for i in range(1,len(nums)):
            rob_i = nums[i] + outcome[1]
            not_rob_i = max(outcome[0], outcome[1])
            outcome = [rob_i, not_rob_i]
        return max(outcome)
