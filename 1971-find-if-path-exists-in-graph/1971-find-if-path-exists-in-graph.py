class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        visited = [False]*n
        def dfs(node):
            if visited[node]:
                return False

            visited[node] = True
            if node == destination:
                return True
            for adj in graph[node]:
                if dfs(adj):
                    return True
            return False

        
        return dfs(source)