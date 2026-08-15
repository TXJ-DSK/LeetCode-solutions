# O(N) time, O(1) space
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        all_xor_result = 0
        existNonZero = False
        for i in nums:
            if i != 0:
                existNonZero = True
            all_xor_result = all_xor_result ^ i
        if all_xor_result != 0:
            return len(nums)
        if existNonZero:
            return len(nums) - 1
        return 0
