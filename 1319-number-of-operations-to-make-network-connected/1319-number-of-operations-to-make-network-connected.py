class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        if len(connections) < n-1:
            return -1
        for x,y in connections:
            graph[x].append(y)
            graph[y].append(x)

        visited = [0]*n
        def dfs(node):
            if visited[node]:
                return
            visited[node] = 1
            for adj in graph[node]:
                dfs(adj)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count+=1
        return count-1
