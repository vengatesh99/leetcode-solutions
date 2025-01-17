class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 0
        n1,n2 = 0,0
        for ch in reversed(a):
            n1 += int(ch)*(2**i)
            i+=1
        i = 0
        for ch in reversed(b):
            n2+=int(ch)*(2**i)
            i+=1
        return str(bin(n1+n2))[2:]