# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) != len(inorder):
            raise Exception("Invalid tree")
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root = preorder[0]
        idx = inorder.index(root)
        left_sub_in = inorder[:idx]
        right_sub_in = inorder[idx+1:]
        left_sub_pre = preorder[1:1+len(left_sub_in)]
        right_sub_pre = preorder[1+len(left_sub_in):]
        return TreeNode(preorder[0], self.buildTree(left_sub_pre, left_sub_in)
            , self.buildTree(right_sub_pre, right_sub_in))
