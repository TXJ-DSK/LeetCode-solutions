# DFS with iteration, O(N) time and space
# Recursion may result in stack overflow, because max height = 5000
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        results = []
        currLevel = [[root, 0, []]]
        nextLevel = []
        while len(currLevel) > 0:
            for item in currLevel:
                node = item[0]
                pathSum = item[1] + node.val
                path = item[2].copy()
                path.append(node.val)
                if node.left is None and node.right is None and pathSum == targetSum:
                    results.append(path)
                if node.left:
                    nextLevel.append([node.left, pathSum, path])
                if node.right:
                    nextLevel.append([node.right, pathSum, path])
            currLevel = nextLevel
            nextLevel = []
        return results
        
