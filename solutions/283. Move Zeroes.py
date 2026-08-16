# O(N) time, O(1) space
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        idx, zerostart = 0, 0
        while idx < n:
            if nums[idx] != 0:
                nums[idx], nums[zerostart] = nums[zerostart], nums[idx]
                zerostart += 1
            idx += 1
            
