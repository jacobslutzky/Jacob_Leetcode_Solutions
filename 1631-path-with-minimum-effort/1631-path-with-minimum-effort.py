from heapq import heapify, heappush, heappop 

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        pq = []
        heapify(pq)
        
        heappush(pq,(0, 0, 0))
        distances = [[float("inf") for i in row] for row in heights]
        distances[0][0] = 0
        while pq:
            dist, row, col = heappop(pq)
            if row == len(heights)-1 and col == len(heights[0])-1:
                return dist
            for i,j in ((row-1,col),(row+1,col),(row,col-1),(row,col+1)):
                if i < len(heights) and i >= 0 and j < len(heights[0]) and j >= 0:
                    new_dist = max(dist,abs(heights[row][col]-heights[i][j]))
                    if new_dist < distances[i][j]:
                        distances[i][j] = new_dist
                        heappush(pq, (new_dist, i, j))




