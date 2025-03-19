class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        i = 0
        while i<n:
            counter = defaultdict(int)
            # while i+1<n and nums[i]==nums[i+1]:
            #     i+=1
            j = n-1
            while j>i:
                complement = -(nums[i]+nums[j])
                if counter[complement]>0:
                    ans.append([nums[i],nums[j],complement])
                    while j>i and nums[j]==nums[j-1]:
                        j-=1
                counter[nums[j]]+=1
                j-=1
            i+=1
            while i<n and nums[i]==nums[i-1]:
                i+=1
        return ans