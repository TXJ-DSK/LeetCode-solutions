# DFS approach, O(n) time, O(1) space
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
    
    def dfs(self, node1, node2) -> bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        return self.dfs(node1.right, node2.left) and self.dfs(node1.left, node2.right)
