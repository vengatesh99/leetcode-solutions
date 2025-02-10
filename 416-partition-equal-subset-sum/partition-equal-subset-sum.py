class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 !=0:
            return False
        memo = {}
        def findSubset(i,s,target):
            if s>target or i == len(nums):
                return False
            if s == target:
                return True
            if (i,target-s) in memo:
                return memo[(i,target-s)]
            isSubset = findSubset(i+1,s+nums[i],target) or findSubset(i+1,s,target)
            memo[(i,target-s)] = isSubset
            return isSubset

        return findSubset(0,0,total//2)