# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        def generate_inorder(node):
            if not node:
                return []
            return generate_inorder(node.left) + [node.val] + generate_inorder(node.right)
        self.output = [float('-inf')] + generate_inorder(root)
        self.index = 0

    def next(self) -> int:
        self.index+=1
        return self.output[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.output)-1
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()