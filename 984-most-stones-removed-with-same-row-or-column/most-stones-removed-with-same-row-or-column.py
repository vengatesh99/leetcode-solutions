class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
    def find(self,node):
        while node!=self.parent[node]:
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
    def removeStones(self, stones: List[List[int]]) -> int:
        sz = 0
        n = len(stones)
        uf = UnionFind(n)
        groups = n
        for i in range(n):
            for j in range(i+1,n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    groups-=uf.union(i,j)
        return n-groups

