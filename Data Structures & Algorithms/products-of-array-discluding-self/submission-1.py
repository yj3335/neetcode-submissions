class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # brute
        prods = [1 for _ in range(len(nums))]
        print(prods)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                prods[i] *= nums[j]
        return prods
