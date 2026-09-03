# O(N) time, O(1) space
class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_num = min(nums1)
        if min_num % 2 == 1:
            return True
        for n in nums1:
            if n % 2 == 1:
                return False
        return True
