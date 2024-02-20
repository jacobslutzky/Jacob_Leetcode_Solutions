class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[elem for elem in row] for row in triangle]

        for row in range(len(triangle)-2,-1,-1):
            for col in range(len(triangle[row])):
                dp[row][col] += min(dp[row+1][col],dp[row+1][col+1])
        return dp[0][0]


