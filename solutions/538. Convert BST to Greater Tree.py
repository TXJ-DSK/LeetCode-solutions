# DFS

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        allVals = []
        self.dfs(root, allVals)
        sortedVals = sorted(allVals, reverse=True)
        cumulative = 0
        newVals = dict()
        for num in sortedVals:
            cumulative += num
            newVals[num] = cumulative
        self.updateDfs(root, newVals)
        return root
    
    def dfs(self, node, valSet):
        valSet.append(node.val)
        if node.left:
            self.dfs(node.left, valSet)
        if node.right:
            self.dfs(node.right, valSet)
    
    def updateDfs(self, node, mapping):
        node.val = mapping[node.val]
        if node.left:
            self.updateDfs(node.left, mapping)
        if node.right:
            self.updateDfs(node.right, mapping)
        
