class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1
        def findMaxIdx(nums, left, right):
            mid = left + (right - left) // 2
            if (mid+1 == len(nums) or nums[mid] > nums[mid+1]) and (mid==0 or nums[mid] > nums[mid-1]):
                return mid
            if nums[mid] >= nums[left]:
                return findMaxIdx(nums, mid+1, right)
            else:
                return findMaxIdx(nums, left, mid-1)
        maxIdx = findMaxIdx(nums, 0, len(nums)-1)
        lower, higher = -1, -1
        if target >= nums[0]:
            lower = 0
            higher = maxIdx
        else:
            lower = maxIdx+1
            higher = len(nums) -1
        def binarySearch(nums, left, right, target):
            if right < left:
                return -1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return binarySearch(nums, mid + 1, right, target)
            else:
                return binarySearch(nums, left, mid - 1, target)
        return binarySearch(nums, lower, higher, target)
