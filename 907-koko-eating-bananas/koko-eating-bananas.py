class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right = 1,max(piles)
        def feasible(bananas):
            h1 = 0
            for pile in piles:
               h1+= ceil(pile/bananas)
            return h1
        while left<right:
            mid = left+(right-left)//2
            print(mid)
            if feasible(mid) <= h:
                right = mid
            else:
                left = mid+1
        return left