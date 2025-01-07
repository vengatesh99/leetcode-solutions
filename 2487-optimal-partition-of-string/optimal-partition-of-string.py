class Solution:
    def partitionString(self, s: str) -> int:
        left,right = 0,0
        hashmap = defaultdict(int)
        hashset = set()
        ans = 1
        isbreak = False
        while right<len(s):
            if s[right] in hashset:
                ans+=1
                hashset = set()
            hashset.add(s[right])
            # while left<=right:
            #     isbreak = True
            #     hashmap[s[left]]-=1
            #     left+=1
            # hashmap[s[right]]+=1
            right+=1
            # if isbreak:
            #     ans+=1
            #     isbreak = False
        return ans