class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")]*(n+1)
        sqrt = int(n**(1/2))
        dp[0] = 0
        for i in range(n+1):
            for j in range(1, sqrt+1):
                square = j**2
                dp[i] = min(dp[i],dp[i-square]+1)
        return dp[-1]

