class Solution:
    def checkPalin(self,string):
        if len(string)==1:
            return True
        i,j = 0,len(string)-1
        while i<j:
            if string[i] == string[j]:
                i+=1
                j-=1
                continue
            return False
        return True
            
    def checkPalinUtil(self,a,b):
        i,j = 0,len(b)-1
        while i<=j:
            if a[i] == b[j]:
                i+=1
                j-=1
            elif a[i]!=b[j]:
                if i-1<0:
                    return self.checkPalin(b)
                if self.checkPalin(b[i:j+1]) or self.checkPalin(a[i:j+1]):
                    return True
                else:
                    return False
        return True
    
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.checkPalinUtil(a,b) or self.checkPalinUtil(b,a)
