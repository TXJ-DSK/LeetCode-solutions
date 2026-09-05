# O(N) time, O(N) space
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_fwd = [nums[0]]
        for i in range(1, n):
            max_fwd.append(max(max_fwd[-1], nums[i]))
        min_bwd = [nums[-1]]
        for i in range(n-2,-1,-1):
            min_bwd.append(min(min_bwd[-1], nums[i]))
        min_bwd = min_bwd[::-1]
        for i in range(n):
            if max_fwd[i] - min_bwd[i] <= k:
                return i
        return -1
