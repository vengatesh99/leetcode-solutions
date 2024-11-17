class Solution:
    def smallestSubsequence(self, s: str) -> str:
        character_map = Counter(s)
        print(character_map)
        currentSet = set()
        stack = []
        for i,ch in enumerate(s):
            character_map[ch]-=1
            if character_map[ch] == 0:
                del character_map[ch]
            if ch in stack:
                continue
            while stack and ord(stack[-1])>ord(ch) and stack[-1] in character_map:
                stack.pop()
            # if ch not in stack:
            stack.append(ch)
        return "".join(stack)