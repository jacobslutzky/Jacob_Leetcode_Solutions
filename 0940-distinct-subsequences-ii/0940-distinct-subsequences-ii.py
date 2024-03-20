class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0]*(n+1)
        dp[0]=1
        last_occurrences = {}

        for i in range(1,n+1):
            dp[i] = dp[i-1]*2
            if s[i-1] in last_occurrences:
                dp[i] -= dp[last_occurrences[s[i-1]]-1]
            last_occurrences[s[i-1]] = i
        
        return (dp[-1]-1) %(10**9+7)
