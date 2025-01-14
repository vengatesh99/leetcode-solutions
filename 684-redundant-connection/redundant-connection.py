class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
    def find(self,node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    def union(self,n1,n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1]>self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1]+=1
        else:
            self.parent[p1] = p2
            self.rank[p2]+=1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        ans = []
        for n1,n2 in edges:
            if not uf.union(n1,n2):
                ans = [n1,n2]
        return ans
