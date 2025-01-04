class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        left,right = 1,max(bloomDay)
        target = m*k
        def isFeasible(minDay):
            bouque = 0
            i = 0
            while i<len(bloomDay):
                flowers = 0
                while i<len(bloomDay) and bloomDay[i]<=minDay and flowers<k:
                    i+=1
                    flowers+=1
                if flowers == k:
                    bouque+=1
                else:
                    i+=1
            return bouque>=m
                
        while left<right:
            mid = left+(right-left)//2
            print(left,right,mid)
            if isFeasible(mid):
                right = mid
            else:
                left = mid+1
        print(left)
        if isFeasible(left-1):
            return left-1
        return left