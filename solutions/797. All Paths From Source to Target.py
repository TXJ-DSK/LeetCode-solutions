class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_paths = self.recursive(graph, 0)
        for path in all_paths:
            path.reverse()
        return all_paths

    def recursive(self, graph, node):
        if node == len(graph) - 1:
            return [[node]]
        result = []
        for child in graph[node]:
            child_paths = self.recursive(graph, child)
            for path in child_paths:
                path.append(node)
                result.append(path)
        return result
