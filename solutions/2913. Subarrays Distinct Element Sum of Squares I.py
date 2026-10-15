# O(N^2) time, O(N) space
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            s = set()
            for j in range(i, n):
                s.add(nums[j])
                result += (len(s) * len(s))
        return result
