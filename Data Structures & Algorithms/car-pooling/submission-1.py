class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #buckets
        points = [0] * 1001
        for t in trips:
            numPass, start, end = t
            points[start] += numPass
            points[end] -= numPass
        
        curCap = 0
        for i in range(1001):
            curCap += points[i]
            if curCap > capacity:
                return False
        
        return True