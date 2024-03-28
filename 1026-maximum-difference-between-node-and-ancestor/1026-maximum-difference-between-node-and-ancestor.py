# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def recurse(node):
        
            if not node.left and not node.right:
                return node.val, node.val, 0
            
            if node.left:
                left_min, left_max, left_v = recurse(node.left)
            else:
                left_min, left_max, left_v = float("inf"),-float("inf"), 0
            
            if node.right:
                right_min, right_max, right_v = recurse(node.right)
            else:
                right_min, right_max, right_v = float("inf"),-float("inf"), 0
            
            curr_min = min(left_min,right_min)
            curr_max = max(left_max,right_max)
            curr_v = max(left_v,right_v, abs(node.val-curr_min),abs(node.val-curr_max))

            return min(curr_min, node.val), max(curr_max, node.val), curr_v
            


            

        return recurse(root)[2]