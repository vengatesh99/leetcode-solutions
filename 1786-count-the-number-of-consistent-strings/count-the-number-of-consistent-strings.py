class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        mask = 0
        count = 0
        for ch in allowed:
            mask = mask ^ (1<<(ord(ch)-ord('a')))
        print(mask)
        for word in words:
            isCons = True
            for ch in word:
                if mask & (1<<(ord(ch)-ord('a'))) == 0:
                    isCons = False
                    break
            if isCons:
                count+=1
        return count