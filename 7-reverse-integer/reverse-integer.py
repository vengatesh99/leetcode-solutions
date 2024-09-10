class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 -1 and x < -2**31:
            return 0
        num = abs(x)
        div = 10
        sign = 1
        reversed_num = 0
        rem = 0
        while num:
            rem = num%div
            reversed_num = reversed_num*10 + rem
            if reversed_num > 2**31 -1:
                return 0
            num = num//10
        if x<0:
            sign = -1
        return sign*reversed_num