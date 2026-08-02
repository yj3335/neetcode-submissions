class ListNode:
    def __init__(self, key, value):
        self.pair = {key:value}
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hashmap = [ListNode(0,0) for _ in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.hashmap)
        cur = self.hashmap[index]
        while cur.next:
            if key in cur.next.pair:
                cur.next.pair[key] = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key % len(self.hashmap)
        cur = self.hashmap[index]
        while cur.next:
            if key in cur.next.pair:
                return cur.next.pair[key]
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.hashmap)
        cur = self.hashmap[index]
        while cur.next:
            if key in cur.next.pair:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)