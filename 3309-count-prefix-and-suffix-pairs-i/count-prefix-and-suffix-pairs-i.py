class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # words = sorted(words, key=lambda x: len(x))
        ans = 0
        def isPrefixSuffix(word1,word2):
            ind = 0
            while ind<len(word1) and word1[ind] == word2[ind]:
                ind+=1
            k1 = len(word1)-1
            k2 = len(word2)-1
            while k1>=0 and word1[k1]==word2[k2]:
                k1-=1
                k2-=1
            return ind == len(word1) and k1 < 0

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if len(words[j])>=len(words[i]) and isPrefixSuffix(words[i],words[j]):
                    ans+=1
        return ans

