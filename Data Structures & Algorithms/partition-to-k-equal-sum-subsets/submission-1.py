class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        target = sum(nums) / k 
        used = [False] * len(nums)

        def backtrack(index, k, subsetSum):
            if k == 0:
                return True
            
            if subsetSum == target:
                return backtrack(0, k-1, 0)
            
            for j in range(index, len(nums)):
                if used[j] or subsetSum + nums[j] > target:
                    continue
                
                used[j] = True

                if backtrack(j+1, k, subsetSum + nums[j]): return True

                used[j] = False

                if subsetSum == 0:
                    return False
            
            return False
        return backtrack(0, k, 0)
