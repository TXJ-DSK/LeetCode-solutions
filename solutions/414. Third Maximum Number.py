# O(N) time, O(N) space
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums = list(set(nums))
        min_int = -1 * (2 ** 32)
        m1, m2, m3 = min_int, min_int, min_int
        for n in nums:
            m3, n = max(m3, n), min(m3, n)
            m2, m3 = max(m2, m3), min(m2, m3)
            m1, m2 = max(m1, m2), min(m1, m2)
        if m3 == min_int:
            return m1
        else:
            return m3
