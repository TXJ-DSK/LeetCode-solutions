# Create a directed graph for all adjacent neighbors, use dfs for query
# O(E) Time creating graph, O(E * N) Time querying where N is the number of queries, O(V) Space

class Node:
    def __init__(self, value: str):
        self.value = value
        self.neighbors = {value: 1.0}
    
    def __str__(self):
        return "value="+self.value+" neighbors="+str(self.neighbors)
    
    def __repr__(self):
        return self.__str__()

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variables = dict()  # map varible str to node
        for i in range(len(equations)):
            v1, v2 = equations[i]
            if v1 not in variables:
                variables[v1] = Node(v1)
            if v2 not in variables:
                variables[v2] = Node(v2)
            v1_neighbors = variables[v1].neighbors
            v2_neighbors = variables[v2].neighbors
            v1_neighbors[v2] = values[i]
            v2_neighbors[v1] = 1/values[i]
        #print(variables)
        def dfs(node, target, path):
            if node in path:
                return -1.0
            path.append(node)
            if node == target:
                result = 1.0
                for i in range(len(path)-1):
                    result *= variables[path[i]].neighbors[path[i+1]]
                return result
            node_neighbors = variables[node].neighbors
            for n in node_neighbors:
                result = dfs(n, target, path.copy())
                if result != -1.0:
                    return result
            return -1.0
        return [dfs(v1, v2, []) if v1 in variables else -1.0 for v1, v2 in queries]
