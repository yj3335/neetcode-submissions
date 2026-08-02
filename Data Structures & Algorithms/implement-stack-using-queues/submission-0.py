class ListNode:
    def __init__(self, x:int):
        self.data = x
        self.next = None

class MyStack:

    def __init__(self):
        self.stack = None

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack = ListNode(x)
        else:
            temp = ListNode(x)
            temp.next = self.stack
            self.stack = temp

    def pop(self) -> int:
        if self.stack:
            top = self.stack.data
            self.stack = self.stack.next
            return top


    def top(self) -> int:
        if self.stack:
            return self.stack.data

    def empty(self) -> bool:
        return False if self.stack else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()