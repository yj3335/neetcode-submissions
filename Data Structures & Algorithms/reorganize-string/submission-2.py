class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        maxHeap = [[-count[i], i] for i in count]
        heapq.heapify(maxHeap)
        
        prev = None
        res = []

        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            res.append(char)
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            freq += 1
            if freq:
                prev = [freq, char]

        
        return "".join(res) if len(res) == len(s) else ""

