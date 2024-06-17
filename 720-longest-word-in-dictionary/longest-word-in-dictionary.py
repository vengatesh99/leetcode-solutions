class Solution:
    def longestWord(self, words: List[str]) -> str:
        dict_set = set(words)
        ans = ""
        cache = {}
        def isDict(word):
            if len(word) == 0:
                return True
            if word in cache:
                return cache[word]
            if word not in dict_set:
                return False
            # word = word[:len(word)-1]
            flag = isDict(word[:-1])
            cache[word] = flag
            return cache[word]
        
        for word in words:
            if isDict(word):
                if len(ans)<len(word):
                    ans = word
                elif len(ans) == len(word):
                    ans = min(ans,word)
        return ans