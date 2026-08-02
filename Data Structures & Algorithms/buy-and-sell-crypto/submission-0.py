class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute
        ans = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
               if prices[j] - prices[i] > 0:
                    ans = max(ans, prices[j]-prices[i])
        return ans 