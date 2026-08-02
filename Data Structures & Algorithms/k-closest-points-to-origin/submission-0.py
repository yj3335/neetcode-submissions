class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #heap = [dist, (points)]
        minHeap = []
        
        def distance(x,y):
            return math.sqrt(x**2 + y**2)
        
        for x,y in points:
            dist = distance(x,y)
            heapq.heappush(minHeap, [-dist, [x,y]]) #mimic maxheap cause we want to keep closest points
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        ans = []
        for dist, point in minHeap:
            ans.append(point)

        return ans