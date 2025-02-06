class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dictionary = set(wordDict)
        memo = {}
        def dfs(ind):
            if ind == len(s):
                return True
            if ind in memo:
                return False
            for i in range(ind,len(s)):
                if s[ind:i+1] in wordDict and dfs(i+1):
                    return True
            memo[ind] = False
            return False
        return dfs(0)