class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = dict()
        for j in range(len(s)-minSize+1):
            word = s[j:j+minSize]
            if word in counts:
                counts[word]+=1
            else:
                if len(collections.Counter(word))<=maxLetters:
                    counts[word]=1
        return max(counts.values()) if len(counts)!=0 else 0