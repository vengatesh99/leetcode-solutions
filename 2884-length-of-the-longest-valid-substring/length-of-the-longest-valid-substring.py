class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        ans = 0
        substr = ""
        forbidden_set = set(forbidden)
        right = len(word)-1
        for left in range(len(word)-1,-1,-1):
            for j in range(left,min(left+10,right+1)):
                if word[left:j+1] in forbidden_set:
                    right = j-1
                    break
            
            ans = max(ans,right-left+1)
        return ans
