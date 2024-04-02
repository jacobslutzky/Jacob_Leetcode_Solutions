class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        for row in grid:
            print(row)
        def dfs(row, col):
            if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
                return False
            if grid[row][col] != 0:
                return True
            grid[row][col] = 2
            valid_island = True
            for i, j in [(1,0), (-1,0), (0,1), (0,-1)]:
                if not dfs(row + i, col + j):
                    valid_island = False
            return valid_island
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0 and dfs(row,col):
                    print(str(row) + " " + str(col))
                   
                    count+=1
        return count

