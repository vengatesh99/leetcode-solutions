class Solution:
    def isSubsets(self, nums, target, ind, memo):
        if ind == len(nums):
            return False
        if target < 0:
            return False
        if target == 0:
            return True
        if (ind,target) in memo:
            return memo[(ind,target)]
        memo[(ind,target)] = self.isSubsets(nums,target - nums[ind],ind+1, memo) or self.isSubsets(nums,target,ind+1,memo)
        return memo[(ind,target)]

    def canPartition(self, nums: List[int]) -> bool:
        memo = {}
        total = sum(nums)
        if total % 2 != 0:
            return False 
        return self.isSubsets(nums, total // 2, 0, memo)