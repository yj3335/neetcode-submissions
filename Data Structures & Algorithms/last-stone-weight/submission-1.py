class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)

        while len(heap)>1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            x,y = -x, -y

            if x != y:
                heapq.heappush(heap, -(x-y))
        
        return -heap[0] if len(heap) > 0 else 0