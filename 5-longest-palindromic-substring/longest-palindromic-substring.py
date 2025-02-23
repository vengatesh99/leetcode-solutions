class Solution:
    def longestPalindrome(self, s: str) -> str:
        #expand around center
        ans = 1
        left,right = 0,0
        n = len(s)
        for l in [0,1]:
            for k in range(n):
                i = k
                j = i+l
                c = 1 if l == 0 else 2
                while i>=0 and j<n and s[i]==s[j]:
                    c+=2
                    i-=1
                    j+=1
                if c>ans:
                    left = i+1
                    right = j-1
                    ans = c
        return s[left:right+1]