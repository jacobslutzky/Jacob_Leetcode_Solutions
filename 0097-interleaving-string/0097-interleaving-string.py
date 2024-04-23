class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False for j in range(len(s1)+1)] for i in range(len(s2)+1)]
        dp[0][0] = True
        if len(s1) + len(s2) != len(s3):
            return False
        for j in range(1, len(s1)+1):
            dp[0][j] = s1[:j] == s3[:j]
        for i in range(1, len(s2)+1):
            dp[i][0] = s2[:i] == s3[:i]
        
        for i in range(1, len(s2)+1):
            for j in range(1, len(s1)+1):
                if s2[i-1] == s3[i+j-1]:
                    dp[i][j] = dp[i-1][j]
                if not dp[i][j] and s1[j-1] == s3[i+j-1]:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]

