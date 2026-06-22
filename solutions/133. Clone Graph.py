# DFS traversal with visited set to avoid duplicate work, O(V + E) Time, O(V) Space
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        node_dict = dict()
        visited = set()
        new_node = Node(node.val)
        node_dict[node.val] = new_node
        def dfs(node, new_node):
            if node.val in visited:
                return
            visited.add(node.val)
            for n in node.neighbors:
                new_neighbor = None
                if n.val not in node_dict:
                    new_neighbor = Node(n.val)
                    node_dict[n.val] = new_neighbor
                else:
                    new_neighbor = node_dict[n.val]
                new_node.neighbors.append(new_neighbor)
                if new_neighbor.val not in visited:
                    dfs(n, new_neighbor)
        
        dfs(node, new_node)
        return new_node
