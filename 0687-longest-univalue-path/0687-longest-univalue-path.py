# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        def dfs(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            left_count = 0
            right_count = 0
            if node.left and node.left.val == node.val:
                left_count = dfs(node.left)
            else:
                dfs(node.left)
            if node.right and node.right.val == node.val:
                right_count = dfs(node.right)
            else:
                dfs(node.right)
    

            self.max_length = max(self.max_length, left_count+right_count)
            return max(left_count,right_count)+1
        dfs(root)
        return self.max_length