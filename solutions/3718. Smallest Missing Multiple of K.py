# O(N) time, O(N) space
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        num = k
        while num in num_set:
            num += k
        return num
