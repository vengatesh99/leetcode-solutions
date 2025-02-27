class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary = sorted(dictionary, key = lambda x:(-len(x),x))
        def lcs(word,i,j):
            if i<0 or j<0:
                return 0
            l = 0
            if word[j] == s[i]:
                l = 1+lcs(word,i-1,j-1)
            else:
                l = lcs(word,i-1,j)
            return l
        for word in dictionary:
            if lcs(word,len(s)-1,len(word)-1) == len(word):
                return word
        return ""