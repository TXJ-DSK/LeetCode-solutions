from collections import Counter
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # O(n^2)
        cnt = Counter(nums)
        arr = sorted(list(cnt.keys()))
        result = []
        for i in range(len(arr)):
            for j in range(len(arr)-1, i-1, -1):
                target = 0 - arr[i] - arr[j]
                if cnt[target] > 0:
                    k = arr.index(target)
                    if k > i and k < j:
                        result.append([arr[i], target, arr[j]])
                    elif k == i and k == j and cnt[target] > 2:
                        result.append([arr[i], target, arr[j]])
                    elif k == i and k != j and cnt[target] > 1:
                        result.append([arr[i], target, arr[j]])
                    elif k == j and k != i and cnt[target] > 1:
                        result.append([arr[i], target, arr[j]])
        return result
