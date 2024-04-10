# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])

        def createTree(node, preorder):
            if not preorder:
                return
            low = 0
            high = len(preorder)
            while low < high:
                mid = low + (high-low)//2
                if preorder[mid] > node.val:
                    high = mid
                else:
                    low = mid+1
            if low > 0:
                node.left = TreeNode(preorder[0])
                createTree(node.left, preorder[1:low])
            if low < len(preorder):
                node.right = TreeNode(preorder[low])
                createTree(node.right, preorder[low+1:])
            
        createTree(root, preorder[1:])
        return root

