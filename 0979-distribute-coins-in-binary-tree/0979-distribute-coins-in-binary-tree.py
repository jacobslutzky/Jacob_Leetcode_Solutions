# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.total_moves = 0
        
        def moveCoins(node):
            if not node:
                return 0
            left_coins =  moveCoins(node.left)
            right_coins =  moveCoins(node.right)
            self.total_moves += abs(left_coins)+abs(right_coins)
            
            
            return node.val-1 + left_coins+right_coins

        moveCoins(root)
        return self.total_moves