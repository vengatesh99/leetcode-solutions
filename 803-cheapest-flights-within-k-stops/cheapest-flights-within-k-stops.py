class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        for u,v,w in flights:
            adj_list[u].append((v,w))
        queue = deque()
        queue.append((src,0))
        dist = [float("inf")]*n
        stops = 0
        while queue and stops<=k:
            sz = len(queue)
            while sz > 0:
                node,wt = queue.popleft()
                for neib, w in adj_list[node]:
                    if wt+w<dist[neib]:
                        dist[neib] = wt+w
                        queue.append((neib,dist[neib]))
                sz-=1
            stops+=1
            
        return dist[dst] if dist[dst]!=float("inf") else -1
