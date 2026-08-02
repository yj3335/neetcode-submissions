class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in nums:
            mp[i] = mp.get(i,0)+1
        
        for val in mp.values():
            if val > 1:
                return True

        return False