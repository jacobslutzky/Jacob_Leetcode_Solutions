# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def check_equal(node,sub_node):
            if not node and not sub_node:
                return True
            if not node or not sub_node:
                return False
            return node.val == sub_node.val and check_equal(node.left,sub_node.left) and check_equal(node.right,sub_node.right)
        return check_equal(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            