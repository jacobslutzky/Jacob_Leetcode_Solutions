from heapq import heappush, heapify, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for i in range(n)]
        for start, end, weight in flights:
            graph[start].append((end,weight))
        
        heap = []
        distances = [float("inf")]*n
        distances[src] = 0
        heappush(heap, (0, src, 0))

        while heap:
            curr_dist, curr_node, curr_k = heappop(heap)
          
            if curr_node == dst:
                return curr_dist
            for node, weight in graph[curr_node]:
                if curr_k <= k:
                    distances[node] = curr_dist + weight
                    heappush(heap, (curr_dist + weight,node, curr_k+1))
        return -1

        
