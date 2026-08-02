class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for task in tasks:
            if task not in count:
                count[task] = 0
            count[task] += 1
        
        maxHeap = [-freq for task, freq in count.items()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                fre = 1 + heapq.heappop(maxHeap)
                if fre:
                    q.append([fre, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time