class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        peak = 0

        left, right = 0, length-1
        while left<=right:
            mid = left + (right - left) // 2
            leftVal, midVal, rightVal = mountainArr.get(mid-1), mountainArr.get(mid), mountainArr.get(mid+1)

            if leftVal < midVal < rightVal:
                left = mid + 1
            elif leftVal > midVal > rightVal:
                right = mid - 1
            else:
                peak = mid
                break
        
        left, right = 0, peak
        while left<=right:
            mid = left + (right - left) // 2
            midVal = mountainArr.get(mid)

            if midVal == target:
                return mid
            elif midVal > target:
                right = mid - 1
            else:
                left = mid + 1

        left, right = peak+1, length-1
        while left<=right:
            mid = left + (right - left) // 2
            midVal = mountainArr.get(mid)

            if midVal == target:
                return mid
            elif midVal > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
            
            