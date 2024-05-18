class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minValIndex,maxValIndex,n = 0,0,len(nums)-1
        for i in range(len(nums)):
            if nums[i]<nums[minValIndex]:
                minValIndex = i
            if nums[i]>=nums[maxValIndex]:
                maxValIndex = i
        print(minValIndex,maxValIndex)
        if minValIndex>maxValIndex:
            return minValIndex+n-maxValIndex-1

        return minValIndex+n-maxValIndex
        