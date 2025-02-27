class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dp(i,j):
            if i >= len(s) and j>=len(p):
                return True
            if j >= len(p):
                return False
            isMatch = i<len(s) and (s[i] == p[j] or p[j]=='.')
            if j<len(p)-1 and p[j+1] == "*":
                return ( isMatch and dp(i+1,j)) or dp(i,j+2)
            if isMatch:
                return dp(i+1,j+1)
            return False
        ans = dp(0,0)
        return ans