class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left,right = 0,len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return True
            if nums[mid]>nums[left]:
                if nums[mid]>target and target>=nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            elif nums[mid]<nums[left]:
                if nums[mid]<target and target<=nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                left+=1
        return False