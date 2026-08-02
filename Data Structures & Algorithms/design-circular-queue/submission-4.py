class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.count = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = ListNode(value)
        self.count += 1
        if not self.head and not self.tail:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return True 

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.count -= 1
        temp = self.head.next
        self.head = temp
        if self.count == 0:
            self.tail = self.head
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.tail.val

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()