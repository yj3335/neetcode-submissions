class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            
            if len(count)<=2:
                continue
            
            new_count = defaultdict(int)
            for key,value in count.items():
                if value > 1:
                    new_count[key] = value-1
            count = new_count

        for num in count.keys():
            c = sum([1 for i in nums if i==num])
            if c > (len(nums)//3):
                ans.append(num)
        
        return ans