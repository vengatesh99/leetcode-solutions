from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = Counter(nums)
        i = 0
        key = sorted(m.keys())
        for k in key:
            if m[k]>=2:
                nums[i] = nums[i+1] = k
                i+=2
            else:
                nums[i] = k
                i+=1
        return i


            
