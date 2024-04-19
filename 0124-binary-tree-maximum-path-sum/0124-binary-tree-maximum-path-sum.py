# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def get_sum(node):
            if not node:
                return float('-inf'),float("-inf")
       
            left_side_path, left_max_path = get_sum(node.left)
            right_side_path, right_max_path = get_sum(node.right)
            
            curr_path = max(left_side_path + node.val,right_side_path+node.val,node.val)
            max_path = max(left_side_path + right_side_path + node.val, curr_path, left_max_path, right_max_path,node.val)
           
            return curr_path, max_path
        return get_sum(root)[1]

            