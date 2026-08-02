class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # postfix array
        rightMax = [0] * len(prices)
        for i in range(len(prices)-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], prices[i+1])
        ans = 0
        for i in range(len(prices)):
            ans = max(ans, rightMax[i]-prices[i])
        return ans