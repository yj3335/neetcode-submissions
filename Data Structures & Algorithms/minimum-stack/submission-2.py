class MinStack:

    def __init__(self):
        self.stack = deque()
        self.heap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.heap[0]:
            heapq.heappop(self.heap)
        else:
            self.heap.remove(temp)
            heapq.heapify(self.heap)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.heap[0]
