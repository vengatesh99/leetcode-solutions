class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1
        def isFeasible(mid):
            if mid%2 == 0:
                return nums[mid] == nums[mid+1]
            return nums[mid]==nums[mid-1]
        while l<r:
            mid = l+(r-l)//2
            if isFeasible(mid):
                l = mid+1
            else:
                r = mid
        return nums[l]