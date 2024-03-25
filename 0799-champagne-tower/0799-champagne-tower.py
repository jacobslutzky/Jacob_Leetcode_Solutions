class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0]*(row+1) for row in range(query_row+1)]
        dp[0][0] = poured
        for row in range(query_row):
            for glass in range(row+1):
                remainder = 0
                if dp[row][glass] > 1:
                    remainder = (dp[row][glass]-1)/2
                    dp[row][glass] = 1
                    
                dp[row+1][glass] += remainder
                dp[row+1][glass+1] += remainder
        if dp[query_row][query_glass] > 1:
            return 1

        return dp[query_row][query_glass]
               

