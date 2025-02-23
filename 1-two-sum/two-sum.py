class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        hashmap = {}
        for i,num in enumerate(nums):
            hashmap[num] = i
        l,r = 0,len(nums)-1
        for i in range(len(nums)):
            if target-nums[i] in hashmap and hashmap[target-nums[i]]!=i:
                return [hashmap[target-nums[i]],i]
        return [-1,-1]