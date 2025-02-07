class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                hashmap[nums[i]*nums[j]].append((i,j))
        for k,v in hashmap.items():
            c = len(v)
            # if c > 1:
            count+=8*math.comb(c,2)
        return count
