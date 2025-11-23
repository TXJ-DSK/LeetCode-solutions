class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = dict()
        for i in range(len(nums)):
            if nums[i] in diffs: # A pair is found
                return [diffs[nums[i]], i]
            else:
                diffs[target - nums[i]] = i
        return [-1, -1]
        
