class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # if len(word2) == 0:
        #     return len(word1)
        memo = {}
        def dp(ind1,ind2):
            if ind2 < 0:
                return ind1+1
            if ind1 < 0:
                return ind2+1
            if(ind1,ind2) in memo:
                return memo[(ind1,ind2)]
            dist = 0
            if word1[ind1] == word2[ind2]:
                dist = dp(ind1-1,ind2-1)
            else:
                dist = 1+min(dp(ind1,ind2-1),dp(ind1-1,ind2),dp(ind1-1,ind2-1))
            memo[(ind1,ind2)] = dist
            return memo[(ind1,ind2)]
        return dp(len(word1)-1,len(word2)-1)