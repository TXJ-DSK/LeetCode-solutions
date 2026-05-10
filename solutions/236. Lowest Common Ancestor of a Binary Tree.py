# DFS, O(n) time

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        foundp, foundq, ans = self.dfs(root, p.val, q.val)
        return ans
    
    def dfs(self, node, pval, qval):
        if not node:
            return False, False, None
        foundp, foundq = False, False
        if node.val == pval:
            foundp = True
        elif node.val == qval:
            foundq = True
        leftp, leftq, leftans = self.dfs(node.left, pval, qval)
        rightp, rightq, rightans = self.dfs(node.right, pval, qval)
        if leftans:
            return True, True, leftans
        elif rightans:
            return True, True, rightans
        foundp = foundp or leftp or rightp
        foundq = foundq or leftq or rightq
        if foundp and foundq:
            return True, True, node
        else:
            return foundp, foundq, None
