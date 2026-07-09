# O(N + Q) Time, O(N) Space, where N is the number of nodes, Q is the number of queries
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent_nodes = [0] * n
        for i in range(1, n):
            if nums[i] - nums[i-1] > maxDiff:
                parent_nodes[i] = i
            else:
                parent_nodes[i] = parent_nodes[i-1]
        
        return [parent_nodes[n1] == parent_nodes[n2] for n1, n2 in queries]
