# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = [(root, 1)]
        max_len = 1
        
        while queue:
            len_q = len(queue)

            for i in range(len_q):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left,2*index))
                if node.right:
                    queue.append((node.right,2*index+1))
            if queue:
                max_len = max(max_len, queue[-1][1]-queue[0][1]+1)
        return max_len
