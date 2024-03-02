class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0:-1}
        count = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count+=1
            else:
                count-=1
            if count in map:
                ans = max(ans,i-map[count])
            else:
                map[count] = i
        return ans