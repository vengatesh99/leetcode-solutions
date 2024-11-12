class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_dict = defaultdict(set)
        ans = 0
        for i,word in enumerate(words):
            for ch in word:
                words_dict[i].add(ch)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                diff = words_dict[i]&words_dict[j]
                if not diff:
                    ans = max(ans,len(words[i])*len(words[j]))
        return ans
