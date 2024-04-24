import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for source, target, time in times:
            if source in graph:
                graph[source].append((-time,target))
            else:
                graph[source] = [(-time,target)]

        heap = [(0,k)]
        min_dists = [float("inf")]*(n+1)
        min_dists[k] = 0
        min_dists[0] = 0
        while heap:
            curr_time, node = heappop(heap)
            if node in graph:
                for adj_time, adj in graph[node]:
                    if abs(curr_time + adj_time) < min_dists[adj]:
                        min_dists[adj] = abs(curr_time + adj_time)
                        heappush(heap, (curr_time + adj_time,adj))
        
        if max(min_dists)==float("inf"):
            return -1
        return max(min_dists)
            




