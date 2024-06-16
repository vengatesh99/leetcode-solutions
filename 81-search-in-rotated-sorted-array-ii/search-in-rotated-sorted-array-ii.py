class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l,r = 0,n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[mid]>nums[l]:
                if nums[l]<=target and target<nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid]<nums[l]:
                if nums[mid]<target and target <=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                l+=1
        return nums[l] == target
