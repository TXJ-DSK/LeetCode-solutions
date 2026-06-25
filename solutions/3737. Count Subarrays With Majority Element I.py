# brute force, O(N^2) Time, O(1) Space
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = 0
        for start in range(n):
            count = 0
            for i in range(start, n):
                if nums[i] == target:
                    count += 1
                else:
                    count -= 1
                if count > 0:
                    result += 1
        return result
