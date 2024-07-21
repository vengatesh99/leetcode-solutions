class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 1
        prefixStr = strs[0]
        while i<len(strs):
            prefix = []
            j = 0
            string2 = strs[i]
            while j<min(len(prefixStr),len(string2)):
                if prefixStr[j] == string2[j]:
                    prefix.append(prefixStr[j])
                    j+=1
                else:
                    break
            prefixStr = "".join(prefix)
            i+=1
        return prefixStr
