# O(N) Time, O(1) Space
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right = sum(nums)
        left = 0
        result = []
        for i in range(len(nums)):
            right -= nums[i]
            result.append(abs(left - right))
            left += nums[i]
        return result
            
