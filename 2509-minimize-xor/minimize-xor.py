class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def count_bits(n):
            ct = 0
            while n>0:
                ct+=(n&1)
                n = n >> 1
            return ct
        ct1,ct2 = count_bits(num1),count_bits(num2)
        ans = num1
        i = 0
        while ct1>ct2:
            if ans & (1<<i):
                ct1-=1
                ans = ans^(1<<i)
            i+=1
        while ct1<ct2:
            if ans & (1<<i) == 0:
                ct1+=1
                ans = ans | (1<<i)
            i+=1
            
        return ans