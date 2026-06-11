# O(NlogN) Time, O(N) Space
# No recursion, which can result stack overflow with unbalanced tree
import math
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        for i in range(len(edges)):
            if edges[i][0] > edges[i][1]:
                edges[i][0], edges[i][1] = edges[i][1], edges[i][0]
        edges.sort()
        edge_dict = {1: 0}
        for e in edges:
            edge_dict[e[1]] = edge_dict[e[0]] + 1
        max_depth = max(edge_dict.values())
        result = 1
        for _ in range(max_depth-1):
            result *= 2
            result %= 1000000007
        return result
