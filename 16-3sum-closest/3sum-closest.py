class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        s = 0
        diff = float("inf")
        nums.sort()
        while i<n:
            j = i+1
            k = n-1
            while j<k:
                s1 = nums[i]+nums[j]+nums[k]
                if abs(s1-target)<diff:
                    s = s1
                    diff = abs(s-target)
                    print(i,j,k,s,diff)
                if s1>target:
                    k-=1
                elif s1<target:
                    j+=1
                else:
                    j+=1
                    k-=1
            i+=1
        print(s,diff)
        return s