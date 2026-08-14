class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {} # max in subarray l,r for alice 

        #return max for alice 
        def dfs(left, right):
            if left > right:
                return 0 
            if (left, right) in dp:
                return dp[(left, right)]

            even = ((right - left) % 2 == 0)
            l = piles[left] if even else 0 
            r = piles[right] if even else 0 

            dp[(left,right)] = max(dfs(left+1, right) + l, 
                                dfs(left, right-1)+r)
            return dp[(left,right)]

        alice_score = dfs(0, len(piles)-1)
        return True if alice_score > sum(piles) - alice_score else False