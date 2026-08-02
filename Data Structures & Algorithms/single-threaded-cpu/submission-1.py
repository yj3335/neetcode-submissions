class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i) #add original index
        
        tasks.sort(key=lambda x : x[0]) #sort based on enqueue time

        minHeap, res = [], []
        i = 0
        time = tasks[0][0]

        while minHeap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1
            
            if minHeap:
                procTime, index = heapq.heappop(minHeap)
                time += procTime
                res.append(index)
            else:
                time = tasks[i][0]
        
        return res