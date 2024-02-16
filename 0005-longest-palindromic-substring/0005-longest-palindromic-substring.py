class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr_max = 0
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            curr_string = s[i]
        
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):
                if s[start] == s[end]:
                    if end-start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if end-start+1 > curr_max:
                            curr_max = end-start+1
                            curr_string = s[start:end+1]
        return curr_string

        



        
    
