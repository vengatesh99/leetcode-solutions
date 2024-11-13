class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        ind = -1
        for i,ch in enumerate(palindrome):
            if ch!='a':
                ind = i
                break
        if len(palindrome)>1 and ind == -1:
            return palindrome[:-1]+'b'
        if len(palindrome)%2 !=0 and ind == len(palindrome)//2:
            ind+=1
            while ind<len(palindrome) and palindrome[ind]=='a':
                ind+=1
            if ind >= len(palindrome):
                return palindrome[:-1]+'b'
            return palindrome[:ind+1]+'b'+palindrome[ind+2]
        return "" if ind == -1 else palindrome[:ind]+'a'+palindrome[ind+1:]