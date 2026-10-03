class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        minm = prices[0]
        

        for i in range(1,len(prices)):
            m = max(m,(prices[i]-minm))
            minm = min(minm,prices[i])
        return m



