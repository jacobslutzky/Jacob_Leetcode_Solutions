class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        dp = [["" for _ in range(len(str2)+1)] for i in range(len(str1)+1)]

        for i in range(1, len(str1)+1):
            for j in range(1, len(str2)+1):
                if len(dp[i-1][j]) >= len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
                
                if str1[i-1] == str2[j-1]:
                    if len(dp[i-1][j-1])+1 > len(dp[i][j]):
                        dp[i][j] = dp[i-1][j-1]+str1[i-1]
        lcs = dp[-1][-1]
        i = 0
        j = 0
        output = ""
        for char in lcs:
            while str1[i] != char:
                output += str1[i]
                i+=1
            while str2[j] != char:
                output += str2[j]
                j+=1
            output+=char
            i+=1
            j+=1
        output += str1[i:] + str2[j:]
        return output
