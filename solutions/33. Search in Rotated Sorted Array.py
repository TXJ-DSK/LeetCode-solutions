class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        # find the index of largest element, after rotation
        def findMaxIdx(left,right):
            while left <= right:
                mid = left + (right - left) // 2
                #print(f"left={left},right={right},mid={mid}")
                if mid == len(nums)-1:
                    return mid
                if nums[mid] > nums[mid+1]:
                    return mid
                if nums[mid] < nums[0]:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        left, right = 0, len(nums)-1
        max_idx = findMaxIdx(left,right)
        if target < nums[0]:# in the second part
            left = max_idx+1
        else: # in the first part
            right = max_idx
        if left > right:
            return -1
        def binarySearch(left, right):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        return binarySearch(left, right)
        
    
    
        
