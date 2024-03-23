class Solution:
    def fib(self, n: int) -> int:
        f0,f1 = 0,1
        if n == 0:
            return f0
        elif n == 1:
            return f1
        i = 2
        f = 0
        while i<=n:
            f = f0+f1
            f0 = f1
            f1 = f
            i+=1
        return f