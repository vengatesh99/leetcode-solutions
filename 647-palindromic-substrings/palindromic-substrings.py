class Solution:
    def countSubstrings(self, s: str) -> int:
        #expand around centers
        count = 0
        for i in range(2):
            for l in range(len(s)):
                r = l+i
                while l>=0 and r<len(s) and s[l] == s[r]:
                    count+=1
                    l-=1
                    r+=1
        return count
            