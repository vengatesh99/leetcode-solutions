from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        charCount = Counter(s)
        res = set()
        left = set()
        for c in s:
            charCount[c]-=1
            for ch in left:
                if charCount[ch]>0:
                    res.add(ch+c)
            left.add(c)
           
        return len(res)

