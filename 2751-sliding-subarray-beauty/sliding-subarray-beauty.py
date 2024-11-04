class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        counter = [0]*50
        i,j = 0,0
        n = len(nums)
        ans = []
        while j<n:
            if nums[j]<0:
                counter[nums[j]+50]+=1
            while j-i+1>k:
                if nums[i]<0:
                    counter[nums[i]+50] = counter[nums[i]+50]-1
                i+=1
            if j-i+1 == k:
                count = 0
                for m in range(50):
                    count+=counter[m]
                    if count >= x:
                        ans.append(m-50)
                        break
                if count<x:
                    ans.append(0)
            j+=1
        return ans