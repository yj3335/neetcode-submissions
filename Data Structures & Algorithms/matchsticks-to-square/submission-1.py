class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sumOfSticks = sum(matchsticks)
        length = sumOfSticks // 4
        sides = [0] * 4

        if (sumOfSticks/4) !=  length:
            return False
        
        matchsticks.sort(reverse=True)

        def backtrack(index):
            if index == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[index] <= length:
                    sides[j] += matchsticks[index]
                    if backtrack(index+1): return True
                    sides[j] -= matchsticks[index]
            return False
        
        return backtrack(0)
            