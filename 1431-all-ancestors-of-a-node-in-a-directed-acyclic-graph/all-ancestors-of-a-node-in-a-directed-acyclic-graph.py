class Solution:
    def findAncestors(self,node,visited,ancestors,adj_list):
        if node in visited:
            return
        visited.add(node)
        ancestors.append(node)
        for neib in adj_list[node]:
            self.findAncestors(neib,visited,ancestors,adj_list)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[b].append(a)
        
        ans = [[] for i in range(n)]
        for node in range(n):
            visited = set()
            ancestors = []
            self.findAncestors(node,visited,ancestors,adj_list)
            for anc in range(n):
                if anc == node:
                    continue
                if anc in ancestors:
                    ans[node].append(anc)
        return ans