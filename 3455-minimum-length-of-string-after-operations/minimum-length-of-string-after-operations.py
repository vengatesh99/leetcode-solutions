from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        hashmap = Counter(s)
        rem = 0
        for key,val in hashmap.items():
            if val>=3:
                if not val%2:
                    rem += 2
                else:
                    rem += 1
            else:
                rem += val
        return rem

