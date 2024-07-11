from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        max_heap = []
        ans = []
        hash_map = Counter(s)

        for k,v in hash_map.items():
            heappush(max_heap,(-v,k))

        while max_heap:
            count,first = heappop(max_heap)
            if len(ans)>0 and ans[-1] == first:
                if len(max_heap) == 0:
                    return ""
                count2,second = heappop(max_heap)
                ans.append(second)
                if count2+1 != 0:
                    heappush(max_heap,(count2+1,second))
                heappush(max_heap,(count,first))
                continue
            ans.append(first)
            if count+1!=0:
                heappush(max_heap,(count+1,first))
        return "".join(ans)
