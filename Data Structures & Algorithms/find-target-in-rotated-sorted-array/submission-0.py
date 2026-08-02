class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = 0
        left, right = 0, len(nums)-1

        while left <= right:
            if nums[left] < nums[right]:
                res = left if nums[left] <= nums[res] else res
                break
            
            mid = left + (right - left) // 2
            res = res if nums[res] <= nums[mid] else mid
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        if nums[res] <= target <= nums[len(nums)-1]:
            left, right = res, len(nums)-1
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        else:
            left, right = 0, res-1
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1