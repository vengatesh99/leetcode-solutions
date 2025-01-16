class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*(n)
    def find(self,node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    def union(self,n1,n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return 0
        if self.rank[p1]>self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1]+=1
        else:
            self.parent[p1] = p2
            self.rank[p2]+=1
        return 1
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        uf = UnionFind(n)
        groups = 0
        adj_list = defaultdict(list)
        for n1,n2 in connections:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        def dfs(node):
            visit.add(node)
            for neib in adj_list[node]:
                if neib not in visit:
                    dfs(neib)

        visit = set()
        for i in range(n):
            if i not in visit:
                groups+=1
                dfs(i)
        return groups -1
        # for n1,n2 in connections:
        #     groups+=uf.union(n1,n2)
        