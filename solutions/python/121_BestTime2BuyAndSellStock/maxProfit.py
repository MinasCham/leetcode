class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_diff = 0
        curr = prices[0]
        for i in range(1,len(prices)):
            curr = min(curr,prices[i])
            max_diff = max(max_diff,prices[i]-curr)
        return max_diff