# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        output = []
        def traverse(node, curr):
            if not node.left and not node.right:
                output.append(curr)
            if node.left:
                traverse(node.left, curr + "->" + str(node.left.val))
            if node.right:
                traverse(node.right, curr + "->" + str(node.right.val))
        
        traverse(root,str(root.val))
        return output

        