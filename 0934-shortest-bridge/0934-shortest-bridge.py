class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = []
        starting_row = -1
        starting_col = -1
        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col] == 1:
                    starting_row = row
                    starting_col = col
                    queue.append((row,col))
                    break
            if queue:
                break
        while queue:
            row, col = queue.pop(0)
            grid[row][col] = 2
            if row+ 1 < len(grid) and grid[row+1][col]==1:
                queue.append((row+1,col))
            if row- 1 >=0 and grid[row-1][col]==1:
                queue.append((row-1,col))
            if col+ 1 < len(grid) and grid[row][col+1]==1 :
                queue.append((row,col+1))
            if col- 1 >= 0 and grid[row][col-1]==1:
                queue.append((row,col-1))
        visited = [[0 for element in row] for row in grid]
        queue = [(starting_row,starting_col,0)]
        min_count = float("inf")
        while queue:
            row, col,count = queue.pop(0)
            visited[row][col] = 1
            if grid[row][col] == 1:
                min_count = min(min_count,count)
            else:
                adder = int(grid[row][col]==0)
                if row+ 1 < len(grid) and not visited[row+1][col]:
                    queue.append((row+1,col,count+adder))
                if row- 1 >=0 and not visited[row-1][col]:
                    queue.append((row-1,col,count+adder))
                if col+ 1 < len(grid) and not visited[row][col+1]:
                    queue.append((row,col+1,count+adder))
                if col- 1 >= 0 and not visited[row][col-1]:
                    queue.append((row,col-1,count+adder))
        return min_count