# O(N) time, O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1, max2 = 0, 0
        for n in nums:
            if n > max2:
                max2 = n
                max1, max2 = max(max1, max2), min(max1, max2)
        return (max1 - 1) * (max2 - 1)
