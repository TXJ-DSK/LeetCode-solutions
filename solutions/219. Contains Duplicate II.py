class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        num_idx = dict()
        for i in range(len(nums)):
            if nums[i] in num_idx:
                j = num_idx[nums[i]][-1]
                if j + k >= i:
                    return True
                num_idx[nums[i]].append(i)
            else:
                num_idx[nums[i]] = [i]
        return False
        
