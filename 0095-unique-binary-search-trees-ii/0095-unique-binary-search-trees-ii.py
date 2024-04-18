# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def recurse(start,end):
            trees = []
            if start == end:
                return [None]

            for i in range(start, end):
                left_subtrees = recurse(start,i)
                right_subtrees = recurse(i+1,end)
                for left in left_subtrees:
                    for right in right_subtrees:
                        trees.append(TreeNode(i,left=left,right=right))
            
            return trees
        return recurse(1, n+1)

            
            
