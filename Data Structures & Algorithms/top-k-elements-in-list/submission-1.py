class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # map and sort
        mp = defaultdict(int)
        for num in nums:
            mp[num] += 1
        mp = dict(sorted(mp.items(), key=lambda x : x[1], reverse=True)[:k])
        return [x for x in mp.keys()]
