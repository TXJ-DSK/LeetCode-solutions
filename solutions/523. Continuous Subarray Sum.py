import itertools
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if len(nums) == 2:
            return sum(nums) % k == 0
        prefixes = list(itertools.accumulate(nums))
        mod_pre = [p % k for p in prefixes]
        if 0 in mod_pre[1:]:
            return True
        
        #print(f"prefixes={prefixes}")
        #print(f"mod_pre={mod_pre}")
        mod_dict = dict()
        for i in range(len(nums)):
            if mod_pre[i] not in mod_dict:
                mod_dict[mod_pre[i]] = i
            else:
                if i - mod_dict[mod_pre[i]] >= 2:
                    return True
        return False
