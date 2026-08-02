class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = stones
        heapq.heapify_max(self.stones)
        print(self.stones)

        while self.stones:
            x = heapq.heappop_max(self.stones)
            if self.stones:
                y = heapq.heappop_max(self.stones)
            else:
                heapq.heappush_max(self.stones, x)
                break

            if x==y:
                continue
            else:
                heapq.heappush_max(self.stones, x-y)
        
        return self.stones[0] if len(self.stones) > 0 else 0
