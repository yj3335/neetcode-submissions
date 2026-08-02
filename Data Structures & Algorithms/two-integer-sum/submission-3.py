class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for ind,val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff], ind]
            prevMap[val] = ind
        
        return