from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        freq_map = Counter(s)
        hash_set = set()
        ans = 0
        for key, val in freq_map.items():
            while val>0 and val in hash_set:
                val-=1
                ans+=1
            if val > 0: 
                hash_set.add(val)
        return ans
        

