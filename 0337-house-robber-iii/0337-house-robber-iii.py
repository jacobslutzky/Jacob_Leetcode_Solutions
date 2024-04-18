# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
           
            if not node:
                return 0,0
            
            left = dfs(node.left)
            right = dfs(node.right)

            return max(node.val + left[1] + right[1], left[0] + right[0]), left[0]+right[0]
        
    

        return dfs(root)[0]


            