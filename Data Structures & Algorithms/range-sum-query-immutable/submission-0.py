class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        add = 0
        for num in self.nums:
            add += num
            self.prefix.append(add)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        if left == right:
            return self.nums[left]
        
        return self.prefix[right] - self.prefix[left-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)