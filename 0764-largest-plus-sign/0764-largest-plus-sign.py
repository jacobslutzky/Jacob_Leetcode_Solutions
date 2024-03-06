class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1 for col in range(n)] for row in range(n)]
        for mine in mines:
            grid[mine[0]][mine[1]] = 0
        dp_up = [[element for element in row] for row in grid]
        dp_down = [[element for element in row] for row in grid]
        dp_right = [[element for element in row] for row in grid]
        dp_left = [[element for element in row] for row in grid]

        for row in range(1, n):
            for col in range(1, n):
                if grid[row][col]:
                    dp_up[row][col] = dp_up[row-1][col]+1
                    dp_left[row][col] = dp_left[row][col-1]+1
                    
        
        for row in range(n-2,-1,-1):
            for col in range(n-2, -1,-1):
                if grid[row][col]:
                    dp_down[row][col] = dp_down[row+1][col]+1
                    dp_right[row][col] = dp_right[row][col+1]+1
        max_size = 0
        for row in range(n):
            for col in range(n):
                max_size = max(max_size, min(dp_up[row][col], dp_left[row][col],dp_down[row][col],dp_right[row][col] ))
        return max_size
