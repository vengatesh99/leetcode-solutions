class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not len(nums):
            return []
        st = nums[0]
        num = st
        result = []
        n = len(nums)
        for i in range(1,n):
            if nums[i] == num+1:
                num = nums[i]
            else:
                if num == st:
                    result.append(f"{num}")
                else:
                    result.append(f"{st}->{num}")
                st = nums[i]
                num = st
        if st == num:
            result.append(f"{st}")
        else:
            result.append(f"{st}->{num}")
        return result