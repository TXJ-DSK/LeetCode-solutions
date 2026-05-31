# O(N) time, O(1) space
class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = 10000000
        for i in range(len(nums)):
            num = nums[i]
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num = num // 10
            min_sum = min(min_sum, digit_sum)
        return min_sum
