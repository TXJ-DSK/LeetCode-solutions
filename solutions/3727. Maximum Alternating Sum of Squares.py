# O(NlogN) time, O(N) space
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = sorted([abs(num) for num in nums], reverse=True)
        mid = (len(nums) + 1) // 2
        result = 0
        for num in nums[:mid]:
            result += num * num
        for num in nums[mid:]:
            result -= num * num
        return result
