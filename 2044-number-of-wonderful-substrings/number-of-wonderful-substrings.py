class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # quadratic soln
        mask = 0
        freq = defaultdict(int)
        freq[0] = 1
        ans = 0
        prefix = 0
        for w in word:
            mask = ord(w)-ord('a')
            prefix = prefix ^ (1<<mask)
            ans+=freq[prefix]
            for ch in ['a','b','c','d','e','f','g','h','i','j']:
                mask = ord(ch)-ord('a')
                oddPattern = prefix ^ (1<<mask)
                ans+=freq[oddPattern]
            freq[prefix]+=1
        return ans
