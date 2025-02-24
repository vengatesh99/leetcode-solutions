class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        sign = "+"
        ans = 0
        stack = []
        MIN_INT = -(2**31)
        MAX_INT = (2**31 - 1)
        while i<n and s[i] == " ":
            i+=1
        if i<n and s[i] in "+-":
            sign = s[i]
            i+=1
        while i<n and s[i]>='0' and s[i]<='9':
            stack.append(int(s[i]))
            i+=1
        sz = len(stack)
        j = sz
        while stack:
            num = stack.pop()
            ans = ans+num*(10**(j-sz))
            sz-=1
        ans = ans if sign == "+" else -1*ans
        if ans < MIN_INT:
            ans = MIN_INT
        if ans>MAX_INT:
            ans = MAX_INT
        return ans