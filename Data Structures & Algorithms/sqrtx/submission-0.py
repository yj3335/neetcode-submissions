class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left,right = 1,x
        while left<=right:
            mid = left + (right-left)//2
            sq = mid*mid
            if sq == x:
                return mid
            elif sq < x:
                left = mid+1
            else:
                right = mid-1
        return left-1    