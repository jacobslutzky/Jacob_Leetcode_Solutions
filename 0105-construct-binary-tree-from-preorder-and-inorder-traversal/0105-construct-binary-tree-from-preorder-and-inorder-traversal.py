# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        root = TreeNode(preorder[0])
        leftPreorder = []
        i = 0
        while inorder[i] != preorder[0]:
            i+=1
        i+=1
        root.left = self.buildTree(preorder[1:i], inorder[:i])
        root.right = self.buildTree(preorder[i:], inorder[i:])
        return root