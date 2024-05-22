class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        for idx, price in enumerate(prices):
            diff = max(prices[idx + 1:], default=0) - price
            if diff > profit:
                profit = diff
        return profit
