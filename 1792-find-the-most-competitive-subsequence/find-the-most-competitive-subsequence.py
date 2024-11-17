class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        for i,num in enumerate(nums):
            remain = len(nums) - i -1
            while stack and stack[-1] > num and len(stack)+remain >=k:
                stack.pop()
            stack.append(num)
        return stack[:k]
                    