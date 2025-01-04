class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left,right = 0, len(nums)-1
        n = len(nums)
        # if n<2:
        #     return n-1
        # if nums[0]>nums[1]:
        #     return 0
        # if nums[n-1]>nums[n-2]:
        #     return n-1
        while left<right:
            mid = left+(right-left)//2
            # if mid == 0: 
            #     if nums[mid]>nums[mid+1]:
            #         return mid
            #     return right
            # if mid == n-1: 
            #     if nums[mid]>nums[mid-1]:
            #         return mid
            #     return left
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left

            
