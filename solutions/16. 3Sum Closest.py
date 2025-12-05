class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        global_min_diff = target - sum(nums[:3])
        for i in range(len(nums)-2):
            jk_target = target - nums[i]
            j, k = i+1, len(nums)-1
            jk_sum = nums[j] + nums[k]
            while(j<k):
                jk_sum = nums[j] + nums[k]
                if jk_sum == jk_target:
                    return target # find a sum that equals target, end early
                elif jk_sum < jk_target:
                    j += 1
                else:
                    k -= 1
                if abs(jk_target - jk_sum) < abs(global_min_diff):
                    global_min_diff = jk_target - jk_sum
        return target - global_min_diff
                    
