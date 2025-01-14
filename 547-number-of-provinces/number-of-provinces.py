class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(set)
        n = len(isConnected)
        visit = set()
        for i in range(n):
            for j in range(n):
                if i!=j and isConnected[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)
        def dfs(node):
            visit.add(node)
            for neib in graph[node]:
                if neib not in visit:
                    dfs(neib)
        provinces = 0
        print(graph)
        for i in range(n):
            if i not in visit:
                dfs(i)
                provinces+=1
        return provinces