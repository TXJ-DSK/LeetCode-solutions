# O(logN) Time, O(1) Space
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        result = [0, 0]

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] >= target:
                result[0] = mid
                right = mid - 1
            else:
                left = mid + 1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] <= target:
                result[1] = mid
                left = mid + 1
            else:
                right = mid - 1
        
        if nums[result[0]] == target and nums[result[1]] == target:
            return result
        else:
            return [-1, -1]
        
