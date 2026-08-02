class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ans = []
        for num in arr:
            val = {num: abs(x-num)}
            heapq.heappush_max(ans, (val[num], num))
            if len(ans) > k:
                heapq.heappop_max(ans)
        return sorted([value for key,value in ans])

