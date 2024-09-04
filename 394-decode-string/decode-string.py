class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] == ']':
                decodeString = ""
                while stack and stack[-1]!="[":
                    decodeString += stack.pop()
                if stack[-1] == "[":
                    stack.pop()
                base = 1
                k = 0
                while stack and stack[-1].isdigit():
                    k += int(stack.pop())*base
                    base *= 10
                while k !=0:
                    for j in range(len(decodeString)-1,-1,-1):
                        stack.append(decodeString[j])
                    k-=1
            else:
                stack.append(s[i])
        return "".join(stack)