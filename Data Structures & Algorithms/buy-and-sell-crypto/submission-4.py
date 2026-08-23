class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        res = 0
        l = 0
        r = 1

        while r<len(prices):
            curr = prices[r]-prices[l]
            if curr<0:
                l=r
            res = max(res,curr)
            r+=1
        return res