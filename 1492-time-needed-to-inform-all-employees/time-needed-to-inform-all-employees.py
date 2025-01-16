class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = defaultdict(list)
        for i,m in enumerate(manager):
            if m != -1:
                adj_list[m].append(i)
        def bfs():
            q = deque()
            q.append((headID,0))
            visit = set()
            time = 0
            maxT = 0
            while q:
                node,t = q.popleft()
                # visit.add(node)
                time = t+informTime[node]
                if len(adj_list[node]) == 0:
                    maxT = max(maxT,time)
                for neib in adj_list[node]:
                    # if neib not in visit:
                    q.append((neib,time))
            return maxT
        return bfs()