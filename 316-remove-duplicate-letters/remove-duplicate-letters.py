class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # charCount = defaultdict(int)
        ans = ""
        stack = []
        seen = set()
        
        charCount = {c:i for i,c in enumerate(s)}
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i]<stack[-1] and i<charCount[stack[-1]]:
                    seen.discard(stack[-1])
                    stack.pop()
                seen.add(s[i])
                stack.append(s[i])
        return "".join(stack)
            


