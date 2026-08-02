class FreqStack:

    def __init__(self):
        self.counts = {}
        self.maxCount = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        valCnt = 1 + self.counts.get(val, 0)
        self.counts[val] = valCnt
        if valCnt > self.maxCount:
            self.maxCount = valCnt
            self.stacks[self.maxCount] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        self.counts[res] -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()