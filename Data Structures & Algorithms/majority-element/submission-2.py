class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ele = None
        n = len(nums)
        for num in nums:
            if count == 0:
                ele = num
                count += 1
            elif num == ele:
                count += 1
            else:
                count -= 1

        check = 0
        for num in nums:
            if num == ele:
                check += 1

        return ele if check>(n//2) else -1
