class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        right = Counter(s)
        left = defaultdict(int)
        right[s[0]]-=1
        ans = set()
        for i in range(1,len(s)):
            left[s[i-1]]+=1
            right[s[i]]-=1
            for k,v in left.items():
                if k in right and min(v,right[k])>0:
                    ans.add(k+s[i]+k)
        return len(ans)
