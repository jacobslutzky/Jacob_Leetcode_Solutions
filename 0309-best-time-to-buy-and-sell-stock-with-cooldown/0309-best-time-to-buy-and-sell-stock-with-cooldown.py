class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0,0,0] for i in range(len(prices))]
       
        dp[0][0] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][2] = max(dp[i-1][1],dp[i-1][2])
            dp[i][1] = dp[i-1][0] + prices[i]
            dp[i][0] = max(dp[i-1][2]-prices[i], dp[i-1][0])
            
        print(dp)
        return max(max(dp[-1]),0)

