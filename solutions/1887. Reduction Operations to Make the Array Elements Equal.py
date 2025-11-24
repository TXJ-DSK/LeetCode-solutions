class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        cnt = Counter(nums)
        key_list = list(cnt.keys())
        if len(key_list) == 1:
            return 0
        key_list.sort(reverse = True)
        result = 0
        accumulative_sum = 0
        for i in range(len(key_list)-1):
            result += accumulative_sum + cnt[key_list[i]]
            accumulative_sum += cnt[key_list[i]]
        return result
        
