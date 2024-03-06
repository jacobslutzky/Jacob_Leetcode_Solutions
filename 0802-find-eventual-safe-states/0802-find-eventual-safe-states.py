class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        valid = [0]*len(graph)
        visited = [0]*len(graph)
        def dfs(node):
            if valid[node] == -1:
                return False
            if visited[node]:
                valid[node] = -1
                return False
            if valid[node] == 1:
                return True
            visited[node] = 1
            for adj in graph[node]:
                if not dfs(adj):
                    valid[node] = -1
                    return False
            valid[node] = 1
            visited[node] = 0
            return True

        for node in range(len(graph)):
            dfs(node)
        
        return [n for n in range(len(valid)) if valid[n]==1 ]