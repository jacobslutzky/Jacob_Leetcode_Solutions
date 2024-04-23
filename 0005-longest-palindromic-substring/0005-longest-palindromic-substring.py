class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr_max = 0
        n = len(s)
        
        dp = [[False if i < j else True for j in range(n)] for i in range(n)]
        max_len = 0
        max_str = s[0]
        for size in range(1,len(s)):
            for i in range(len(s)-size):
                if dp[i+1][i+size-1] and s[i] == s[i+size]:
                    if size > max_len:
                        max_len = size
                        max_str = s[i:i+size+1]
                    dp[i][i+size] = True
        return max_str

        



        
    
