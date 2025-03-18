class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        char_freq = defaultdict(int)
        for word in words:
            for ch in word:
                char_freq[ch]+=1
        pairs = sum([v//2 for k,v in char_freq.items()])
        lengths = sorted([len(w) for w in words])
        ans = 0
        for l in lengths:
            pairsNeeded = l//2
            pairs-=pairsNeeded
            if pairs>=0:
                ans+=1
        return ans

        