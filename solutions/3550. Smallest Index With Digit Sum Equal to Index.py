# O(N) time, O(1) space
class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            dsum = 0
            n = nums[i]
            while n > 0:
                dsum += n % 10
                n = n // 10
            if dsum == i:
                return i
        return -1
