class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = float("inf")
        for string in strs:
            minLength = min(minLength, len(string))
        ind = 0
        prefix = ""
        while ind<minLength:
            nextChar = ""
            for string in strs:
                if nextChar == "":
                    nextChar = string[ind]
                    continue
                if nextChar != string[ind]:
                    return prefix
            prefix+=nextChar
            ind+=1
        return prefix
