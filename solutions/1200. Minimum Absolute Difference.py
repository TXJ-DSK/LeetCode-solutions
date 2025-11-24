class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[-1] - arr[0]
        result = []
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                result.clear()
            min_diff = min(min_diff, diff)
            if diff == min_diff:
                result.append([arr[i], arr[i+1]])
        return result
