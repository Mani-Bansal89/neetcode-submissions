class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        for sell_price in prices:
            max_profit=max(max_profit,sell_price-buy_price)
            if sell_price < buy_price:
                buy_price = sell_price
        return max_profit
        