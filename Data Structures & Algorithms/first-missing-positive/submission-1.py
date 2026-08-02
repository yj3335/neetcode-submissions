class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # set
        hashset = set(nums)
        for num in range(1, len(nums) + 1):
            if num not in hashset:
                return num
        return len(nums) + 1
