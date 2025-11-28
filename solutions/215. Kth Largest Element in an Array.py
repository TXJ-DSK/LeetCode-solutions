class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        keys = sorted(list(cnt.keys()), reverse = True)
        count = 0
        for key in keys:
            count += cnt[key]
            if count >= k:
                return key
        return -9999
        
