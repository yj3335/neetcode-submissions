class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a:
            maxHeap.append([-a,'a'])
        if b:
            maxHeap.append([-b, 'b'])
        if c:
            maxHeap.append([-c, 'c'])
            
        heapq.heapify(maxHeap)

        res = []

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res.append(char2)
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, [count2,char2])
                heapq.heappush(maxHeap, [count,char])
            else:
                res.append(char)
                count += 1
                 
                if count:
                    heapq.heappush(maxHeap, [count, char])
        
        return "".join(res)