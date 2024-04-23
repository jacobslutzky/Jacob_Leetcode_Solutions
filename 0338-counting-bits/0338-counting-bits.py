class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        
        i = 1
        while i < n+1:
            dp[i] = 1
            i*=2
        for i in range(0,n+1):
            if not dp[i]:
                if i % 2 == 0:
                    dp[i] = dp[i//2]
                else:
                    dp[i] = dp[i//2]+1

        return dp