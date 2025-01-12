class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
    def find(self,n1):
        res = n1
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1]+=self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2]+=self.rank[p1]
        return

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {}
        for i,a in enumerate(accounts):
            for email in a[1:]:
                if email in emailToAcc:
                    uf.union(i,emailToAcc[email])
                else:
                    emailToAcc[email] = i
        ans = []
        emailGroup = defaultdict(list)
        for email,i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(email)
        for i,e in emailGroup.items():
            ans.append([accounts[i][0]]+sorted(e))
        return ans


                    
        