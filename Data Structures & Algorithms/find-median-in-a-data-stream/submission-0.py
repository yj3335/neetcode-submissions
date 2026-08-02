class MedianFinder:

    def __init__(self):
        self.maxHeap = [] #left
        self.minHeap = [] #right

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        if (self.maxHeap and self.minHeap and (-self.maxHeap[0]) > self.minHeap[0]):
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        
        #check imabalance
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, -val)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]

        return (self.minHeap[0] + (-self.maxHeap[0])) / 2       