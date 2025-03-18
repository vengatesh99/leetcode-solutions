class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freqNum = defaultdict(int)
        for num in nums:
            freqNum[num]+=1
        nums.sort()
        ans = set()
        for i in range(len(nums)-2):
            # freqNum[nums[i]]-=1
            target = -nums[i]
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l]+nums[r]>target:
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    ans.add((nums[i],nums[l],nums[r]))
                    l+=1
                    r-=1
            
            # for j in range(i+1,len(nums)):
            #     freqNum[nums[j]]-=1
            #     rem = -nums[i]-nums[j]
            #     if rem>=nums[i] and rem>=nums[j] and freqNum[rem]  > 0:
            #         triplet = (nums[i],nums[j],rem)
            #         ans.add(triplet)
            #     freqNum[nums[j]]+=1
            # freqNum[nums[i]]+=1
        return list(ans)