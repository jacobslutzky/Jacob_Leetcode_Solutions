# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        output = []
        def dfs(node, curr):
            if not node.left and not node.right:
                output.append(chr(node.val+97)+ curr)
                return
            if node.left:
                dfs(node.left, chr(node.val+97) + curr)
            if node.right:
                dfs(node.right, chr(node.val+97) + curr)

        
        dfs(root, "")
        return min(output)

                