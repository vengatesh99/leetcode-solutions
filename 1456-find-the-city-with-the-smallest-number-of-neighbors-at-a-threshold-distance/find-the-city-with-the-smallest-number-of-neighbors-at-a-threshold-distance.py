class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_list = defaultdict(list)
        ans = -1
        mincities = float("inf")
        for u,v,w in edges:
            adj_list[u].append((v,w))
            adj_list[v].append((u,w))
        def dj(start):
            minheap = [(0,start)]
            visit = set()
            while minheap:
                w,node = heapq.heappop(minheap)
                if node in visit:
                    continue
                visit.add(node)
                for neib,nw in adj_list[node]:
                    if neib not in visit and nw+w<=distanceThreshold:
                        heapq.heappush(minheap,(nw+w,neib))
            return len(visit)-1
        for i in range(n):
            cities = dj(i)
            print(i,cities)
            if mincities>=cities:
                ans = i
                mincities = cities
        return ans