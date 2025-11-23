class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        arr_sum = sum(nums)
        remainder = arr_sum % p
        if remainder == 0: # the sum of arry is divisible by p
            return 0

        # maintain a dictionary recording the last occurence of remainder of prefix sum
        remainder_last_idx = {0:-1}
        curr_prefix_sum = 0
        min_length = len(nums)

        for index, num in enumerate(nums):
            curr_prefix_sum = (curr_prefix_sum + num) % p
            target_prefix_sum = (curr_prefix_sum - remainder) % p
            # sum of subarray have the same remainder with total array
            if target_prefix_sum in remainder_last_idx:
                subarray_length = index - remainder_last_idx[target_prefix_sum]
                min_length = min(min_length, subarray_length)
            remainder_last_idx[curr_prefix_sum] = index

        return -1 if min_length == len(nums) else min_length
