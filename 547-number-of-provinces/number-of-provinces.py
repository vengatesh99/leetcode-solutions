class UnionFind:
    def __init__(self,sz):
        self.parent = [i for i in range(sz)]
        self.rank = [1]*sz
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        ans = len(isConnected)
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j]:
                    ans -= uf.union(i,j)
        return ans