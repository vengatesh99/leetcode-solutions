class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        isOdd = nums[0]%2 != 0
        for i in range(1,len(nums)):
            if isOdd and nums[i]%2 == 0 or not isOdd and nums[i]%2!=0:
                isOdd = not isOdd
                continue
            return False
        return True
