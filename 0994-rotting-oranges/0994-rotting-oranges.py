class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        num_fresh = 0
        num_rotten = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    num_fresh += 1
                if grid[row][col] == 2:
                    queue.append((row,col))
        minutes = 0
        while queue:
            if num_fresh == 0:
                    return minutes
            for _ in range(len(queue)):
                row,col = queue.pop(0)
                for i,j in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if row+i < len(grid) and row+i >= 0 and col+j < len(grid[0]) and col+j>=0 and grid[row+i][col+j] == 1:
                        grid[row+i][col+j] = 2
                        num_fresh-=1
                        queue.append((row+i,col+j))
            minutes+=1
        return -1
        
       