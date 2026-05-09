# BFS approach, O(nlogn) for balanced tree, O(n^2) for single sided tree
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        result = 0
        currLevel = [[root, []]]
        nextLevel = []
        while len(currLevel) > 0:
            for item in currLevel:
                node = item[0]
                pathSums = item[1].copy()
                for i in range(len(pathSums)):
                    pathSums[i] += node.val
                pathSums.append(node.val)
                result += pathSums.count(targetSum)
                if node.left:
                    nextLevel.append([node.left, pathSums])
                if node.right:
                    nextLevel.append([node.right, pathSums])
            
            currLevel = nextLevel
            nextLevel = []
        return result

# Recursive DFS approach, O(n) time and space, may cause stack overflow for single sided tree
import collections
class Solution:
    result = 0
    target = 0
    pathSums = Counter([0])
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        self.result = 0
        self.pathSums = Counter([0])
        self.target = targetSum
        self.dfs(root, 0)
        return self.result
    
    def dfs(self, node, rootPathSum):
        if node is None:
            return
        rootPathSum += node.val
        self.result += self.pathSums[rootPathSum - self.target]
        self.pathSums[rootPathSum] += 1

        self.dfs(node.left, rootPathSum)
        self.dfs(node.right, rootPathSum)
        self.pathSums[rootPathSum] -= 1
