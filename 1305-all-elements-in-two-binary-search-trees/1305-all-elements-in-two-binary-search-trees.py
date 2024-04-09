# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        l1 = inorder(root1)
        l2 = inorder(root2)
        output = []
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] < l2[j]:
                output.append(l1[i])
                i+=1
            else:
                output.append(l2[j])
                j+=1
        return output + l1[i:] + l2[j:]