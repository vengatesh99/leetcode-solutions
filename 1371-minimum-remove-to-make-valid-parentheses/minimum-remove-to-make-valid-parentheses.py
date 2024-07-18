class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        i = 0
        ans = ""
        removal_set = set()
        while i<len(s):
            if s[i] == "(":
                stack.append((s[i],i))
            elif s[i] == ")":
                if len(stack) == 0:
                    removal_set.add(i)
                else:
                    stack.pop()
            i+=1

        while len(stack)!=0:
            _,index = stack.pop()
            removal_set.add(index)
        
        for i in range(len(s)):
            if i in removal_set:
                continue
            ans+=s[i]
        return ans
            
                
                
                