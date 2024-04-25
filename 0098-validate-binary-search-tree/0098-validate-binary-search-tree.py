# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return (not root.left or root.left.val < root.val) and (not root.right or root.right.val > root.val) \
         and self.isValidBST(root.left) and self.isValidBST(root.right)