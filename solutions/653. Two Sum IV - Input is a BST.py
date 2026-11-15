# O(N) time, O(N) space

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        complements = set()
        def dfs(node, comp, k):
            if not node:
                return False
            if node.val in comp:
                return True
            comp.add(k - node.val)
            return dfs(node.left, comp, k) or dfs(node.right, comp, k)
        return dfs(root, complements, k)
