class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}

        for i in nums:
            mp[i] = mp.get(i,0)+1
        
        sorted_dict = sorted(mp.items(), key=lambda x : x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(sorted_dict[i][0])

        return ans