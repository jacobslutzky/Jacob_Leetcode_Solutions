class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        dp = [[0 for col in row] for row in grid]


        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                dp[row][col] = grid[row][col]
                if row > 0 and col > 0:
                    dp[row][col] += min(dp[row-1][col], dp[row][col-1])
                elif col > 0:
                    dp[row][col] += dp[row][col-1]
                elif row > 0:
                    dp[row][col] += dp[row-1][col]
    
        return dp[-1][-1]
