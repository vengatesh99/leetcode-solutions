class Solution:
    def findMinInsertions(self,s,start,end,memo):
        if start>=end:
            return 0
        if s[start:end+1] in memo:
            return memo[s[start:end+1]]
        ans = 0
        if s[start] == s[end]:
            ans = self.findMinInsertions(s,start+1,end-1,memo)
        else:
            ans = 1+min(self.findMinInsertions(s,start+1,end,memo),self.findMinInsertions(s,start,end-1,memo))
        memo[s[start:end+1]] = ans
        return ans

    def minInsertions(self, s: str) -> int:
        memo = defaultdict(int)
        return self.findMinInsertions(s,0,len(s)-1,memo)
