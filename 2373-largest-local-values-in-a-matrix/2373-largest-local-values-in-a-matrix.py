class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        output_grid = [[float("-inf") for col in range(len(grid[0])-2)] for row in range(len(grid)-2)]
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                for r in range(row, row+3):
                    for c in range(col, col+3):
                        output_grid[row][col] = max(output_grid[row][col], grid[r][c])
        return output_grid
            
                
