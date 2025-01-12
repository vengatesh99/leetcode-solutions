from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) == k:
            return True
        count = 0
        odd = 0
        if len(s)<k:
            return False
        hashmap = Counter(s)
        for key,v in hashmap.items():
            if v%2 == 0:
                count += 1 if not count else 0
            else:
                odd +=1
        if count == 0:
            return odd<=k
        ans = count + odd-1
        return ans <= k