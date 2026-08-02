class Solution:
    def merge(self, nums: List[int], start: int, mid: int, end: int) -> None:
        temp = []
        i,j = start, mid+1
        while i<=mid and j<=end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
        while i<=mid:
            temp.append(nums[i])
            i += 1
        while j<=end:
            temp.append(nums[j])
            j += 1
        for k in range(start,end+1):
            nums[k] = temp[k - start]

    def mergeSort(self, nums: List[int], start: int, end: int) -> None:
        if start < end:
            mid = (start+end)//2
            self.mergeSort(nums, start, mid)
            self.mergeSort(nums, mid+1, end)
            self.merge(nums, start, mid, end)

    def sortArray(self, nums: List[int]) -> List[int]:
        # merge
        self.mergeSort(nums, 0, len(nums)-1)
        return nums