class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_max = 0
        curr_low = float("inf")
        for price in prices:
            curr_low = min(curr_low,price)
            curr_max = max(curr_max, price-curr_low)
        return curr_max
