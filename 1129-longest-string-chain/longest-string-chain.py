class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = lambda x: len(x))
        dp = [1 for _ in words]
        def isPredecessor(word_i,word_j):
            if len(word_i)-len(word_j)>1 or len(word_i)==len(word_j):
                return False
            c = 0
            k = 0
            p = 0
            while k<len(word_j) and p<len(word_i):
                if word_j[k]!=word_i[p]:
                    c+=1
                else:
                    k+=1
                p+=1
            return c<3 and k == len(word_j)
        for i in range(1,len(words)):
            m = 1
            for j in range(i-1,-1,-1):
                if isPredecessor(words[i],words[j]):
                    m = max(m,1+dp[j])
                    print(words[j],words[i])
            dp[i] = m
        print(words)
        print(dp)
        return max(dp)
