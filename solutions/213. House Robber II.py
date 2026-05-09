class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        # rob first building
        outcome = [nums[0], 0]
        for i in range(1, len(nums)):
            rob_i = nums[i] + outcome[1]
            not_rob_i = max(outcome)
            outcome = [rob_i, not_rob_i]
        result_rob_first = outcome[1]
        # not rob first building
        outcome = [0, 0]
        for i in range(1, len(nums)):
            rob_i = nums[i] + outcome[1]
            not_rob_i = max(outcome)
            outcome = [rob_i, not_rob_i]
        result_not_rob_first = max(outcome)
        return max(result_rob_first, result_not_rob_first)
