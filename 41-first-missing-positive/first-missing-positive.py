class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = set(nums)
        minimum, maximum = nums[0],nums[0]
        for num in numbers:
            minimum = min(num,minimum)
            maximum = max(num,maximum)
        maximum = 2 if maximum<0 else maximum+1
        for i in range(1,maximum):
            if i not in numbers and i!=0:
                return i
        return maximum