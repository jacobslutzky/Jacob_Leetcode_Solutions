class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for day in range(days[-1]+1)]
        dp[0] = 0
        i = 0
        for day in range(1, days[-1]+1):
            if days[i] != day:
                dp[day] = dp[day-1]
            else:
                i+=1
                dp[day] = dp[day-1] + costs[0]
                if day > 7:
                    dp[day] = min(dp[day],costs[1] + dp[day-7])
                else:
                    dp[day] = min(dp[day],costs[1])
                if day > 30:
                    dp[day] = min(dp[day],costs[2] + dp[day-30])
                else:
                    dp[day] = min(dp[day],costs[2])
        return dp[-1]