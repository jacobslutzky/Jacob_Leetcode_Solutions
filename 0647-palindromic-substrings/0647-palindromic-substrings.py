class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]

        for i in range(len(s)):
            dp[i][i] = True
        count = len(s)


        for size in range(1,len(s)):
            for i in range(0, len(s)-size):
                if (size <= 2 or dp[i+1][i+size-1]) and s[i] == s[i+size]:
                    dp[i][i+size] = True
                    count+=1
        return count