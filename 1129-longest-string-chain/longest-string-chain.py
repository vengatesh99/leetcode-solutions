class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = [1 for _ in words]
        words.sort(key = lambda x: len(x))
        def isChain(w1,w2):
            c = 0
            for k in range(len(w2)):
                if w2[:k]+w2[k+1:] == w1:
                    c+=1
                    break
            return c!=0
            
        for i in range(1,len(words)):
            for j in range(i-1,-1,-1):
                if len(words[i])-len(words[j]) == 1 and isChain(words[j],words[i]):
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)