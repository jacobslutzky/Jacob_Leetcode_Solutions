# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def rev_inorder(node, curr_sum):
            if not node:
                return curr_sum
            
            right_sum = rev_inorder(node.right, curr_sum)
            
            node.val += right_sum

            left_sum = rev_inorder(node.left, node.val)

            return left_sum

        rev_inorder(root, 0)
        return root