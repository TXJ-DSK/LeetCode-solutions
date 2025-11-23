class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            return 0
        total_even = 0
        total_odd = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                total_even += nums[i]
            else:
                total_odd += nums[i]
        # sum of even/odd index numbers before index i
        even_front = [0 for _ in range(len(nums))]
        odd_front = [0 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            even_front[i] = even_front[i-1]
            odd_front[i] = odd_front[i-1]
            if i % 2 == 0:
                odd_front[i] += nums[i-1]
            else:
                even_front[i] += nums[i-1]
        #print("even_front",even_front)
        #print("odd_front",odd_front)
        count = 0
        for i in range(0, len(nums)):
            even_sum = even_front[i]
            odd_sum = odd_front[i]
            # alter the sign after i, exclude i when adding
            if i % 2 == 0:
                odd_sum += (total_even - even_front[i] - nums[i])
                even_sum += (total_odd - odd_front[i])
            else:
                even_sum += (total_odd - odd_front[i] - nums[i])
                odd_sum += (total_even - even_front[i])
            if even_sum == odd_sum:
                count += 1
        return count
        
