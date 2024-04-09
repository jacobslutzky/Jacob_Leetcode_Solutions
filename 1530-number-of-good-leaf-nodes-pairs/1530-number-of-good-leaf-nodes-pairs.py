# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        nodes = {}
        leaf_nodes = []
        def build_graph(node, parent):
            nodes[node] = []
            for adj in [parent, node.left,node.right]:
                if adj != None:
                    nodes[node].append(adj)

            if node.left:
                build_graph(node.left, node)
            if node.right:
                build_graph(node.right, node)
            if not node.left and not node.right:
                leaf_nodes.append(node)
        build_graph(root, None)
        count = [0]
        def dfs(node, curr_dist,prev):
            if curr_dist >= distance:
                return
            for adj in nodes[node]:
                if adj != prev:
                    if len(nodes[adj]) == 1:
                        count[0]+=1
                    dfs(adj, curr_dist+1,node)

        for node in leaf_nodes:
            dfs(node, 0, None)
        return count[0]//2


        



