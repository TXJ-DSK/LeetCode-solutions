# sliding window, O(N) time, O(N) space
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = [0] * (n+1)
        suffix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        for i in range(n-1, -1, -1):
            suffix[i] = suffix[i+1] + arr[i]
        # n+1 stands for unable to construct such array at this cutoff idx
        prefix_len = [n+1] * (n+1)
        head, tail = 0, 0
        while head < n+1:
            arrsum = prefix[head] - prefix[tail]
            if arrsum == target:
                prefix_len[head] = head - tail
                head += 1
            elif arrsum < target:
                head += 1
            else:
                tail += 1
        for i in range(1, n+1): # rolling minimum
            prefix_len[i] = min(prefix_len[i], prefix_len[i-1])
        #print(prefix_len)
        
        suffix_len = [n+1] * (n+1)
        head, tail = n, n
        while head > -1:
            arrsum = suffix[head] - suffix[tail]
            if arrsum == target:
                suffix_len[head] = tail - head
                head -= 1
            elif arrsum < target:
                head -= 1
            else:
                tail -= 1
        for i in range(n-1, -1, -1): # rolling minimum
            suffix_len[i] = min(suffix_len[i], suffix_len[i+1])
        #print(suffix_len)
        result = n+1
        for i in range(n+1):
            if prefix_len[i]>0 and suffix_len[i]>0:
                result = min(result, prefix_len[i]+suffix_len[i])
        if result == n+1:
            return -1
        else:
            return result
