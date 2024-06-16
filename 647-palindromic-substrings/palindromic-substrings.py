class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False if i != j else True for j in range(len(s))] for i in range(len(s))]
        # print(dp)
        # count = [[0 for _ in range(len(s))] for _ in range(len(s))]
        n = len(s)
        ans, k = n,1
        while k<len(s):
            j = k
            i = 0
            while i< n -1 and j < n:
                # if j == i:
                #     dp[i][j] = True if s[i] == s[j] else False
                if j-i == 1:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        ans+=1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]:
                        dp[i][j] = True
                        ans+=1
                i+=1
                j+=1
            k+=1
        return ans

