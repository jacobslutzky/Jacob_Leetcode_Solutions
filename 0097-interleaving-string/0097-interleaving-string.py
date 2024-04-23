class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = [[False for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        dp[0][0] = True
        if len(s1) + len(s2) != len(s3):
            return False
        for j in range(1, len(s2)+1):
            dp[0][j] = s2[:j] == s3[:j]
        for i in range(1, len(s1)+1):
            dp[i][0] = s1[:i] == s3[:i]
            
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if dp[i-1][j] and s3[i+j-1] == s1[i-1]:
                    dp[i][j] = True
                if dp[i][j-1] and s3[i+j-1] == s2[j-1]:
                    dp[i][j] = True
        return dp[-1][-1]