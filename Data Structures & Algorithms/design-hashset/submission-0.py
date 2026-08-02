class MyHashSet:
    myList = None
    def __init__(self):
        self.myList = []

    def add(self, key: int) -> None:
        try:
            self.myList.index(key)
        except ValueError:
            self.myList.append(key)
            self.myList.sort()

    def remove(self, key: int) -> None:
        try:
            found = self.myList.index(key)
            self.myList = self.myList[:found] + self.myList[found+1:]
        except ValueError:
            pass

    def contains(self, key: int) -> bool:
        try:
            return self.myList.index(key) >= 0
        except ValueError:
            return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)