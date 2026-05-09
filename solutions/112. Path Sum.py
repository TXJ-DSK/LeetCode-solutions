# DFS with iteration, O(n) time and space complexity
# Recursion may result in stack overflow, because maximum tree height = 5000

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        currLevel = [(root, 0)]
        nextLevel = []
        while len(currLevel) > 0:
            for tup in currLevel:
                node = tup[0]
                pathSum = tup[1] + node.val
                if node.left is None and node.right is None:
                    if pathSum == targetSum:
                        return True
                if node.left:
                    nextLevel.append((node.left, pathSum))
                if node.right:
                    nextLevel.append((node.right, pathSum))
            currLevel = nextLevel
            nextLevel = []
        return False
