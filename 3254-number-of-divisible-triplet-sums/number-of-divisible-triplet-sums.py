class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            counter = defaultdict(int)
            for j in range(len(nums)-1,i,-1):
                ans+=counter[-(nums[i]+nums[j])%d]
                counter[nums[j]%d]+=1
        return ans