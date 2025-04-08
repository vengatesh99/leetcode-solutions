class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = 0
        open = 0
        stack = []
        ignore = set()
        for i,ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ")":
                if len(stack) == 0:
                    ignore.add(i)
                else:
                    stack.pop()
        ans = []
        for i in range(len(s)):
            if (stack and i == stack[0]):
                if stack:
                    stack.pop(0)
                continue
            if i in ignore:
                continue
            ans.append(s[i])
        return "".join(ans)