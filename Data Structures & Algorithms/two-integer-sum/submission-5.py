class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in mp:
                return [i if i<mp[diff] else mp[diff], i if i>mp[diff] else mp[diff]]
            else:
                mp[nums[i]] = i
        return [-1,-1]