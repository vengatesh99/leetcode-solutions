class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums)%3 != 0:
            return []
        nums.sort()
        i = 0
        ans = []
        while i < len(nums):
            if i+2>=len(nums):
                return []
            if nums[i+2]-nums[i]>k:
                return []
            ans.append(nums[i:i+3])
            i+=3
        return ans
        