from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        char_set = set()
        val_set = {}
        if len(word1)!=len(word2):
            return False
        mp = Counter(word1)
        values = list(mp.values())
        values.sort()
        mp2 = Counter(word2)
        for k in mp2.keys():
            if k not in mp:
                return False
        values2 = list(mp2.values())
        values2.sort()
        i = 0
        for i in range(len(values)):
            if values[i]!=values2[i]:
                return False
        return True