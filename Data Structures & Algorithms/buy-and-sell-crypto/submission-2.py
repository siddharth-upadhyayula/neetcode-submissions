class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        res = 0
        l = 0
        r = 1

        while l<r and r<len(prices):
            curr = prices[r]-prices[l]
            if prices[l]>prices[l+1]:
                l+=1
            r+=1
            res = max(curr,res)
        return res