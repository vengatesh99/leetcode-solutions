class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        left,right = 0,max(nums)
        n = len(nums)
        def feasible(target):
            # print("target",target)
            nums_copy = [num for num in nums]
            maxNum = float("-inf")
            for i in range(n-1,0,-1):
                if nums_copy[i]>target:
                    diff = nums_copy[i]-target
                    nums_copy[i] = target
                    nums_copy[i-1]+=diff
            maxNum = max(nums_copy)
            return maxNum<=target

        while left<right:
            mid = (left+right)//2
            if feasible(mid):
                right = mid
            else:
                left = mid+1
        return left