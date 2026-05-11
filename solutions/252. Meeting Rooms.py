# O(nlogn) time, O(1) space
class Solution:
    def canAttend(self, arr):
        if len(arr) <= 1:
            return True
        # Sort in ending time ASC
        arr.sort(key=lambda x:x[1])
        minStart = arr[len(arr)-1][0]
        for i in range(len(arr)-2, -1, -1):
            if minStart < arr[i][1]:
                return False
            minStart = min(minStart, arr[i][0])
        return True
