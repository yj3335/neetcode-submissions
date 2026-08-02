class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #sort
        nums.sort()
        missing = 1
        for n in nums:
            if n<=0:
                continue
            if n == missing:
                missing += 1
        return missing
        