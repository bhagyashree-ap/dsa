class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy=0   #best buy day
        profit=0   #max profit

        for sell in range(1, len(prices)):   #check every sell day
            if prices[sell]<prices[buy]:
                buy=sell     #found better buy 

            else:
                profit=max(profit, prices[sell]-prices[buy])    #update profit

        return profit