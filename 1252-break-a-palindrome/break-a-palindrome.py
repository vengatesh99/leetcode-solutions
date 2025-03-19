class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        for i in range(ord('a'),ord('a')+26):
            for j in range(n//2):
                if palindrome[j]!=chr(i):
                    if palindrome[j]=='a':
                        return palindrome[:n-j-1]+chr(i)+palindrome[n-j:]
                    return palindrome[:j]+chr(i)+palindrome[j+1:]
        return ""
