class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        num_set = set()
        for num in nums:
            num_set.add(num)

        ans = 0
        for num in num_set:
            if (num-1) not in num_set:
                count = 1
                while (num+count) in num_set:
                    count += 1
                ans = max(count, ans)

        return ans