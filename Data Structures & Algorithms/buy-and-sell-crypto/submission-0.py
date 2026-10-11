class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)-1):
            print(prices[0:len(prices) - i - 1])
            sellpr = prices[len(prices) - i - 1]
            buypr = min(prices[0:len(prices) - i - 1])
            if sellpr - buypr > max:
                max = sellpr - buypr
        
        return max
        


        