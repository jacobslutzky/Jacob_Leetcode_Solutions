class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        dp = [[0 for  x in range(m+1)] for y in range(n+1)]
        
        for num in strs:
            numOnes = num.count("1")
            numZeros= num.count("0")
            print(numOnes)
            for i in range(n, numOnes-1, -1):
                for j in range(m, numZeros-1, -1):
                    dp[i][j] = max(dp[i-numOnes][j-numZeros] + 1, dp[i][j])
                    
        return dp[-1][-1]
