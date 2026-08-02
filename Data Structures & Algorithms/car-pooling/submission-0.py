class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #minHeap 
        trips.sort(key=lambda t : t[1])
        minHeap = [] # store [end, numPass]
        curCap = 0 

        for t in trips:
            numPass, start, end = t

            while minHeap and minHeap[0][0] <= start:
                curCap -= minHeap[0][1]
                heapq.heappop(minHeap)

            curCap += numPass
            if curCap > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        
        return True
