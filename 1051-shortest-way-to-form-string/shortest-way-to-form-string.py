class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        ans = 0
        source_set = set(source)
        target_set = set(target)
        # print(source_set)
        # print(target_set)
        for ch in target:
            if ch not in source_set:
                return -1
        i,j = 0,0
        n,m = len(target),len(source)
        ans = 1
        while j<n:
            if i == len(source):
                i = 0
                ans+=1
                continue
            if source[i]!=target[j]:
                i+=1
            elif source[i] == target[j]:
                i+=1
                j+=1
        return ans
        