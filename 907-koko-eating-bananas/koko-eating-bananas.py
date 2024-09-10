class Solution:
    def calculateHours(self,piles,h):
        hours = 0
        for banana in piles:
            rem = banana%h
            hours += banana//h
            if rem!=0:
                hours+=1
        return hours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 1,max(piles)
        while lo<hi:
            mid = (lo+hi)//2
            hours = self.calculateHours(piles,mid)
            if hours<=h:
                hi = mid    
            else:
                lo = mid+1
        return hi