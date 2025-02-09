class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #boyer moore
        hashmap = {}
        for n in nums:
            hashmap[n] = 1+hashmap[n] if n in hashmap else 1
            if len(hashmap) == 2:
                k1,k2 = hashmap.keys()
                hashmap[k1]-=1
                hashmap[k2]-=1
                if hashmap[k1] == 0:
                    del hashmap[k1]
                if hashmap[k2] == 0:
                    del hashmap[k2]
        # if len(hashmap) == 1:
        return list(hashmap.keys())[0]
        