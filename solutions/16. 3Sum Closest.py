class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        global_min_diff = target - sum(nums[:3])
        for i in range(len(nums)-2):
            jk_target = target - nums[i]
            for j in range(i+1, len(nums)-1):
                k_target = jk_target - nums[j]
                low,high = j+1, len(nums)-1
                k = low
                min_diff = k_target - nums[k]
                while low <= high:
                    mid = low + (high - low) // 2
                    if nums[mid] <= k_target:
                        low = mid + 1
                    else:
                        high = mid - 1
                    if abs(min_diff) > abs(k_target - nums[mid]):
                        k = mid
                        min_diff = k_target - nums[mid]
                if abs(min_diff) < abs(global_min_diff):
                    global_min_diff = min_diff
                    if min_diff == 0:
                        return target # find a sum that equals target, end early
        return target - global_min_diff
                    
