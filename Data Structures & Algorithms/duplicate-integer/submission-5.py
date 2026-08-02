class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        for key,value in mp.items():
            if value > 1:
                return True
        return False