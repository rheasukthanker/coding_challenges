#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0 
        for p in prices[1:]:
            if p<buy_price:
                buy_price = p
            profit = max(profit, p-buy_price)
        return profit
