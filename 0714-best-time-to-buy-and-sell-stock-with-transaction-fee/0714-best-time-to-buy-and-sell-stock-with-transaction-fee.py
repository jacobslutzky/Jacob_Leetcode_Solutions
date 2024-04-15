class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        max_profit = 0
        max_after_buying = float("-inf")
        for i in range(0, len(prices)):
            max_after_buying = max(max_after_buying, max_profit-prices[i])
            max_profit = max(prices[i]+max_after_buying-fee, max_profit)
            print(max_after_buying)
            print(max_profit)
            print()
        return max_profit