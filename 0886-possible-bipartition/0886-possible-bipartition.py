class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for _ in range(n+1)]
        colors = [-1]*(n+1)
        
        for person, disliked in dislikes:
            adj[person].append(disliked)
            adj[disliked].append(person)
        

        def dfs(node, color):
            
            colors[node] = color

            for nbr in adj[node]:
                if colors[nbr] == colors[node] or (colors[nbr] == -1 and not dfs(nbr, not color)):
                    return False
            return True


        for i in range(1, n+1):
            if colors[i] == -1 and not dfs(i, 0):
                return False

        return True