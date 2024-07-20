class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        stack2 = []
        n = len(s)
        m = len(part)
        j = m-1
        for i in range(n):
            stack.append(s[i])
            while j>=0 and len(stack)>0 and stack[-1] == part[j]:
                stack2.append(stack.pop(-1))
                j-=1
            
            if j>=0:
                while stack2:
                    stack.append(stack2.pop(-1))
            stack2 = []
            j = m-1
        return "".join(stack)
            