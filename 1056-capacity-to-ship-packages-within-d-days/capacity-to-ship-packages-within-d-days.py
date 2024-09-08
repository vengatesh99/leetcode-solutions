class Solution:
    def calculateDays(self,weight,weights):
        days,wt = 0,0
        for w in weights:
            if w>weight:
                return float("inf")
            if wt + w > weight:
                days+=1
                wt = w
            else:
                wt+=w
        return days+1
            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        W = 0
        for w in weights:
            W+=w
        left,right = 1,W
        ans = 0
        while left<right:
            midW = (left+right)//2
            days_req = self.calculateDays(midW,weights)
            print(midW,days_req)
            if days_req<=days:
                right = midW
            elif days_req>days:
                left = midW+1
            
        return left
        # return left