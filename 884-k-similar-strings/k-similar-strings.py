class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        queue = [(s1,0)]
        s2_list = list(s2)
        n = len(s2)
        visit = set()
        ans = float("inf")
        while queue:
            s,level = queue.pop(0)
            if s == s2:
                return level
            cur_list = list(s)
            i = 0
            while i<n and cur_list[i] == s2_list[i]:
                i+=1
            for j in range(i,n):
                if cur_list[j] == s2_list[i] and s2_list[j]!=cur_list[j]:
                    cur_list[i],cur_list[j] = cur_list[j],cur_list[i]
                    newNeib = "".join(cur_list)
                    if newNeib not in visit:
                        queue.append((newNeib,level+1))
                        visit.add(newNeib)
                    cur_list[i],cur_list[j] = cur_list[j],cur_list[i]
        return -1