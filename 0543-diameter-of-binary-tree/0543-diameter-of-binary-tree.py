# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def get_diameter(root):
            if not root:
                return 0,0

            left_max,left_height = get_diameter(root.left)
            right_max,right_height = get_diameter(root.right)
            print(root.val)
            print(left_height)
            print(right_height)
            print()
            return max(left_max,right_max,left_height+right_height+1), max(left_height,right_height)+1

        return get_diameter(root)[0]-1