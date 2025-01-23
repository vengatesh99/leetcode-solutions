class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)
        n = len(equations)
        scope = set()
        ans = []
        for i in range(n):
            u,v = equations[i]
            w = values[i]
            scope.add(u)
            scope.add(v)
            adj_list[u].append((v,w))
            adj_list[v].append((u,1/w))
        for query in queries:
            src,dest = query[0],query[1]
            if src not in scope or dest not in scope:
                ans.append(-1)
                continue
            if src == dest:
                ans.append(1)
                continue
            q = deque()
            visit = set()
            q.append((src,1))
            isAns = False
            while q:
                sz = len(q)
                while sz>0 and q:
                    node,wt = q.popleft()
                    if node == dest:
                        ans.append(wt)
                        q = deque()
                        isAns = True
                        break
                    if node in visit:
                        continue
                    visit.add(node)
                    for neib,w in adj_list[node]:
                        if neib not in visit:
                            q.append((neib,w*wt))
                    sz-=1
            if not isAns:
                ans.append(-1)
        return ans
            
