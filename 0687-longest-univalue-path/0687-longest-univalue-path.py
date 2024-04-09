# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        visited = set()
        def recurse(node):
            if not node:
                return 0
            curr_length = 0
            if node not in visited:
                curr_length = dfs(node)[1]
            max_left_length = recurse(node.left)
            max_right_length = recurse(node.right)
            
            return max(max_left_length, max_right_length, curr_length)
        
        def dfs(node):
            visited.add(node)
            if not node.left and not node.right:
                return 1,0
            if node.left and node.left.val == node.val:
                left_count,max_left_count = dfs(node.left)
            else:
                left_count = 0
                max_left_count=0
            if node.right and node.right.val == node.val:
                right_count,max_right_count = dfs(node.right)
            else:
                right_count = 0
                max_right_count =0

            return max(left_count,right_count)+1, max(left_count+right_count,max_left_count,max_right_count)
        return recurse(root)