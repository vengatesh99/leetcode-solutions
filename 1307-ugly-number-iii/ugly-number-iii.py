class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left,right = 1,n*c
        ab = a*b//math.gcd(a,b)
        bc = b*c//math.gcd(b,c)
        ac = a*c//math.gcd(a,c)
        abc = a*bc//math.gcd(a,bc)
        def feasible(mid):
            return (mid//a) + (mid//b)+ (mid//c) - (mid//ab) - (mid//bc) - (mid//ac) + (mid//abc) >= n
        while left < right:
            mid = left+(right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left
