class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left,right = 1,max(arr)
        diff = float("-inf")
        def sumNew(mid):
            sum = 0
            for num in arr:
                if num>mid:
                    sum+=mid
                else:
                    sum+=num
            return sum
        while left<right:
            mid = left+(right-left)//2
            sum = sumNew(mid)
            if sum>target:
                right = mid
            else:
                left = mid+1
        if abs(sumNew(left-1)-target) <= abs(sumNew(left)-target):
            return left-1
        return left