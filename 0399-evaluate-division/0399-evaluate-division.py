class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for i in range(len(equations)):
            x = equations[i][0]
            y = equations[i][1]
            val = values[i]
            if x in graph:
                graph[x].append((y,val))
            else:
                graph[x] = [(y,val)]
            if y in graph:
                graph[y].append((x,1/val))
            else:
                graph[y] = [(x,1/val)]

        visited = set()
        def dfs(x,y, curr_val):
            if x == y:
                return curr_val
            if x in visited:
                return -1
            visited.add(x)
            if x in graph:
                for adj, val in graph[x]:
                    output_val = dfs(adj, y, curr_val*val)
                    if output_val != -1:
                        visited.remove(x)
                        return output_val
            visited.remove(x)
            return -1
            
        
        output = []
        for x,y in queries:
            if x not in graph or y not in graph:
                output.append(-1)
            elif x == y:
                output.append(1)
            else:
                output.append(dfs(x,y,1))
        return output