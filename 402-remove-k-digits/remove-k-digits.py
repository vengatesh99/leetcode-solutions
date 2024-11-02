class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if len(num) == k:
            return "0"
        for i in range(len(num)):
            while k>0 and stack and int(stack[-1])>int(num[i]):
                stack.pop()
                k-=1
            stack.append(num[i])
            end = len(stack)-1
        while k>0:
            k -=1
            end-=1
    
        ind = -1
        print(stack)
        for i,num in enumerate(stack):
            print(i,num)
            if num == "0":
                ind = i
            else:
                break
        stack = stack[ind+1:end+1]
        if not stack:
            return "0"
        return "".join(stack)