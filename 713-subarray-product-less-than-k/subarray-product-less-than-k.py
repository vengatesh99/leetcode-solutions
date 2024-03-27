class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i,j,ans = 0,0,0
        prod = 1
        n = len(nums)
        while i<n:
            prod *= nums[i]
            while j<=i and prod>=k:
                prod//=nums[j]
                j+=1
            ans+=(i-j+1)
            i+=1

        return ans
