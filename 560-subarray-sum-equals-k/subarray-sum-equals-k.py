class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = {0:1}
        cur_sum = 0
        count = 0
        for num in nums:
            cur_sum+=num
            count+=hm.get(cur_sum-k,0)
            hm[cur_sum] = hm.get(cur_sum,0)+1
        return count