# O(N + logN * Q) Time, O(N) Space
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        disjoints = []
        for i in range(n-1):
            if nums[i+1] - nums[i] > maxDiff:
                disjoints.append(i+0.5)
        if len(disjoints) == 0: # all nodes are connected
            return [True] * len(queries)
        
        result = []
        for n1, n2 in queries:
            nsmall, nbig = min(n1, n2), max(n1, n2)
            found_disjoint = False
            left, right = 0, len(disjoints)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nsmall < disjoints[mid] < nbig:
                    found_disjoint = True
                    break
                if disjoints[mid] < nsmall:
                    left = mid + 1
                elif disjoints[mid] > nbig:
                    right = mid - 1
            result.append(not found_disjoint)
        
        return result
