class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [0]*len(isConnected[0])
        count_provinces = 0
        def dfs(node):
            visited[node] = 1
            for i in range(len(isConnected[0])):
                if i != node and not visited[i] and isConnected[node][i]:
                    dfs(i)
        
        
        for node in range(len(isConnected)):
            if visited[node] == 0:
                dfs(node)
                count_provinces += 1
        return count_provinces
        
        