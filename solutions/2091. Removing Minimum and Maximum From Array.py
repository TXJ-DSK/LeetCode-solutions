# O(N) time, O(1) space
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_val, max_val = 999999, -999999
        min_pos, max_pos = -1, -1
        n = len(nums)
        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
                min_pos = i
            if nums[i] > max_val:
                max_val = nums[i]
                max_pos = i
        pos_left, pos_right = min(min_pos, max_pos), max(min_pos, max_pos)
        return min(pos_right+1, n-pos_left, pos_left+1+n-pos_right)
