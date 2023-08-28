class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowPrice = float('inf')
        profit = 0

        for i, a in enumerate(prices):
            lowPrice = min(lowPrice, a)
            profit = max(profit, a - lowPrice)
        
        return profit
  """
  Try to sell everyday
  """

