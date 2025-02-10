class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones)//2
        n = len(stones)
        memo = {}
        def findSum(i,target):
            if i == n:
                return 0
            if target-stones[i]<0:
                return findSum(i+1,target)
            if (i,target) in memo:
                return memo[(i,target)]
            maxsum = max(stones[i]+findSum(i+1,target-stones[i]),findSum(i+1,target))
            memo[(i,target)] = maxsum
            return maxsum

        return sum(stones)-2*findSum(0,target)
