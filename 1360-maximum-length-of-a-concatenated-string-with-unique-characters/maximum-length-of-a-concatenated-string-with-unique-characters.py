class Solution:
    def __init__(self):
        self.ans = 0
    def isSafe(self,newString,string):
        hashset = set()
        for ch in string:
            if ch in hashset:
                return False
            hashset.add(ch)
        for ch in newString:
            if ch in hashset:
                return False
            hashset.add(ch)
        return True
    def backtrack(self,arr,ind,string):
        for i in range(ind,len(arr)):
            if self.isSafe(arr[i],string):
                string+=arr[i]
                self.ans = max(self.ans,len(string))
                self.backtrack(arr,i+1,string)
                string = string[:-len(arr[i])]

    def maxLength(self, arr: List[str]) -> int:
        self.backtrack(arr,0,"")
        return self.ans