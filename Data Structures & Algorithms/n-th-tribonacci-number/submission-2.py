class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <=2:
            return 1
            
        zero, one, two = 0,1,1

        for i in range(n-2):
            temp1 = one
            temp2 = two
            two = zero + one + two
            one = temp2
            zero = temp1
        
        return two