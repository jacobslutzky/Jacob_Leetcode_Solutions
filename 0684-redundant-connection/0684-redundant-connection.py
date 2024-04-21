class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        for x, y in edges:
            if x in graph:
                graph[x].append(y)
            else:
                graph[x] = [y]
            if y in graph:
                graph[y].append(x)
            else:
                graph[y] = [x]
        
        visited = [False]*(len(edges)+1)
        def dfs(node,edge):
            if visited[node]:
                return 0

            visited[node] = True
            count = 0
            for adj in graph[node]:
                if (edge[0] != node or edge[1]!=adj ) and (edge[1] != node or edge[0]!=adj):
                    count += dfs(adj,edge)
                        
            visited[node] = False
            return count +1    

        output_edge = None
        for edge in edges:
            if dfs(1,edge) == len(edges):
                output_edge = edge
        return output_edge


       