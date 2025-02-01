class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u,v,w in roads:
            adj_list[u].append((v,w))
            adj_list[v].append((u,w))
        q = [(0,0)]
        mindist = {i:(float("inf"),1) for i in range(n)}
        HIGH = 10**9 + 7
        while q:
            dist,u = heapq.heappop(q)
            for v,w in adj_list[u]:
                if w+dist<mindist[v][0]:
                    heapq.heappush(q,(dist+w,v))
                    mindist[v] = (w+dist,mindist[u][1])
                elif w+dist == mindist[v][0]:
                    mindist[v] = (mindist[v][0],mindist[u][1]%HIGH+mindist[v][1]%HIGH)
        return mindist[n-1][1]%HIGH
            
