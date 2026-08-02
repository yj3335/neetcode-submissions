class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k: int, start: int, target: int) -> None:
            if k != 2:
                for i in range(start, len(nums)):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            else:
                left,right = start, len(nums)-1
                while left<right:
                    s = nums[left] + nums[right]
                    if s == target:
                        res.append([*quad, nums[left], nums[right]])
                        left += 1
                        while left<right and nums[left] == nums[left-1]:
                            left += 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1
        kSum(4, 0, target)
        return res  