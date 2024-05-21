class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash_map = {}
        wordDictSet = set()
        for word in wordDict:
            wordDictSet.add(word)

        def dp(string):
            if string == "":
                return False
            if len(string) == 1 and string not in wordDictSet:
                return False
            if string in wordDictSet:
                return True
            if string in hash_map:
                return hash_map[string]
            
            left,right = "",""
            for i in range(len(string)):
                left += string[i]
                right = string[i+1:]
                hash_map[left] = dp(left)
                if hash_map[left]:
                    hash_map[right] = dp(right)
                hash_map[string] = hash_map[left] and hash_map[right]
                if hash_map[string]:
                    return hash_map[string]
            return False
                
        return dp(s)
        # return hash_map[s]


