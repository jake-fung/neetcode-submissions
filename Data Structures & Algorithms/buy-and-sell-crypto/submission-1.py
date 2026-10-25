class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, res = 0, 1, 0
        while r < len(prices) and l < len(prices):
            net = prices[r] - prices[l]
            if net < 0:
                l = r
                r += 1
            elif net > res:
                res = net
                r+=1
            else:
                r+=1
        return res
        