class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_dict = defaultdict(int)
        i,j = 0,0
        n = len(s)
        ans = 0
        currentDict = defaultdict(int)
        while j<n:
            currentDict[s[j]]+=1
            while i<=j and len(currentDict)>maxLetters:
                currentDict[s[i]]-=1
                if currentDict[s[i]] == 0:
                    del currentDict[s[i]]
                i+=1
            while i<=j and j-i+1>maxSize:
                currentDict[s[i]]-=1
                if currentDict[s[i]] == 0:
                    del currentDict[s[i]]
                i+=1
            while i<=j and j-i+1>=minSize:
                substring_dict[s[i:j+1]]+=1
                ans = max(ans,substring_dict[s[i:j+1]])
                currentDict[s[i]]-=1
                if currentDict[s[i]] == 0:
                    del currentDict[s[i]]
                i+=1
            j+=1
        return ans