class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        sorted_words = sorted(words, key = lambda x: len(x))
        memo = {}
        predecessor = defaultdict(set)
        def isPredecessor(pred,actual):
            length = 0
            for i in range(len(actual)):
                if pred == actual[:i]+actual[i+1:]:
                    length+=1
                    break
            return length !=0
        def dp(index):
            if index == 0:
                return 1
            if index in memo:
                return memo[index]
            ans = 1
            for i in range(index):
                if len(sorted_words[index]) - len(sorted_words[i]) == 1 and isPredecessor(sorted_words[i],sorted_words[index]):
                    predecessor[sorted_words[index]].add(sorted_words[i])
                    ans = max(ans,1+dp(i))
            memo[index] = ans
            return memo[index]
        ans = 1
        for i in range(1,len(words)):
            ans = max(ans,dp(i))
        return ans
                