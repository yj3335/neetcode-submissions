class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        k = 1
        while k < len(nums):
            i = k
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            if i < len(nums):
                nums[count] = nums[i]
                count +=1
            k = i + 1
        return count