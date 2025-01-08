class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i,j = 0,0
        ans = count = 0
        while j<len(nums):
            if nums[j] == 0:
                count+=1
            else:
                ans+=(count)*(count+1)//2
                count = 0
            j+=1
        
        return ans+count*(count+1)//2 if count else ans