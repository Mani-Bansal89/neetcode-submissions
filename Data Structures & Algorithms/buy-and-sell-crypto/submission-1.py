class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        sell_price = 0
        if len(prices)==1:
            return max_profit
        for i in range(0,len(prices)-1):
            if prices[i] < prices[i+1]:
                if buy_price >= prices[i]:
                    buy_price = prices[i]
                sell_price = prices[i+1]
            elif prices[i] > prices[i+1]:
                if i!=0 and buy_price >= prices[i+1]:
                    buy_price = prices[i+1]
                    sell_price = 0
            profit = sell_price-buy_price
            if profit>max_profit:
                max_profit=profit
        return max_profit
        