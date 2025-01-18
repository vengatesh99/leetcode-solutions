class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u,v,w in times:
            adj_list[u].append((v,w))
        minheap = [(0,k)]
        visit = set()
        time = 0
        while minheap:
            t,node = heapq.heappop(minheap)
            if node in visit:
                continue
            time = max(time,t)
            visit.add(node)
            for neib,w in adj_list[node]:
                if neib not in visit:
                    heapq.heappush(minheap,(w+t,neib))
        return time if len(visit) == n else -1


