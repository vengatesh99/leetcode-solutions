class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i,j = 0,len(s)-1
        n = len(s)
        while i<j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1
        
        I = 0
        while I<len(s):
            start = I
            end = I
            while end< n and s[end]!=" ":
                end+=1
            end1 = end-1
            while start<end1:
                temp = s[start]
                s[start] = s[end1]
                s[end1] = temp
                start+=1
                end1-=1
            I = end+1
        return s
            
        