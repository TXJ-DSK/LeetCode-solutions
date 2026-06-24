# divide and conquer, O(N) Time, O(N) Space
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        
        def recursive(left, right):
            if left > right:
                return None
            elif left == right:
                return TreeNode(nums[left])
            mid = left + (right - left) // 2
            return TreeNode(nums[mid], recursive(left, mid-1), recursive(mid+1, right))

        return recursive(0, len(nums)-1)
