class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj_list = {}
        color = {}
        isSafe = {}
        for i,neib in enumerate(graph):
            adj_list[i] = neib
        ans = []
        def dfs(node):
            if node in isSafe:
                return isSafe[node]
            isSafe[node] = False
            for neib in adj_list[node]:
                if not dfs(neib):
                    return False
            isSafe[node] = True
            return True
        for i in range(len(graph)):
            if i not in isSafe:
                dfs(i)
        for i in range(len(graph)):
            if isSafe[i]:
                ans.append(i)
        return ans