class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right

        def helper(cap: int) -> bool:
            ships = 1
            cur = cap
            for w in weights:
                if cur - w < 0:
                    ships += 1
                    cur = cap
                cur -= w
            return ships <= days

        while left<=right:
            cap = left + (right-left)//2
            if helper(cap):
                res = min(res, cap)
                right = cap - 1
            else:
                left = cap + 1

        return res