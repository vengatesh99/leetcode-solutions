class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left,right = 1,max(nums)
        def feasible(mid):
            ans = 0
            for num in nums:
                ans+=ceil(num/mid)
            return ans <= threshold
        while left<right:
            mid = left+(right-left)//2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left