class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price=prices[0]
        profit=0
        for i in prices[1:]:
            if buy_price>i:
                buy_price=i
            profit=max(profit,i-buy_price)
        return profit