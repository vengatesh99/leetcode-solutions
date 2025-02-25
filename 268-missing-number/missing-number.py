class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        def cyclicSort(i):
            while i<n:
                while nums[i]<n and nums[i]!=i:
                    # temp = nums[nums[i]]
                    # nums[nums[i]] = nums[i]
                    # nums[i] = temp
                   nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
                i+=1
        cyclicSort(0)
        for i in range(n):
            if i!=nums[i]:
                return i
        return n