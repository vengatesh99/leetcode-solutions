class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i,j):
            if i >= len(s) and j>=len(p):
                return True
            if j >= len(p):
                return False
            if(i,j) in memo:
                return memo[(i,j)]
            isMatch = i<len(s) and (s[i] == p[j] or p[j]=='.')
            if j<len(p)-1 and p[j+1] == "*":
                match = ( isMatch and dp(i+1,j)) or dp(i,j+2)
                memo[(i,j)] = match
                return match
            if isMatch:
                match = dp(i+1,j+1)
                memo[(i,j)] = match
                return match
            return False
        ans = dp(0,0)
        return ans