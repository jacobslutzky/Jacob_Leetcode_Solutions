# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
     # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        left_bad = None
        right_bad = None
        prev = None
        def inorder(node, post):
            if node == None:
                return
            prev = inorder(node.left,)
            inorder(node.right, node)
            if post != None and left_bad == None and node.val > post.val:
                left_bad = node
            elif prev != None and node.val < prev.val:
                right_bad = node
            return node
        inorder(root, None)
        left_bad.val, right_bad.val = right_bad.val, left_bad.val

        


        
        
        


        
        