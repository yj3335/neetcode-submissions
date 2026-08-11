class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}

        def dfs(index, amt):
            if amt == amount:
                return 1
            if index == len(coins) or amt > amount:
                return 0
            if (index, amt) in dp:
                return dp[(index, amt)]
            
            dp[(index, amt)] = dfs(index, amt + coins[index]) + dfs(index+1, amt)
            return dp[(index, amt)]
        
        return dfs(0, 0)