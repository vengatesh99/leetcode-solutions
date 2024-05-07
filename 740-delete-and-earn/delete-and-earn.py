class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        cache = {}
        max_num = 0
        for num in nums:
            hash_map[num]+=num
            max_num = max(num,max_num)
        def dp(num):
            if num <= 0:
                return 0
            if num == 1:
                return hash_map[1]
            if num in cache:
                return cache[num]
            cache[num] = max(dp(num-2)+hash_map[num],dp(num-1))
            return cache[num]
        return dp(max_num)
        