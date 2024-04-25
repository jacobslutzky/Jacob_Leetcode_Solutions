# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def countNodes(maxNode, node):
            if not node:
                return
            if node.val >= maxNode:
                self.count+=1
                maxNode = node.val

            countNodes(maxNode, node.left)
            countNodes(maxNode,node.right)
        countNodes(root.val,root)
        return self.count
