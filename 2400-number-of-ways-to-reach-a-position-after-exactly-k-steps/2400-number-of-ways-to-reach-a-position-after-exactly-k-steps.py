class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        
        if k + startPos < endPos:
            return 0
        dp = [[0]*(k+startPos+k) for _ in range(k+1)]
            
        dp[0][k-1+startPos] = 1
        for i in range(1,k+1):
            for j in range(len(dp[0])):
                if j - 1 >= 0:
                    dp[i][j] += dp[i-1][j-1] % (10**9+7)
                if j + 1 < len(dp[0]):
                    dp[i][j] += dp[i-1][j+1] % (10**9+7)
        return dp[k][k-1+endPos] % (10**9+7)