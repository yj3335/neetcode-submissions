class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, i = 0, len(nums)-1, 0

        def swap(j,k):
            nums[j],nums[k] = nums[k], nums[j]
        
        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(i,right)
                right -= 1
        
