class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices)==1:
            return max_profit
        for buy_day,buy_price in enumerate(prices):
            for sell_day in range(buy_day+1,len(prices)):
                profit = prices[sell_day] - buy_price
                if profit>max_profit:
                    max_profit=profit
        return max_profit
        