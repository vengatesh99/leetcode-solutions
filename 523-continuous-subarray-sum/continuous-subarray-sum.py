class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preMod = 0
        rem = {}
        rem[0] = -1
        for i,num in enumerate(nums):
            preMod = (preMod+num)%k
            if preMod in rem: 
                if i - rem[preMod]>1:
                    return True
            else:
                rem[preMod] = i
        return False