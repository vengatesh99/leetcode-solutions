class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for u,nodes in enumerate(graph):
            for v in nodes:
                adj_list[u].append(v)
                adj_list[v].append(u)
        color = [-1 for _ in range(len(graph))]
        for i in range(0,len(graph)):
            if color[i] == -1:
                queue = [(i,0)]
                while queue:
                    node,c = queue.pop(0)
                    if color[node]!=-1:
                        if color[node]!=c:
                            return False
                        continue
                    color[node] = c
                    for neib in adj_list[node]:
                        if color[neib] == -1:
                            queue.append((neib, not c))
        return True
        